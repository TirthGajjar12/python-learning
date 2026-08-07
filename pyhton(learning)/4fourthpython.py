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
        

#task 3

user_txt = input("Enter paragraph: ")

with open('paragraph_save.txt','w')as User_data:
    User_data.write(user_txt) #here we are writing the user input into the file named paragraph_save.txt


with open('paragraph_save.txt','r')as User_data:
    usertext = User_data.read() #we are reading the content of the file and storing it in the variable usertext

with open('paragraph_save.txt','r') as User_data:
    lines_list = User_data.readlines() #here we are reading the content of the file and storing it in the variable lines_list as a list of lines
    total_lines = len(lines_list) #here we are counting the number of lines in the file and storing it in the variable total_lines

print(usertext) 

count_word = usertext.split() #here we are splitting the usertext into a list of words based on whitespace and storing it in the variable count_word
total_words = len(count_word) #here we are counting the number of words in the file and storing it in the variable total_words
 
print(len(usertext)) #here we are printing the total number of characters in the file including whitespace

print(len(usertext.replace(" ",""))) #here we are replacing all the whitespace in the usertext with an empty string and then counting the number of characters in the file excluding whitespace

with open('paragraph_save.txt','r') as User_data:
    lines_list = User_data.readlines() #here we are reading the content of the file and storing it in the variable lines_list as a list of lines
    lines_list.reverse() #here we are reversing the order of the lines in the list

with open('reversed_file.txt','w') as reversed_file:
    for i in lines_list:
        reversed_file.write(i) #here we are writing the reversed lines into a new file named reversed_file.txt

with open('reversed_file.txt','r') as reversed_file:
    new_reverse_string = reversed_file.read() #here we are reading the content of the reversed_file.txt and storing it in the variable new_reverse_string
    new_reverse_string = new_reverse_string.replace('is','was')  #here we are replacing all the occurrences of the word 'is' with 'was' in the new_reverse_string

with open('reversed_list.txt','w') as reversed_file:
    final_string = reversed_file.write(new_reverse_string) #we are writing the final modified string into a new file named reversed_list.txt

print(final_string) #here we are printing the total number of characters written into the reversed_list.txt file


