# Write a function to find the least common multiple (LCM) of two numbers
def lcm(a, b):
    return abs(a * b) // lcm(a, b)
print(lcm(12, 15))  # Output: 60