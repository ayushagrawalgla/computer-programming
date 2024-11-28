# Write a function to flatten a nested list
def flatten(lst):
    return [item for sublist in lst for item in sublist]
print(flatten([[1, 2], [3, 4], [5]]))  # Output: [1, 2, 3, 4, 5]