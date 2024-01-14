print("Welcome to the roller-coaster")
height = int(input("What is your height? "))
bill = 0
if height >= 120:
    print("You can ride the roller-coaster")
    age = int(input("How old are you? "))
    if age >= 18:
        print("You need to pay 12 euros")
        bill = 12
    elif 12 < age < 18:
        print("You need to pay 7 euros")
        bill = 7
    else:
        print("You need to pay 5 euros")
        bill = 5

    wantPhoto = input("Do you want a photo? Y or N ")
    if wantPhoto == "Y":
        bill += 3

    print(f"Your final bill is {bill} ")
else:
    print("You can't, sorry.")
