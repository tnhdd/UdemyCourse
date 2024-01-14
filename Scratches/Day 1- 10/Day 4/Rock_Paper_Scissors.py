import random

rock = '''Rock'''
paper = '''Paper'''
scissors = '''Scissors'''
game_image = [rock, paper, scissors]
userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
print(f"You choose {game_image[userInput]} ")
computerChoose = random.randint(0, 2)
print("Computer choose: ")
print(game_image[computerChoose])

if computerChoose == userInput:
    print("Draw")
else:
    if userInput == 0:
        if computerChoose == 1:
            print("Computer win")
        elif computerChoose == 2:
            print("You win")
    if userInput == 1:
        if computerChoose == 0:
            print("You win")
        elif computerChoose == 2:
            print("Computer win")
    if userInput == 2:
        if computerChoose == 0:
            print("Computer win")
        elif computerChoose == 1:
            print("You win")
