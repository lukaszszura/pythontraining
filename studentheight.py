student_height = input("Please place 5 student height with space between:\n" ).split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
total_hieght = 0

for height in student_height:
    total_hieght +=height
    # print(f"Total height = {total_hieght}")

number_of_student = 0

for student in student_height:
    number_of_student += 1
    # print(f"number of students = {number_of_student}")

average_height = round(total_hieght / number_of_student)
print(average_height)


