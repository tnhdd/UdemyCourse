currentAge = input("What is your current age? ")

ageLeft = 90 - int(currentAge)

monthLeft = ageLeft * 12
weeksLeft = ageLeft * 52
dayLeft = ageLeft * 365

print(f"You have {monthLeft} months , {weeksLeft} weeks, {dayLeft} days left")