# Create a dictionary from a list with indices as keys
lst = ['apple', 'banana', 'cherry']
d = {i: lst[i] for i in range(len(lst))}
print(d)  # Output: {0: 'apple', 1: 'banana', 2: 'cherry'}