"""EX02 - One Shot Wordle"""
__author__ = 730616700

secret_word: str = "python"
secret_idx: int = 0
word: str = input(f"What is your {len(secret_word)} guess? ")
word_idx: int = 0
boxes: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(word) != len(secret_word):
    word: str = input(f"That was not {len(secret_word)} letters! Try again: ")

while word_idx < len(word):
    if word[word_idx] == secret_word[word_idx]:
        boxes = boxes + GREEN_BOX
    else:
        char_exist: bool = False
        alt_secret_idx: int = 0
        while (not char_exist) and (alt_secret_idx < len(secret_word)):
            if secret_word[alt_secret_idx] == word[word_idx]:
                char_exist = True
            else:
                alt_secret_idx = alt_secret_idx + 1
        if char_exist:
            boxes = boxes + YELLOW_BOX
        else:
            boxes = boxes + WHITE_BOX
    word_idx = word_idx + 1
print(boxes)
    
if word == secret_word:
    print("Woo! You Got it!")
else:
    print("Not quite. Play again soon!")