# Write a function to generate a multiplication table for a number
def multiplication_table(n, limit=10):
    return [n * i for i in range(1, limit + 1)]
print(multiplication_table(5))  # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]