# Remove all vowels from a string
def remove_vowels(s):
    vowels = "aeiou"
    return ''.join(char for char in s if char.lower() not in vowels)
print(remove_vowels("hello world"))  # Output: "hll wrld"