# Find all even numbers in a list
def find_evens(lst):
    return [num for num in lst if num % 2 == 0]
print(find_evens([1, 2, 3, 4]))  # Output: [2, 4]