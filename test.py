import statistics



students = {"Pedro": [100, 50,],
            "Miguel": [50, 60],
            "Ze": [30, 80] }

# entering a grade for a student
def enter_grade():
    studententer  = input("which student? ")
    grade = input("Please enter grade: ")
    students[studententer].append(int(grade))

# Removing a student from the system
def remove_student():
    student = input("which student? ")
    del students[student]
    print("The student was removed")

# Calculate the average grade of a student
def average():
    student = input("which student? ")
    print("The average of ", student, " is ", statistics.mean(students[student]))

# There should be a log-in system to allow only admin access to the grading system.
password = " "

while password != "patorras":
    password = input("Please insert pass: ")
else:
    print("Welcome")


#The user should be able to select whether he/she wants to remove a student, enter grades for a student or find the average grades.
print("what do you pretend?")
action = input("""Please enter: \"enter grade\" to enter a grade,
              \"remove student\" to remove a student,
              \"enter average\" to calculate the average.  """)

if action == "enter grade":
    enter_grade()
elif action == "remove student":
    remove_student()
elif action == "average":
    average()



print(students)
