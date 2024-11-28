# Write a function to calculate the Fibonacci sequence up to n terms
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]

