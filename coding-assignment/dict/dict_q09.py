# Remove duplicates from a dictionary by values
d = {'a': 1, 'b': 2, 'c': 1}
unique_dict = {k: v for k, v in d.items() if list(d.values()).count(v) == 1}
print(unique_dict)  # Output: {'b': 2}