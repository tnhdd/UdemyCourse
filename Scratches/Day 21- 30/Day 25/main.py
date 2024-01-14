# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# list_temp = data["temp"].to_list()
#
# print(list_temp)
#
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp * 1.8 + 32)

# Create a data frame from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angelo"],
#     "score": [56, 67, 97]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pandas.read_csv("squirrel.csv")
data_dict = data.to_dict()
list_color = data["Primary Fur Color"].value_counts()
print(list_color)
# by_color = list_color.to_csv("bycolor.csv")
