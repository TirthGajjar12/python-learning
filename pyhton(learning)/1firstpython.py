print("hello world")

#in pyhton indetation is very importent and also if not given correctly it will give errors

if 60 > 12:
    print('60 is bigger')  #if we dont put a space before print in this specefic case or we can call it indetation it will give error

 #we have to use the same number of spaces in the same block of code, otherwise Python will give you an error 
if 700 < 1000:
    print('1000')
    print('nothing')    

#in pyhton variable is create when we assiagn value to it 
x = 50
y = "Tirth"

#if we have to write the both satement in the same line we can do ii by adding semicolon ; between them like this\

print('hello') ; print('world')

#we can put the end='' at the end of the statement so that the satement gets printed on the same line

print('this is tirth', end=' ')
print('this will be in the same line')


#using the numbers we can do alot of things and alos that we can used them for calculations as well

print(800 + 200)
print('this number is even',12,'check it')

#we can assasign a veirable and also make sure that it is not the same data type that it should be

x = print(str(30))
y = print(int(30))
z = print(float(30))

#here we changed the intiger data type to another so that we can see what type of that ii shows 

print(type(x))
print(type(y))
print(type(z))

#there are conditions to name the variable so there rule first is that variable name can only be sratedd by either a to z or _ 

variable_1 = 'yash'
_variable2 = 'tirth'

print(_variable2)

#there is way to name the variables and that is to use either camal case (ex:myVariableName),pascal case (ex:MyVariableName) or the snake case (ex:my_vriable_name)

#we can assign mutltiple value to the variable as well

x,y,z = 'tirth','daksh','yash'

print(x)
print(y)
print(z)

#we can assign same value to multiple variable as well 

s = t = u = "tirth"

print(s)
print(t)
print(u)

#unpaking it is used for extrecting the values from list into variables 

fruites = ['mango','watermelon','melon']

h,i,j  = fruites 

print(h)
print(i)
print(j)  

#adding two strings menas string concatination to merage two strings 

#there is type of variable named globel variable that can be used everywhere

x = 'hey it is me'

def myfuc():
    print('hi',x)  #here we can use the global veriable x in a local function 

myfuc()

#what happens if we create the same variable insdie of the local function 

x_y = 'global here'

def myfunc():
    x_y = 'local here'
    print('hi',x_y) #we redecalred the element here so it took local as priority and it satyed inside that fucnction

myfunc()

print('hi', x_y )

#fstrings in python that are used so that we can place anything in the sentence as well as how we use it and also string formatting here we are going to see that

print("my name is:%s my roll no is:%d how are you:%s"%('Tirth',12,'Tirth')) #thus is and old trick and it is not used now 

#now days we use fstring

name = 'Tirth'
department = 'computer depatment'
age = '20'
print(f'my name is {name} , i am new here , and i am from {department},my age is {age} ')

#some of the string methods 

a = 'Tirth its me'

print(len(a)) #to find length of the string 
print(a.capitalize()) #to capitalize the keyowrds 

str = 'this is an example so take it as it is'
sub = 'a'
print('count',str.count(sub)) #to cont  given latter here we counted a it provides how many tomes it is insidethat string

#to join the string in a diffrent way

s = '-'
seq = ('a','b','c')
c = s.join(seq)
print(c)
print(type(c))

#here we are seaing how we can splite the string

string = "this where we part the ways"
ls  = string.split(' ')
print(ls)

#to check if the string is uppercase and there is another way we can check if the string is lowercase

sprt = 'THIS IS IN THE UPPERCASE'
print(sprt.isupper())

#we can even force the string to convert in the upper or lowercase

str = 'this is lowercase and will be converted to uppercase'
print(str.upper())

#to replace the existing word 
skkr = 'this is and example.it is very fast'
print(skkr.replace('is','was'))

#reverse the string 
ttp = 'this is an string'
print()


