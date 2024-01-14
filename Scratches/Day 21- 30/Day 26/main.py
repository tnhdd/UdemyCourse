# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# even_num = [num for num in numbers if num % 2 == 0]
# print(even_num)

# with open("file1.txt", "r") as file1:
#     num1 = file1.read()
#     num1_ints = [int(x) for x in num1.split()]
#     print(num1_ints)
# with open("file2.txt", "r") as file2:
#     num2 = file2.read()
#     num2_ints = [int(y) for y in num2.split()]
#     print(num2_ints)
#
# mutual_num = []
# for num in num1:
#     if num in num2:
#         mutual_num.append(num)
# print(*mutual_num)

# with open("file1.txt") as file1:
#     file1_data = file1.readlines()
# with open("file2.txt") as file2:
#     file2_data = file2.readlines()
# result = [int(num) for num in file1_data if num in file2_data]
# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list_words = sentence.split()
# result = {word: len(word) for word in list_words}
# print(result)
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: temp * 9/5 + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

# for (index, row ) in student_data_frame.interrows():
#     if row.student == "X"
#         print(row.score)