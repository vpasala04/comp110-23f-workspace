"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730616700"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    single_char: str = input("Enter a single character: ")
       
if len(single_char) != 1:
    print("Error: Character must be a single character")
    exit()
else:
    print("Searching for " + single_char + " in " + word)

index: int = 0
char_count: int = 0

if word[index] == single_char:
    print(single_char + " found at index " + str(index))
    index = index + 1
    char_count = char_count + 1
else:
    index = index + 1
    
if word[index] == single_char:
    print(single_char + " found at index " + str(index))
    index = index + 1
    char_count = char_count + 1
else:
    index = index + 1
    
if word[index] == single_char:
    print(single_char + " found at index " + str(index))
    index = index + 1
    char_count = char_count + 1
else:
    index = index + 1

if word[index] == single_char:
    print(single_char + " found at index " + str(index))
    index = index + 1
    char_count = char_count + 1
else:
    index = index + 1

if word[index] == single_char:
    print(single_char + " found at index " + str(index))
    index = index + 1
    char_count = char_count + 1
else:
    index = index + 1

if char_count == 1:
    print(str(char_count) + " instance of " + single_char + " found in " + word)
else:
    if char_count != 0:
        print(str(char_count) + " instances of " + single_char + " found in " + word)
    else:
        print("No instances of " + single_char + " found in " + word)