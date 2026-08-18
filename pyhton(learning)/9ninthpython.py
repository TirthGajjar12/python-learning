#task 1 python dictionary function

students = {}

number_of_student = int(input("Enter how many number of student you want to save: "))

for i in range(number_of_student):

        roll_no = int(input("Enter the roll number of the student: "))

        name = input("Enter the name of the student: ")

        marks = int(input("Enter students marks "))

students[roll_no] = [name,marks]


user_options = int(input("If you want to see roll number enter 1 , if names enter 2 else for marks enter 3: "))

if user_options == 1:

    search_roll = int(input("Enter the roll number you want to find: "))

    if search_roll in students:
        print(students[search_roll])

elif user_options == 2:

    search_name = input("Enter the name that you want to find: ")

    found = False

    for roll_no,details in students.items():
        if details[0].lower() == search_name.lower() :
             print(f'student found ! Roll No: {roll_no} | Name: {details[0]} | Marks: {details[1]}') 
    found = True

    if not found:
         print("ther are no names like this") 
elif user_options == 3:

    search_marks = int(input("Enter the marks you want to find: "))

    found = False 

    for roll_no,details in students.items():
         if details[1] == search_marks:
              print(f"students with same marks {details[0]}")
    found = True

else:
     print("Enter valid number of your informations")


