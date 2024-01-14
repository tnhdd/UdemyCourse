import random
import pandas


with open("./letter_templates/letter_1.txt", "w+") as letter1:
    data = pandas.read_csv("letter_templates/test.csv")

    print(data)
