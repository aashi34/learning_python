import random
print("Welcome to the Dice Rolling Game!")

while True:
    user_input = input("Do you want to roll the dice? (y/n): ")
    if user_input.lower() == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You rolled: {dice1} and {dice2}")

    elif user_input.lower() == "n":
        print("Thanks for playing")
        exit()
        break
    
    else:
        print("Invalid input, please enter y or n")


