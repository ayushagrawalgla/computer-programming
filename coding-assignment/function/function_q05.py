# Write a function to find the longest word in a list
def longest_word(words):
    return max(words, key=len)
print(longest_word(["apple", "banana", "cherry"]))  # Output: "banana"