# Remove an element from a list
def remove_element(lst, elem):
    lst.remove(elem)
    return lst
print(remove_element([1, 2, 3], 2))  # Output: [1, 3]