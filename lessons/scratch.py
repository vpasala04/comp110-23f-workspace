"""EX02 - One Shot Wordle"""
__author__ = 730616700

secret_word: str = "python"
secret_word_idx: int = 0
word: str = input("What is your 6-letter guess? ")
word_idx: int = 0
boxes: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(word) != len(secret_word):
    word: str = input("That was not 6 letters! Try again: ")

if len(word) == len(secret_word):
    while word_idx < len(secret_word):
        if word[word_idx] == secret_word[secret_word_idx]:
            boxes = boxes + GREEN_BOX
            word_idx = word_idx + 1
            secret_word_idx = secret_word_idx + 1
        else:
            alt_secret_idx: int = 0
            alt_word_idx: bool = False
            while (not alt_word_idx) and (alt_secret_idx < len(secret_word)):
                if secret_word[alt_secret_idx] == word[word_idx]:
                    alt_word_idx = True
                else:
                    alt_secret_idx = alt_secret_idx + 1
            if alt_word_idx:
                boxes = boxes + YELLOW_BOX
            else:
                boxes = boxes + WHITE_BOX
        word_idx = word_idx + 1
    print(boxes)

    if word == secret_word:
        print("Woo! You Got it!")
    else:
        print("Not quite. Play again soon!")
