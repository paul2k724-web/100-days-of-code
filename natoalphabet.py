import pandas as pd

# Read CSV file
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create dictionary using dictionary comprehension
phonetic_dict = {
    row.letter: row.code
    for _, row in data.iterrows()
}

# Ask user for input
word = input("Enter a word: ").upper()

# Convert word to NATO alphabet
output_list = [phonetic_dict[letter] for letter in word]

print(output_list)
