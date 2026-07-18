## Hangman Game in Python

import random

words = [
    "python",
    "computer",
    "algorithm",
    "science",
    "keyboard",
    "developer",
    "internet",
    "programming",
    "software",
    "database"
]

word = random.choice(words)
guessed_letters = []
tries = 6

print("===== WELCOME TO HANGMAN =====")

while tries > 0:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed Letters:", guessed_letters)
    print("Remaining Tries:", tries)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly!")
        break

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        print("❌ Wrong Guess!")
        tries -= 1

if tries == 0:
    print("\n💀 Game Over!")
    print(f"The correct word was: {word}")