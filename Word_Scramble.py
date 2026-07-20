## Create a Word Scramble Game in Python
import random

easy_words = ["cat", "dog", "book", "tree", "fish"]
medium_words = ["python", "laptop", "science", "teacher", "student"]
hard_words = ["algorithm", "programming", "developer", "dictionary", "computer"]

def scramble(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)

def play_game(words):
    score = 0
    lives = 3

    random.shuffle(words)

    for word in words:

        scrambled = scramble(word)

        while True:

            print("\n----------------------------")
            print("Scrambled Word:", scrambled)
            print("Lives:", lives)
            print("Score:", score)

            print("\n1. Guess")
            print("2. Hint")
            print("3. Skip")

            choice = input("Enter choice: ")

            if choice == "1":

                guess = input("Enter your guess: ").lower()

                if guess == word:
                    print("✅ Correct!")
                    score += 1
                    break

                else:
                    lives -= 1
                    print("❌ Wrong!")

                    if lives == 0:
                        print("\nGame Over!")
                        print("Final Score:", score)
                        return

            elif choice == "2":
                print("💡 Hint: First letter is", word[0])

            elif choice == "3":
                print("Skipped!")
                print("Correct Word:", word)
                break

            else:
                print("Invalid choice.")

    print("\n=======================")
    print("Game Finished!")
    print("Final Score:", score)
    print("=======================")


while True:

    print("\n===== WORD SCRAMBLE GAME =====")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Exit")

    difficulty = input("Choose difficulty: ")

    if difficulty == "1":
        play_game(easy_words)

    elif difficulty == "2":
        play_game(medium_words)

    elif difficulty == "3":
        play_game(hard_words)

    elif difficulty == "4":
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice.")

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "NO":
        print("Goodbye!")
        break

