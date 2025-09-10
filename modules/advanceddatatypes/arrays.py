'''Python lists'''

a = [1, 2, 3, 4]
b = [2.4, 3.14, 9.99999]

array = []
for ii in range(10):
    array.append(ii * 100)

print(f"Array a (size={len(a)}): {a}")
print(f"Array b (size={len(b)}): {b}")
print(f"Array array (size={len(array)}): {array}")

# Iterating through an array:
total = 0
for value in a:
    total += value
print(f"The sum of {a} is {total}")
