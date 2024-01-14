print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

firstDigit = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
secondDigit = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

score = int(str(firstDigit) + str(secondDigit))

if score < 10 or score > 90:
    print(f"Your score is {score} NO")
elif 40 < score < 50:
    print(f"Good then")
else:
    print(f"Your score is {score}")