'''Given a file article.txt,
Count frequency of each word (ignore case and punctuation)'''
import string

# Open file
with open("article.txt", "r") as file:
    text = file.read().lower()   # convert to lowercase

# Remove punctuation
for ch in string.punctuation:
    text = text.replace(ch, "")

# Split into words
words = text.split()

# Count frequency
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# Print result
for word, count in freq.items():
    print(word, ":", count)
