# Find the frequency of each character in a string
string = "hello"
frequency = {char: string.count(char) for char in set(string)}
print(frequency)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}