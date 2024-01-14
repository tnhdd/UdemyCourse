student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_Height = 0
for height in student_heights:
    total_Height += height

total_Student = 0
for num_student in student_heights:
    total_Student += 1

average_Height = round(total_Height / total_Student, 0)
print(average_Height)

"""
print(student_heights)
sumHeight = sum(student_heights)
averageHeight = sumHeight / (n + 1)
print(round(averageHeight,0))
# 156 178 165 171 187
"""
