# Insert an element at a specific index in a list
def insert_element(lst, index, elem):
    lst.insert(index, elem)
    return lst
print(insert_element([1, 2, 3], 1, 4))  # Output: [1, 4, 2, 3]