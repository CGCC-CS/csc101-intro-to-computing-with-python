# Open and read CSV file safely using 'with'
with open("books.csv") as file_obj:
    csv_rows = file_obj.readlines()   # Get list of lines (with \n)

list_csv = []
for row in csv_rows:
    row = row.strip("\n")             # Remove trailing newline
    cells = row.split(",")            # Split line into list by comma
    list_csv.append(cells)            # Add row to 2-D list

print(list_csv)                       # [['Title', 'Author'], ['1984', 'Orwell'], ...]
file_obj.close()                      # Manually close the file
