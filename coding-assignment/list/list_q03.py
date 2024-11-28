# Find the index of an element in a list
def index_of_element(lst, elem):
    return lst.index(elem) if elem in lst else -1
print(index_of_element([1, 2, 3], 2))  # Output: 1