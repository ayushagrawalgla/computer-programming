# Multiply elements of a list by a scalar
def multiply_by_scalar(lst, scalar):
    return [elem * scalar for elem in lst]
print(multiply_by_scalar([1, 2, 3], 2))  # Output: [2, 4, 6]