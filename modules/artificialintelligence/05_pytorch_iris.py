# AI with Python Example 5: A Neural Network with PyTorch
# CSC101 - Introduction to Computing with Python
# Trains a small neural network to identify the species of an iris flower
# from 4 measurements. It follows the same steps as Examples 1-4:
# a model with adjustable numbers, a loss, a training loop, and a test.
# The difference is that PyTorch does the math for us.
#
# Fisher, R. A. (1936). Iris. UCI Machine Learning Repository.
# https://doi.org/10.24432/C56C76

import csv
import random
from pathlib import Path

import matplotlib.pyplot as plt
import torch
import torch.nn as nn

# ---------------------------------------------------------------
# Named constants
# ---------------------------------------------------------------
TEST_FRACTION = 0.2    # hold back 20% of the flowers for testing
SEED = 50              # same seed = same results every time you run
EPOCHS = 200           # how many times to repeat the training loop
LEARNING_RATE = 0.01   # how big each adjustment is (NUDGE in Example 3)
REPORT_EVERY = 20      # print progress every 20 epochs

# A neural network only works with numbers, so each species gets a
# number. A species' number is its index in this list.
SPECIES = ["setosa", "versicolor", "virginica"]

# ---------------------------------------------------------------
# 1. Load the data (same as Example 4)
# ---------------------------------------------------------------
csv_path = Path(__file__).resolve().parent / "iris.csv"

features = []   # 4 measurements for each flower
labels = []     # species number for each flower: 0, 1, or 2

with open(csv_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        features.append([
            float(row["sepal_length"]),
            float(row["sepal_width"]),
            float(row["petal_length"]),
            float(row["petal_width"]),
        ])
        labels.append(SPECIES.index(row["species"]))

# ---------------------------------------------------------------
# 2. Shuffle and split into training and test sets (same as Example 4)
# ---------------------------------------------------------------
random.seed(SEED)
indexes = list(range(len(features)))
random.shuffle(indexes)

test_size = int(len(indexes) * TEST_FRACTION)
test_indexes = indexes[:test_size]
train_indexes = indexes[test_size:]

# ---------------------------------------------------------------
# 3. Convert the lists to tensors
# ---------------------------------------------------------------
# A TENSOR is PyTorch's version of a NumPy array: a grid of numbers that
# does math on every element at once. X is the usual name for the inputs
# and y is the usual name for the answers.
X_train = torch.tensor([features[i] for i in train_indexes])
y_train = torch.tensor([labels[i] for i in train_indexes])
X_test = torch.tensor([features[i] for i in test_indexes])
y_test = torch.tensor([labels[i] for i in test_indexes])

print("Training data shape:", X_train.shape)   # 120 flowers, 4 numbers each
print("Test data shape:", X_test.shape)        # 30 flowers, 4 numbers each
print()


# ---------------------------------------------------------------
# 4. Create the model
# ---------------------------------------------------------------
# Our model in Example 1 had 2 parameters. This one has 187, arranged in
# layers. Each nn.Linear layer is many copies of "weight * input + bias".
#
#   4 measurements -> 8 neurons -> 12 neurons -> 3 scores (one per species)
#
# class IrisModel(nn.Module) means "IrisModel is a kind of nn.Module", so
# it gets PyTorch's training abilities for free.
class IrisModel(nn.Module):
    """A neural network with two hidden layers that classifies irises."""

    def __init__(self, in_features=4, h1=8, h2=12, out_features=3):
        super().__init__()   # set up the nn.Module part of the object
        self.fc1 = nn.Linear(in_features, h1)    # input -> hidden layer 1
        self.fc2 = nn.Linear(h1, h2)             # hidden layer 1 -> 2
        self.out = nn.Linear(h2, out_features)   # hidden layer 2 -> output

    def forward(self, x):
        """Send the measurements through each layer and return 3 scores."""
        # relu changes negative numbers to 0. Without it, stacking layers
        # would be no more powerful than a single straight-line model.
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.out(x)
        return x


torch.manual_seed(SEED)   # the parameters start out as random numbers
model = IrisModel()

parameter_count = sum(p.numel() for p in model.parameters())
print("Adjustable parameters in the model:", parameter_count)

# ---------------------------------------------------------------
# 5. Choose a loss function and an optimizer
# ---------------------------------------------------------------
# The criterion measures how wrong the model is (loss() in Example 2).
# CrossEntropyLoss is the standard choice when the answer is a category.
criterion = nn.CrossEntropyLoss()

# The optimizer adjusts the parameters (the if/elif nudges in Example 3).
optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

# ---------------------------------------------------------------
# 6. Train the model
# ---------------------------------------------------------------
losses = []

for epoch in range(1, EPOCHS + 1):
    scores = model(X_train)              # guess: calling model() runs forward()
    loss = criterion(scores, y_train)    # check: how wrong were the guesses?
    losses.append(loss.item())           # .item() turns a tensor into a float

    if epoch % REPORT_EVERY == 0:
        print(f"Epoch {epoch:>3}: loss = {loss.item():.4f}")

    optimizer.zero_grad()   # clear the notes from the last epoch
    loss.backward()         # work out which way to nudge every parameter
    optimizer.step()        # nudge: adjust all the parameters

# ---------------------------------------------------------------
# 7. Test the model on flowers it has never seen
# ---------------------------------------------------------------
# torch.no_grad() tells PyTorch we are only using the model, not training.
with torch.no_grad():
    test_scores = model(X_test)

# The model gives 3 scores for each flower. The highest score wins.
# argmax gives the INDEX of the highest score, just like np.argmax().
predictions = torch.argmax(test_scores, dim=1)

correct = (predictions == y_test).sum().item()   # count the Trues
print()
print(f"Test accuracy: {correct} of {len(y_test)} correct "
      f"({correct / len(y_test) * 100:.1f}%)")


# ---------------------------------------------------------------
# 8. Classify a new flower
# ---------------------------------------------------------------
def predict_species(measurements):
    """Print and return the predicted species for one flower.

    measurements is a list of 4 numbers: sepal length, sepal width,
    petal length, and petal width, in centimeters.
    """
    with torch.no_grad():
        scores = model(torch.tensor(measurements))

    # softmax turns the 3 scores into 3 probabilities that add up to 1.
    probabilities = torch.softmax(scores, dim=0)
    species = SPECIES[torch.argmax(probabilities).item()]

    print(f"Measurements: {measurements}")
    print(f"  Predicted species: {species}")
    for i in range(len(SPECIES)):
        print(f"  {SPECIES[i]:<12}{probabilities[i].item() * 100:>6.1f}%")
    return species


print()
predict_species([5.1, 3.5, 1.4, 0.2])   # a typical setosa
predict_species([5.9, 3.0, 5.1, 1.8])   # a typical virginica

# ---------------------------------------------------------------
# 9. Save the trained model and load it back
# ---------------------------------------------------------------
# Training is the slow part. Saving the learned parameters to a file means
# another program can use the model without training it again.
model_path = Path(__file__).resolve().parent / "iris_model.pt"
torch.save(model.state_dict(), model_path)

loaded_model = IrisModel()                            # a new, untrained model
loaded_model.load_state_dict(torch.load(model_path))  # copy in the parameters
print()
print("Model saved to", model_path.name, "and loaded back.")

# ---------------------------------------------------------------
# 10. Graph the loss
# ---------------------------------------------------------------
plt.plot(range(1, EPOCHS + 1), losses)
plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()   # always last: the program pauses until you close the chart
