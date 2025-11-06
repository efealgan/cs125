# Create 2 empty lists
first_half = []
last_half = []

# Input number of words
n = int(input("How many words? "))

# Input n words
for i in range(n):
    word = input("Enter a word: ").strip()
    first_letter = word[0].lower()
    
    # Check if the word starts with A–M or N–Z
    if 'a' <= first_letter <= 'm':
        first_half.append(word)
    else:
        last_half.append(word)

# Sort the lists
first_half.sort()
last_half.sort()

# Display the lists
print("\nWords from A–M:", first_half)
print("Words from N–Z:", last_half)
