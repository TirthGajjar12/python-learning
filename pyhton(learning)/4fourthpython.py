#ch-5 data structure and file I/O

#first task

user = "1,'a',2,'b',3,4,55,'asit','nimesh'"

new_list = user.split(',') #it will split the string into a list of elements based on the comma separator

str_list = []

int_list = []

for item in new_list: #it will iterate through each item in the new_list
    if item.isdigit(): #isdigit() is a method that checks if the string consists of digits only
        int_list.append(int(item))
    else:
        str_list.append(item) 

print(max(int_list),min(int_list)) #it will print the maximum and minimum value from the integer list
str_list.reverse()
print(str_list)


#task 2

student={
's1':{
    'rollno':None,
    'name':None,
    'marks':None,
    'grade':None,
},
's2':{
    'rollno':None,
    'name':None,
    'marks':None,
    'grade':None,
},
's3':{
    'rollno':None,
    'name':None,
    'marks':None,
    'grade':None,
},
's4':{
    'rollno':None,
    'name':None,
    'marks':None,
    'grade':None,
},
's5':{
    'rollno':None,
    'name':None,
    'marks':None,
    'grade':None,
}
}

for keys in student:
    print(f"\n--- Enter details for {keys} ---")

    student[keys]['rollno'] = input('Enter a roll number: ')
    student[keys]['name'] = input('Enter your name: ')
    student[keys]['marks'] = int(input('Enter your marks: '))

for keys,values in student.items():
    marks = values['marks']

    if marks >= 90:
        values['grade'] = 'A'
    elif marks >= 80:
        values['grade'] = 'B'
    elif marks >=70:
        values['grade'] = 'C'
    elif marks >=60:
        values['grade'] = 'D'
    elif marks < 50:
        values['grade'] = 'Fail'
    else:
        values['grade'] = "invaild"

print("\n--- final students data---")
for key,value in student.items():
    print(f"{key} and {value}")
        
