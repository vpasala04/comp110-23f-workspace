"""EX02 - Wordle."""
__author__ = "730616700"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(secret_word: str, search_char: str) -> bool:
    """Returns whether a character from word matches any character in secret_word"""
    assert len(search_char) == 1
    secret_word_idx: int = 0
    while secret_word_idx < len(secret_word):
        if search_char == secret_word[secret_word_idx]:
            return True
        secret_word_idx = secret_word_idx + 1
    return False

def emojified(user_guess: str, secret_word: str) -> str:
    """Returns the boxes indicating green,yellow or white codification by comparing the user_guess and secret_word strings"""
    assert len(user_guess) == len(secret_word)
    boxes: str = ""
    user_guess_idx: int = 0
    while user_guess_idx < len(user_guess):
        if user_guess[user_guess_idx] == secret_word[user_guess_idx]:
            boxes = boxes + GREEN_BOX
        elif contains_char(secret_word, user_guess[user_guess_idx]):
            boxes = boxes + YELLOW_BOX
        else:
            boxes = boxes + WHITE_BOX
        user_guess_idx = user_guess_idx + 1
    return boxes

def input_guess(expected_len: int) -> str:
    """Determines length of the user's guess for secret_word"""
    user_guess: str = input(f"Enter a {expected_len} character word: ")
    while len(user_guess) != expected_len:
        user_guess: str = input(f"That wasn't {expected_len} chars! Try again: ")
    return user_guess

def main() -> None:
    """Establishes secret_word and keeps track of how many turns the user has spent, whether the user won the game, and overall flow of the wordle game"""
    secret_word: str = "codes"
    secret_word_idx: int = 0
    current_turn: int = 1
    max_turns: int = 6
    user_guess: str = ""
    boxes: str = ""
    correct_boxes: str = ""
    correct_ans: bool = False
    secret_word_len: int = len(secret_word)
    #Establising the correct emoji box string
    while secret_word_idx < secret_word_len:
        correct_boxes = correct_boxes + GREEN_BOX
        secret_word_idx = secret_word_idx + 1
    #Comparing user_guess and secret_word and coordinating user guesses with turns
    while (current_turn <= max_turns) and (not correct_ans):
        print(f"=== Turn {current_turn}/{max_turns} ===")
        user_guess = input_guess(len(secret_word))
        boxes = emojified(user_guess, secret_word)
        print(boxes)
        if (boxes == correct_boxes):
            print(f"You won in {current_turn}/{max_turns} turns!")
            correct_ans = True
        current_turn = current_turn + 1
    if not correct_ans:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")
if __name__ == "__main__":
    main()