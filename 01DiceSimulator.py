#dice that will give th random face no when we press a key

import random

print("Welcome to dice Simulator!\n")
# print(x)
userInp = 'y'
while userInp=='y' :
    
    #TODO: Generate Random Numbers between 1 and 6
    x = random.randint(1,6)

    #TODO: check the number and get the face
    if x == 1:
        print("--------")
        print("|      |")
        print("|   *  |")
        print("|      |")
        print("--------")
    if x == 2:
        print("--------")
        print("|      |")
        print("|*    *|")
        print("|      |")
        print("--------")
    if x == 3:
        print("---------")
        print("|*      |")
        print("|   *   |")
        print("|      *|")
        print("---------")
    if x == 4:
        print("--------")
        print("|*    *|")
        print("|      |")
        print("|*    *|")
        print("--------")
    if x == 5:
        print("--------")
        print("|*    *|")
        print("|   *  |")
        print("|*    *|")
        print("--------")
    if x == 6:
        print("--------")
        print("|*    *|")
        print("|*    *|")
        print("|*    *|")
        print("--------")
        
    userInp = input("Enter y or n: ")