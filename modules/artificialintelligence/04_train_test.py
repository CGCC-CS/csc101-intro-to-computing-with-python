# AI with Python Example 4: Training Data vs. Test Data
# CSC101 - Introduction to Computing with Python
# How do you know a model really learned something? You test it on data
# it has never seen. This program builds two flower classifiers and shows
# why a perfect score on the training data can be meaningless.
#
# The data is the Iris data set: 150 flowers from 3 species, with 4
# measurements each (in centimeters).
# Fisher, R. A. (1936). Iris. UCI Machine Learning Repository.
# https://doi.org/10.24432/C56C76

import csv
import random
from pathlib import Path

# ---------------------------------------------------------------
# Named constants
# ---------------------------------------------------------------
TEST_FRACTION = 0.2   # hold back 20% of the flowers for testing
SEED = 50             # same seed = same shuffle every time you run

# ---------------------------------------------------------------
# 1. Load the data
# ---------------------------------------------------------------
# Build a path to iris.csv in the same folder as this script
csv_path = Path(__file__).resolve().parent / "iris.csv"

features = []   # the measurements: what the model gets to look at
labels = []     # the species: the answer the model should give

with open(csv_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        measurements = (
            float(row["sepal_length"]),
            float(row["sepal_width"]),
            float(row["petal_length"]),
            float(row["petal_width"]),
        )
        features.append(measurements)
        labels.append(row["species"])

print("Flowers loaded:", len(features))
print("First flower:", features[0], "->", labels[0])

# ---------------------------------------------------------------
# 2. Shuffle, then split into training and test sets
# ---------------------------------------------------------------
# The file is sorted by species, so we must shuffle first. Otherwise the
# test set would be the last 30 rows: all one species.
# We shuffle a list of INDEXES so features and labels stay lined up.
random.seed(SEED)
indexes = list(range(len(features)))
random.shuffle(indexes)

test_size = int(len(indexes) * TEST_FRACTION)
test_indexes = indexes[:test_size]     # first 20% of the shuffled indexes
train_indexes = indexes[test_size:]    # everything else

train_features = [features[i] for i in train_indexes]
train_labels = [labels[i] for i in train_indexes]
test_features = [features[i] for i in test_indexes]
test_labels = [labels[i] for i in test_indexes]

print("Training flowers:", len(train_features))
print("Test flowers:", len(test_features))
print()

# ---------------------------------------------------------------
# 3. Model A: memorize the training data
# ---------------------------------------------------------------
# A dictionary that maps each set of measurements to its species.
# This is like studying for an exam by memorizing the answer key.
answer_key = {}
for i in range(len(train_features)):
    answer_key[train_features[i]] = train_labels[i]


def predict_memorizer(measurements):
    """Return the memorized species, or "unknown" if never seen before."""
    return answer_key.get(measurements, "unknown")


# ---------------------------------------------------------------
# 4. Model B: a simple rule
# ---------------------------------------------------------------
# Petal length (index 2) separates the species fairly well. The cutoffs
# 2.5 and 4.8 came from looking at the TRAINING flowers only.
def predict_rule(measurements):
    """Return a species based on petal length."""
    petal_length = measurements[2]
    if petal_length < 2.5:
        return "setosa"
    elif petal_length < 4.8:
        return "versicolor"
    else:
        return "virginica"


# ---------------------------------------------------------------
# 5. Accuracy: what fraction did the model get right?
# ---------------------------------------------------------------
def accuracy(model, flower_features, flower_labels):
    """Return the percent of flowers the model labels correctly.

    model is a FUNCTION. Passing a function as an argument lets this
    one accuracy function score any model.
    """
    correct = 0
    for i in range(len(flower_features)):
        if model(flower_features[i]) == flower_labels[i]:
            correct += 1
    return correct / len(flower_features) * 100


# ---------------------------------------------------------------
# 6. Compare the two models
# ---------------------------------------------------------------
print(f"{'Model':<12}{'Training':>10}{'Test':>10}")
print("-" * 32)
print(f"{'Memorizer':<12}"
      f"{accuracy(predict_memorizer, train_features, train_labels):>9.1f}%"
      f"{accuracy(predict_memorizer, test_features, test_labels):>9.1f}%")
print(f"{'Rule':<12}"
      f"{accuracy(predict_rule, train_features, train_labels):>9.1f}%"
      f"{accuracy(predict_rule, test_features, test_labels):>9.1f}%")

# The memorizer looks perfect on the training data and falls apart
# on the test data. It did not learn anything about flowers; it learned
# the answer key. When a model does this it is called OVERFITTING.
#
# The rule scores about the same on both. It learned a real pattern, so
# it still works on flowers it has never seen. The test score is the
# honest one, which is why Example 5 holds back test data too.

# TRY IT:
# 1. Why is the memorizer's test score not exactly 0%?
#    (Hint: can two different flowers have the same measurements?)
# 2. Change the cutoffs in predict_rule. Can you beat the test accuracy?
# 3. If you tuned the cutoffs by checking the test score over and over,
#    would the test score still be an honest measurement?
