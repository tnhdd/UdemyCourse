import random

name = input("Give me random name, separated by comma ")

num_item = len(name)
random_choice_ = random.randint(0, num_item - 1)
person_who_will_pay_the_bill = name[random_choice_]
print(person_who_will_pay_the_bill + " is going to buy the meal today")
"""
import random
name = input("Give me random name, separated by comma ")
randomName = random.choice(list(name.split(",")))
print(f"{randomName} should pay the bill")



"""