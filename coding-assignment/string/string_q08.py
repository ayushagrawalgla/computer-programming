# Reverse each word in a sentence
sentence = "Hello world"
reversed_words = ' '.join(word[::-1] for word in sentence.split())
print(reversed_words)