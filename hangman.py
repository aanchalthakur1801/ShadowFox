import random

words_with_hints = {
    "python": "A popular programming language.",
    "chocolate" : "A sweet treat made from cocoa.",
    "elephant": "The largest land animal.",
    "library" : "A place full of books for reading.",
    "astronaut": "A person who travels in space."
}

word, hint = random.choice(list(words_with_hints.items()))
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
print(f"Hint: {hint}")

hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    """
]

while attempts > 0 and "_" in guessed_word:
    print(hangman_stages[6 - attempts])
    print("Word: ", " ".join(guessed_word))
    print(f"Attempts left: {attempts}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess 
    else:
        attempts -= 1
        print("Incorrect guess!")

if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", word)
else:
    print(hangman_stages[6])
    print("Game over! The word was:", word)
