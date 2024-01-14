print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? "))
numPeople = int(input("How many people so split the bill? "))

amountToPay = float(totalBill + totalBill * percentage / 100)
amountEachPerson = round(float(amountToPay / numPeople), 2)

print(f"Each person should pay {amountEachPerson}")
