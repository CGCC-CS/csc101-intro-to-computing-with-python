# AI with Python

Code examples for the CSC101 AI with Python module. Each file is a short, heavily commented program you can run, read, and change. Work through them in order: Examples 1-4 build every idea by hand in plain Python, so that Example 5 (PyTorch) is the same four ideas at a larger scale.

| # | File | Needs | What it shows |
|---|---|---|---|
| 1 | `01_model_basics.py` | Nothing | A model is a function with adjustable numbers (parameters). Tune a ride-share fare model by hand. |
| 2 | `02_loss.py` | Nothing | Loss: one number that measures how wrong a model is. Mean squared error with the accumulator pattern. |
| 3 | `03_learning.py` | Nothing | Training: a loop that guesses, checks the loss, and nudges the parameters. Ends with a table that maps each piece to PyTorch. |
| 4 | `04_train_test.py` | Nothing | Loading the Iris data, shuffling and splitting it, and why a model that memorizes scores 100% in training and fails the test (overfitting). |
| 5 | `05_pytorch_iris.py` | PyTorch, Matplotlib | A neural network that classifies iris flowers: tensors, a model class, a loss function, an optimizer, the training loop, test accuracy, saving and loading. |
| 6 | `06_experiment_lab.py` | PyTorch | Runs Example 5 with different epochs, learning rates, and layer sizes and prints a comparison table. Predict, run, explain. |

`iris.csv` is the data file for Examples 4-6. Keep it in the same folder as the programs.

## The big idea

Every example, from the 2-parameter fare model to the neural network, is the same four steps:

1. **Model**: a function with adjustable numbers that turns an input into a prediction.
2. **Loss**: one number that says how wrong the predictions are.
3. **Training**: a loop that adjusts the numbers to make the loss smaller.
4. **Testing**: checking the model on data it has never seen.

| Idea | By hand (Examples 1-4) | PyTorch (Example 5) |
|---|---|---|
| Parameters | `weight`, `bias` | `model.parameters()` |
| Prediction | `predict(distance, weight, bias)` | `model(X_train)` |
| Loss | `loss(weight, bias)` | `criterion(scores, y_train)` |
| Step size | `NUDGE` | `lr` (learning rate) |
| One pass of the loop | one step | one epoch |
| Adjusting the parameters | the `if`/`elif` nudges | `loss.backward()` and `optimizer.step()` |
| Honest score | `accuracy()` on the test lists | accuracy on `X_test` |

## How to run the examples

**Examples 1-4** use only Python's standard library. Open one in VS Code and click **Run**.

**Google Colab (no setup for Examples 5-6):** PyTorch and Matplotlib are already installed. Upload `iris.csv` with the folder icon on the left, paste the code into a cell, and change the `csv_path` line to `csv_path = "iris.csv"` (a notebook has no `__file__`). In Example 5, also change the `model_path` line to `model_path = Path("iris_model.pt")`.

**VS Code:** Install the libraries once. Open the terminal and run:

```
pip install torch matplotlib
```

If `pip` is not found, try `python -m pip install torch matplotlib` (Windows) or `python3 -m pip install torch matplotlib` (Mac). PyTorch is a large download, so this can take a few minutes.

Example 5 pauses while the chart window is open. Close it to end the program. It also creates `iris_model.pt`, the saved model, in this folder.

## Vocabulary

| Term | Meaning |
|---|---|
| Model | A function with adjustable numbers that makes predictions |
| Parameter | One of the adjustable numbers (a weight or a bias) |
| Feature | An input the model looks at (petal length) |
| Label | The correct answer for one example (the species) |
| Loss | One number measuring how wrong the model is; lower is better |
| Training | Repeatedly adjusting the parameters to lower the loss |
| Epoch | One pass through the training loop |
| Learning rate | How big each adjustment is |
| Training data | The examples the model learns from |
| Test data | Examples held back to check the model honestly |
| Overfitting | Memorizing the training data instead of learning the pattern |
| Tensor | PyTorch's version of a NumPy array |
| Hyperparameter | A setting a person chooses before training (epochs, learning rate, layer sizes) |

## Common mistakes

- **`ModuleNotFoundError: No module named 'torch'`**: PyTorch is not installed in VS Code. Run the `pip install` command above, or use Colab.
- **`FileNotFoundError` for `iris.csv`**: The data file is not in the same folder as the program (or was not uploaded to Colab).
- **Testing on the training data**: A high score on data the model has already seen proves nothing. Always report the test score.
- **Forgetting to shuffle**: `iris.csv` is sorted by species. Splitting without shuffling puts one whole species in the test set.
- **Forgetting `optimizer.zero_grad()`**: PyTorch keeps adding to its notes from earlier epochs, and the model learns badly or not at all.
- **Learning rate too big or too small**: Too big and the loss jumps around and never settles. Too small and the model barely changes. Example 6 shows both.

## Course alignment

Builds on functions, loops, lists, dictionaries, file I/O, classes, and the libraries from the data analysis module.
