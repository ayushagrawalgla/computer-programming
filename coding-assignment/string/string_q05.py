# Count vowels in a string
string = "hello world"
vowels = "aeiou"
count = sum(1 for char in string.lower() if char in vowels)
print(count)  # Output: 3