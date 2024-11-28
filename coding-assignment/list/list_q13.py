# Find the frequency of each element in a list
def frequency(lst):
    return {item: lst.count(item) for item in set(lst)}
print(frequency([1, 2, 2, 3, 4, 4]))  # Output: {1: 1, 2: 2, 3: 1, 4: 2}