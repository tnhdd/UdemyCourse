height = float(input("Enter your height in m "))
weight = float(input("Enter your weight in kg "))

bmi = float(weight / height ** 2)
bmiRounded = round(bmi, 2)
print(f"Your bmi is {bmiRounded}")

if bmiRounded < 18.5:
    print("You're underweight")
elif 18.5 <= bmiRounded < 25:
    print("You're normal weight")
elif 25 <= bmiRounded < 30:
    print("You're overweight")
elif 30 <= bmiRounded < 35:
    print("You're obese")
else:
    print("You're clinically obese")
