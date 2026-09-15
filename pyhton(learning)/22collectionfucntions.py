variable = input("Enter the variables here...")

str_list = []
int_list = []

for values in variable.split(","):
    if  values.isdigit():
        int_list.append(values)
    else:
        str_list.append(values)    



print(str_list)
print(int_list)


#task 2 

student={
's1':{
    'rollno':0,
    'name':"",
    'marks':0,
    'grade':None,
},
's2':{
    'rollno':0,
    'name':"",
    'marks':0,
    'grade':None,
},
's3':{
    'rollno':0,
    'name':"",
    'marks':0,
    'grade':None,
},
's4':{
    'rollno':0,
    'name':"",
    'marks':0,
    'grade':None,
},
's5':{
    'rollno':0,
    'name':"",
    'marks':0,
    'grade':None,
}

}

for student_id in student:
    print(f"Enter details for {student_id}")

    student[student_id]['rollno'] = int(input("Enter roll number: "))
    student[student_id]['name'] = input("Enter name: ")

    student[student_id]['marks'] = int(input("Enter marks: "))

    if student[student_id]['marks'] >= 80:
        student[student_id]['grade'] = "excellent"
    elif student[student_id]['marks'] >= 60:
        student[student_id]['grade'] = "good"
    elif student[student_id]['marks'] >= 40:
        student[student_id]['grade'] = "alright"
    else:
        student[student_id]['grade'] = "failed"

print(student)