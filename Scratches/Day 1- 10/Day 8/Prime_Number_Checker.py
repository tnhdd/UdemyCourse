# Write your code below this line 👇


def prime_checker(number):
    is_Prime = True
    for i in range(2, number):
        if number % i == 0:
            is_Prime = False
    if is_Prime:
        print(f"{n} is prime number")
    else:
        print(f"{n} is not a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))

prime_checker(number=n)
