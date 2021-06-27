student_heights = input("Input a list of student heights : ").split()
for n in range(0, len(student_heights)) :
    student_heights[n] = int(student_heights[n])

total_height = 0
number_of_students = 0
for height in student_heights :
    number_of_students += 1
    total_height += height

average_height = total_height / number_of_students

print(f"Average height of students is {round(average_height)}.")