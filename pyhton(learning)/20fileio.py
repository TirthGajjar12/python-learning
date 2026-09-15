# #os and how to get the current working directory
import os

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


    

#task 2 for this file

def input_Collection():
    file_name = input("Enter the file name: ")
    location = input("Enter the location: ")
    full_path = os.path.join(location,file_name)

    with open(full_path,"w") as My_file:
        input_number = int(input("Enter the number of line you want: "))
        for i in range(input_number):
            data = input("Enter data: ")
            My_file.write(f"{data}\n")

    with open(full_path,"r") as My_file:
        all_lines = My_file.readlines()


    Line_count = 0
    Word_count = 0
    char_with_space = 0
    char_without_spaces = 0


    for line in all_lines:
        Line_count += 1

        clean_line = line.strip('\n')

        char_with_space += len(clean_line)

        char_without_spaces += len(clean_line.replace(" ",""))

        Word_count += len(clean_line.split()) 

    print(f"total number of char in this file with space: {char_with_space} and without space: {char_without_spaces} ")


input_Collection()