# AI with Python Example 6: Experiment Lab
# CSC101 - Introduction to Computing with Python
# Wraps the training steps from Example 5 in a function so you can run
# many experiments and compare them in a table. Before each experiment,
# PREDICT what will happen. Then run it and see if you were right.
#
# The settings you choose BEFORE training (epochs, learning rate, layer
# sizes) are called HYPERPARAMETERS. The model learns its parameters;
# a person chooses the hyperparameters.

import csv
import random
from pathlib import Path

import torch
import torch.nn as nn

TEST_FRACTION = 0.2
SEED = 50
SPECIES = ["setosa", "versicolor", "virginica"]

# ---------------------------------------------------------------
# 1. Load and split the data (same as Example 5)
# ---------------------------------------------------------------
csv_path = Path(__file__).resolve().parent / "iris.csv"

features = []
labels = []

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

random.seed(SEED)
indexes = list(range(len(features)))
random.shuffle(indexes)

test_size = int(len(indexes) * TEST_FRACTION)
test_indexes = indexes[:test_size]
train_indexes = indexes[test_size:]

X_train = torch.tensor([features[i] for i in train_indexes])
y_train = torch.tensor([labels[i] for i in train_indexes])
X_test = torch.tensor([features[i] for i in test_indexes])
y_test = torch.tensor([labels[i] for i in test_indexes])


# ---------------------------------------------------------------
# 2. The model (same as Example 5)
# ---------------------------------------------------------------
class IrisModel(nn.Module):
    """A neural network with two hidden layers that classifies irises."""

    def __init__(self, in_features=4, h1=8, h2=12, out_features=3):
        super().__init__()
        self.fc1 = nn.Linear(in_features, h1)
        self.fc2 = nn.Linear(h1, h2)
        self.out = nn.Linear(h2, out_features)

    def forward(self, x):
        """Send the measurements through each layer and return 3 scores."""
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.out(x)
        return x


# ---------------------------------------------------------------
# 3. One experiment = one call to this function
# ---------------------------------------------------------------
def run_experiment(epochs, learning_rate, h1, h2):
    """Train a new model with the given settings.

    Returns a tuple: (final training loss, test accuracy as a percent).
    """
    torch.manual_seed(SEED)   # every experiment starts from the same place
    model = IrisModel(h1=h1, h2=h2)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        loss = criterion(model(X_train), y_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    with torch.no_grad():
        predictions = torch.argmax(model(X_test), dim=1)
    correct = (predictions == y_test).sum().item()

    return loss.item(), correct / len(y_test) * 100


# ---------------------------------------------------------------
# 4. The experiments
# ---------------------------------------------------------------
# Each tuple is (epochs, learning rate, hidden layer 1 size, hidden layer 2
# size). The first row is the model from Example 5. Each row after it
# changes ONE setting, so you can tell what caused any difference.
# ADD YOUR OWN ROWS to the end of this list.
experiments = [
    (200, 0.01, 8, 12),     # baseline: the settings from Example 5
    (10, 0.01, 8, 12),      # far fewer epochs
    (1000, 0.01, 8, 12),    # many more epochs
    (200, 0.0001, 8, 12),   # tiny learning rate
    (200, 1.0, 8, 12),      # huge learning rate
    (200, 0.01, 1, 1),      # tiny network
    (200, 0.01, 64, 64),    # big network
]

print(f"{'Epochs':>6}{'Rate':>9}{'H1':>5}{'H2':>5}{'Loss':>10}{'Test':>9}")
print("-" * 44)

for epochs, learning_rate, h1, h2 in experiments:
    loss, test_accuracy = run_experiment(epochs, learning_rate, h1, h2)
    print(f"{epochs:>6}{learning_rate:>9}{h1:>5}{h2:>5}"
          f"{loss:>10.4f}{test_accuracy:>8.1f}%")

# QUESTIONS:
# 1. Which single change hurt the model the most? Why do you think so?
# 2. A tiny learning rate and too few epochs fail for the same reason.
#    What is it? (Think about NUDGE and STEPS in Example 3.)
# 3. Does a bigger network always give a better test score?
# 4. With only 30 test flowers, each flower is worth 3.3%. How confident
#    should you be that a 96.7% model is really better than a 93.3% one?
# 5. Find the SMALLEST network and FEWEST epochs that still reach at
#    least 90% test accuracy. Add your rows to the experiments list.
