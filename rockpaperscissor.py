import random

computer = random.choice([-1, 0, 1])  
youstr = input("Enter your choice: ")
youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "rock", -1: "paper", 0: "scissor"}

if youstr not in youDict:
    print("Invalid choice!")
    exit()
you = youDict[youstr]

print("you chose", reverseDict[you], "Computer chose", reverseDict[computer])


if(computer == you):
    print("its a draw")

else:
    if(computer == -1 and you == 1):
        print("you lose")
        
    elif(computer == -1 and you == 0):
        print("you win")
        
    elif(computer == 1 and you == -1):
        print("you win")
        
    elif(computer == 1 and you == 0):
        print("you lose")
        
    elif(computer == 0 and you == -1):
        print("you lose")
        
    elif(computer == 0 and you == 1):
        print("you win")
        
    else:
        print("Something went wrong")