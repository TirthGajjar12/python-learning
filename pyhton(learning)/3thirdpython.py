#function slide 4 there are two types of function first user define and another one is buiit-in

#task 1 

def myfucn():

    change = input('tell the value to replace:')

    replace = input('Enter the value that you want put when you change old vlaue:')


    num = input('Enter the string that you want to reverse: ') #here we take input

    print(num.replace(change,replace))

    finalString = "" #here we make an empty string
    for char in num: #start of the loop so that we can get each charater 
        finalString = char + finalString  #now in this the first chater gets saved and then a second charater gets added after the first one thats how we use this method of string reverse

    print(finalString) 




myfucn()


#before task 2 a little practice (related to task 2)

#creating the loop for making a new list from existing list practices1

teams = [['Tirth','jhon'],['Alice','bob'],['hemil','smith']]

all_players = [] #here we are colleting all the elements from the teams list

for iteam in teams:  #first we are gettings this elements ['Tirth','jhon']
    for element in iteam: #then breaking them down one by one 
        all_players.append(element) #then adding them to final list named all_players

print(all_players) 

#
news = [items for sublist in teams for items in sublist ] #fastest way to make a loop and implement thinges that are done above this practices.it is wrapped in [ ], Python automatically knows it is supposed to build a new list, so you don't even have to write the word .append()

print(news)

#practices 2


class_1 = [45,82,34]
class_2 = [55,91,48]
class_3 = [77,21,60]


def analyze_score(*args):
    all_scores = [items for sublist in args for items in sublist]

    curved_scores = list(map(lambda x:x + 5,all_scores)) 

    passed_score = list(filter(lambda y: y >= 50 ,curved_scores))

    print(passed_score)


analyze_score(class_1,class_2,class_3)


#main assingment


master_list = []

num_of_list = int(input('Enter the number of list that you want to create: '))

for i in range(num_of_list):
    current_list = []
    total_elements = int(input('how may element for this list: '))
    for z in range(total_elements):
        elements = int(input('Enter the element that you want to add'))
        current_list.append(elements)
    master_list.append(current_list)

def calculate(*args):
    list_count = len(args)

    if list_count == 1:
        print(args[0])
    elif list_count == 2:
        combaine2 = args[0]+args[1]
        print(max(combaine2),min(combaine2))
    elif list_count == 3:
        combaine3 = args[0]+args[1]+args[2]
        print(sum(combaine3))  
    else:
        new_list = [iteam for sublist in args for iteam in sublist]

        middle_list = list(map(lambda x: x * x,new_list))

        final_list = list(filter(lambda x: x % 2 != 0,middle_list))

        print(final_list)

calculate(*master_list)

#some practice for assignment 2

import os 

#to find exextly where the python script is running 
current_location = os.getcwd()
print(f"i am currently running inside {current_location}")

#create a brand new folder
os.mkdir('My_test_folder!')
print("successfully created test folder")

#for creating and make sure that we have everything in the folder we are lisitng here 
folder_contents = os.listdir(current_location)
print(f"successfully listing the content {folder_contents}")

#removing the folder so it does not create any unneccery issues 
os.rmdir('My_test_folder!')
print('successfully deleted not wanted folder')

#assasingment 2 
def write_data(n):


    with open("studentInfo.txt", "w") as info_file, open("studentMarks.txt", "w") as marks_file: #this is the main thing here we are opening the file and giving it a name that we can use ,if this file existes they will be over written and if not it will be created 
        for i in range(n):
            roll_no = int(input("Enter students roll number: "))
            name = input("Enter students name: ")
            m1 = int(input("Enter the first marks: "))
            m2 = int(input("Enter the second marks: "))
            m3 = int(input("Enter the third marks: "))

            info_file.write(f"{roll_no}-{name}\n") # here we are saving it 
            marks_file.write(f"{roll_no}-{m1}-{m2}-{m3}\n")

total_students = int(input("Enter the number"))


write_data(total_students)

