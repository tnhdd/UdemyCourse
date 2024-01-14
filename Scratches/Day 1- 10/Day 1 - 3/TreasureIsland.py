print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

firstChoice = input("Where do you want to go, left or right? ")
if firstChoice == "left":
    secondChoice = input("Do you want to swim or wait? ")
    if secondChoice == "wait":
        thirdChoice = input("Which door you want to open? ")
        if thirdChoice == "yellow":
            print("YOU WIN!!!")
        elif thirdChoice == "red":
            print('Burned by fire, GAME OVER! ')
        elif thirdChoice == "blue":
            print("Eaten by beats, GAME OVER! ")
        else:
            print("GAME OVER!!! ")
    else:
        print("You are attacked buy trout, GAME OVER! ")
else:
    print("Fall into a hole, GAME OVER! ")
