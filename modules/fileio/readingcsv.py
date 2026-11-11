import csv
from pathlib import Path

# Build a path to books.csv in the same folder as this script
csv_path = Path(__file__).resolve().parent / "books.csv"

# Open and read the CSV file safely using 'with'
with csv_path.open(newline="") as file_obj:
    # Each row becomes a list of cells
    list_csv = list(csv.reader(file_obj))

# [['Title', 'Author'], ['1984', 'Orwell'], ...]
print(list_csv)
