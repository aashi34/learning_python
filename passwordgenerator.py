import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

length = int(input("Enter the length of the password: "))
password = ""

for i in range(length):
    password+= random.choice(characters)
print(password)
