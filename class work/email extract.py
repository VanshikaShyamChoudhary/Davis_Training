'''From a file data.txt, Extract all valid email addresses and save them into emails.txt'''
import string

emails = set()

with open("data.txt", "r") as file:
    words = file.read().split()

for word in words:
    # Remove punctuation from start/end
    clean_word = word.strip(string.punctuation)
    
    # Basic email validation
    if "@" in clean_word:
        parts = clean_word.split("@")
        
        if len(parts) == 2 and "." in parts[1]:
            emails.add(clean_word)

# Write to file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Emails extracted successfully!")
