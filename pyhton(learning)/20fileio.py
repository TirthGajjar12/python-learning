# #os and how to get the current working directory
# import os

# cur_folder = os.getcwd()
# print(cur_folder)

# #creating a new folder named my music

# folder_name = "My_Music"
# # os.mkdir(folder_name)

# # os.chdir(folder_name)
# # new_location = os.getcwd()
# # print(new_location)

# #renaming the file 
# os.chdir("pyhton(learning)")
# print(os.listdir())
# os.rename("temp_name.txt","final_report.txt")
# os.remove("junk_file.txt") 


#task one for this file

input_student = int(input("Enter the number of the student you want: "))

with open ("final_report.txt","w") as student_info, open("second_report.txt","w") as marks_file:
    for i in range(input_student):
        student_name = input("Enter the student name: ")
        student_rollno = int(input("Enter the roll_no of the student: "))
        student_info.write(f"{student_rollno}-{student_name}\n")
        for subject_marks in range(3):
            marks = int(input(f"Enter the {subject_marks+1} marks: "))
            marks_file.write(f"{marks}\n")


    
    