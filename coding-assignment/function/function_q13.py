# Write a function to calculate the sum of digits in a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
print(sum_of_digits(123))  # Output: 6