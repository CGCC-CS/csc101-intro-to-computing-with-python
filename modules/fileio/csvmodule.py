import csv

# Read CSV using csv module (handles quotes, commas in fields)
with open("books.csv", newline='') as file_obj:
    reader = csv.reader(file_obj)
    list_csv = [row for row in reader]  # List comprehension

print(list_csv)
