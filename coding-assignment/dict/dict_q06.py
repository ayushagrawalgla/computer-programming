# Sort a dictionary by values
d = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_dict)  # Output: {'b': 1, 'c': 2, 'a': 3}