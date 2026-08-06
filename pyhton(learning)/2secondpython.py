#if else satement in pyhton ex:

i = 15
if i < 30:
    print('i is less then 30')
else:
    print('i is greater then 30')

#in if-else when we write the first statment we have to put first condtion as true under the if and and we have to put second condtions as flase or opposite in the else 
# but if we need more condition then these if and else we can use elif 

i = 50
if i < 10:
    print('i is less then 10') 
elif i > 10 :
    print('i is bigger then 10')
elif i == 50 :
    print('i is 50')
else:
    print('i is not present')

#we can use the nested if else so that we can have if-else statment inside an if-else here is an example :

x = -1

if x < 0:   #here we are using if-else and also nested if else inside of the if else condtion
    x = 0 
    print('negetive changed to zero')
    if x == 0:
        print('zero')
    elif x ==1:
        print('single')
        if x == 0:
            print('zero')
    else:
        print('more')

#there are two operators in the python 'and' operator and 'or' operator
a = False
b = True

if a or b: #here the or checks weather the a or b condtion have true or not, it checks weather one of the statement is true then and noly it prints
    print('hello1')

c = True
d = True

if c and d: #here the and checks weather the c and d both condtions are true or not if both are theo then and then only it prints 
    print('hello2')

#lets see the useage of the comparison operators

print(a==b) #false
print(a!=b) #True
print(a>b) #False
print(a<b) #True
print(a>=b) #False
print(a<=b) #True

#aretmetic operators

H = 3
I = 2

print(H+I)
print(H-I)
print(H*I)
print(H/I)
print(H%I)
print(H**I)
print(H//I)


#labs for learning

TI = True

if(TI): #this condition checks if TI is true  
    print(TI) #this prints because it is true
else:  #and this cehcks if it is false 
    print(TI) #code does not come here it skips this because the codtion was true


# xyz = int(input('Enter interger value'))
xyz = 0
if xyz < 0:
    xyz = 0
    if xyz == 0:
        print('x is zero')
    elif xyz==1:
        print('x is one')
        if xyz == 0:
            print('x is zero')
        else:
            print('more')


#loops 

for i in range(1,10,3): #used for iterting inside the loops 1 shows where to start and 10 shows where to stop and 3 here menas  is the step (the increment). It tells Python how much to add to the loop variable on each iteration
    print(i)

#here we are going to see how we can loop the string and can print each latter one by one 

zm = 'hi its me tirth and how are you'

for i in zm:
    print('each letter here', i)

print(range(10))   #it shows total range object and also rnage object range(0,10)

AZ = ['Tirth','Yash','Parth','Shlok','Hit','Harsh']

# for i in AZ: 
    # print('this is each element in the list',i)
print(len(AZ)) #this shows total numbers of the string that are present in the list

for i in range(len(AZ)): #first the len(AZ) gets 6 as number then when the loops runs i goes and assigns 1 to 0 and so on and prints the output like this 0 Tirth
    print(i,AZ[i])

for i in range(20,30):
    print('index',i) 


lf = ['hello' for x in range (5)] #this creates list containg 5 hellos ['hello', 'hello', 'hello', 'hello', 'hello']
print(lf)


#this while loop example and also how to use them 

count = 0   

while count < 10:
    print(count)
    count += 1  #here we are seeing that example of infinte loop
else:
    print('in else')
    print('count')    

#exercies here user input 

#1

xlm = input('Enter a character: ')

if xlm == 'a':
    print('you have enterd a')
elif xlm == 'b':
    print('you have enterd b')
elif xlm == 'c':
    print('you have enterd c')
else:
    print('invalid character')

#2

num = int(input('Enter a number: '))

if num >= 0:
    if num % 2 != 0:
        num = num + 1
        print(num)
    elif num % 2 == 0:
        num = num*30.1
        print(num)
elif num <= 0:
    if num%2 != 0:
         num = num-10
         print(num)
    elif num%2 == 0:
         num = num/30.1
         print(num)
else:
    print('Enter a vlaid number')            

#3

marks = int(input("Enter your marks for checking the grades: "))

if 90 <= marks <= 100:
    print('A grade') 
elif 80 <= marks <= 90:
    print('B grade')
elif 80 <= marks <= 50:
    print('C grade')
elif 50 <= marks <= 40:
    print('D grade')
elif marks <= 40:
    print('your failed')
else:
    print('invaild')


#4
num_row = int(input('Enter the valid number of the rows that you want: '))


for i in range(1,num_row+1): #so the 1 to num_row here is row that we can use and also that we have to add +1 because if user writes 4 then the rows will only go to 3 thats way
    for c in range(0,i): #this is columns and loop inside a loop that detetmines how many columns that we need from the i in the first loop
        print( 1 ,end='') #used for printing 1 and ending without any space annd completeting on the same line

    print() # for adding the new line

#5 

num_row = int(input('Enter a vlaid number of the rows that you want: ')) #this one is for a prograsive pyramid of numbers

current_number = 1

for i in range(1,num_row+1):
    for c in range(0,i):
        print(current_number,end='')

        current_number = current_number+1
    print()  


#6
    # this is for the reverse or upside down pyramid
for i in range(5,0,-1):
    for c in range(0,i):
        print('*',end='')

    print()  

#7 for creating dimamond

row = int(input('Enter the total numbar of the rows: '))


for current_rows in range(1,row + 1):

    for s in range(row-current_rows):
        print(" ",end='')

    for r in range(current_rows):
        print("* ", end='') 

    print()       

#8 creating diamond 
rows = int(input('Enter your number for the diamond: ')) #first we take input from the users 

for current_row in range(1,rows+1): #then using for loop we are using the +1 so that we reach our desired number

    for s in range(rows-current_row): #minues the current postion of current in first loop from total rows thats how much space we need 
        print(" ",end='')

    for c in range(current_row): #then we print total number of stars that we need in the current row
        print("* ",end='')

    print() #we use this print to go to the next line after the first loop is completed

for revers_row in range(rows-1,0,-1):# we use this loop to print the reverse of the first loop so that we can get the diamond shape and also we use -1 so that it goes in reverse order

    for s in range(rows-revers_row):#we use this loop to print the spaces in the reverse order so that we can get the diamond shape and also we use -1 so that it goes in reverse order
            print(" ",end='')
    
    for c in range(revers_row):#we use this loop to print the stars in the reverse order so that we can get the diamond shape and also we use -1 so that it goes in reverse order 
            print("* ",end='')

    print()        

#9 creating factorial number calcullation


num = int(input('Enter a number: ')) #a factorial is the product of all positive integers less than or equal to that number.

factotial = 1 #keep the 1 

current_number = num 


while current_number > 0: #till the number go to 0 the loop will keep going 
    factotial = factotial * current_number 
    current_number = current_number - 1

print(f'the factorial of {num} is {factotial}') 