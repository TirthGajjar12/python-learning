#strings mthodes in python 

raw_data = "apple,banana,orange \n"
print(raw_data)
clean_data = raw_data.strip() #strip removes invisiable space and new line \n from the beginning to the end of the string
print(clean_data)
A_list = clean_data.split(',') #split is used for cutting the slice from the speretor in this case it is , and makes a list 
print(A_list)
new_string = "& ".join(A_list) #takes list of strings and joines them
print(new_string)

#lists and tuples
#list are for your go to for that changes and tuples are for that data that never changes 

apps = ['insta','facebook','x','gemini']

Ai = ['grok']

apps.append('chatGPT') #it does add an element to list but it addes in the last 
print(apps)

apps.extend(Ai) #this is used for adding the list element to another list remeber this does not add an list in another list it justs adds its element to another list in end of the list
print(apps)

item = apps.pop(2) #gives us the element from the list and element can be choosen via the index 
print(item)

#Dictionaries in python (key value pair)

user = {"name":"tirth","role":"Admin"}

print(user.get("email","No email provided")) #get method is for getting the key from the the list and if we give it an string to retrun in ew dont find the array then it does not give us error

#dictionaries loop

for key, value in user.items(): #this is how we used loops in the dictionaries and also that it we need to use .items because it covertes our dictionaries into a list 

    print(f"{key}:{value}")

#sets are fast and also used for finding something 

#but sets cant hold duplicate elements and also does not have any order

set1 = {1, 2, 3, 4}
set2 = set(["apple", "banana", "cherry"])

print(set1)   
print(set2)

#list comprehansion 

number = [1,2,3,4,5,6,7,8,9,10]

doubled_number = [num * 2 for num in number if num % 2 == 0]

print(doubled_number)

#dictonary comprehansion

names = ["Tirth","yash","parth","modi"]

final_dictonary = {name : len(name) for name in names}

print(final_dictonary)

#some practices for deep-dive concept

raw_csv = "  john_doe, 25, developer \n"

clean_data = raw_csv.strip()

data_list = clean_data.split(",")

print(data_list)

clean_list = [item.strip() for item in data_list]

print(clean_list)

#task 2 

inventory = {"apples": 50, "bananas": 20}

just = inventory.get("oranges",'we do not have oranges right now')

for key ,value in inventory.items():

    print(f"product: {key} | quantity: {value} {just}")

#task 3 


celsius_temps = [-5, 12, -2, 20, 30]

temps = [item+10 for item in celsius_temps if item > 0]

print(temps)

#task for Generators use yield to produce values lazily, one at a time, which is memory-efficient for large or infinite sequences


def fibonacci(n):

    a = 0
    b = 1

    for i in range(n):
        yield a
        a,b=b,a+b

for x in fibonacci(10):
    print(x)


def create_user(username,*roles,**profile_info):

    print(f"welcome here: {username}")

    for i in roles:

        print(f"your role : {i}")

    for key, value in profile_info.items():

        print(f"{key} : {value}")    

create_user("tirth","admin","moderator",age = 21,city = 'ahemdabad',status = "Active")        

#just a practice for the class and object in python

class Shoppingcart():

    def __init__(self,Customer_name):

        self.Customer_name = Customer_name
        self.__cart_items = []

    def add_item(self,Product_name):

        self.__cart_items.append(Product_name)
        print(self.__cart_items)    


tirth_cart =  Shoppingcart('Tirth')
tirth_cart.add_item('apple')


class Alert():

    def __init__(self,message):
        self.message = message

    def send_alert(self):
        print("Sending a generic alert")


class Email_Alert(Alert):

        def __init__(self,message):
            super().__init__(message) 

        def  send_alert(self):
            return (f'This is a {self.message} ')  


class Sms_Alert(Alert):

    def __init__(self,message):
        super().__init__(message)

    def send_alert(self):
        return (f'This is a {self.message} ')  


alert = Email_Alert('Email alert')
print(alert.send_alert())

# practices 3

salaries = [45000, 52000, 38000, 71000, 41000, 95000, 39000]

new_list = [i for i in salaries if i > 50000]

print(new_list)

#decorator 

def system_logger(func):
    def wrapper(*args,**kwrgs):
        print("LOG: Action starting...")
        func(*args,**kwrgs)
        print("LOG: Action Complete...")
    return wrapper


@system_logger
def delete_user(username):
    print(f"deleting user {username} from the database")

delete_user("tirth")

#yield 


def transaction_generator(limit):
    current_id= 1


    while current_id <= limit:
        yield current_id
        current_id = current_id + 1


print("Transaction processing...")


for trans_id in transaction_generator(5):
    print(f"processing ID : {trans_id}")



#args and kwargs 

def name_profile(name,**kwargs):
    print(f"Creating a user profile for {name}...")

    for key, value in kwargs.items():
        print(f"{key} : {value}")


name_profile('Tirth',role = 'backend dev', language = 'python', company = "Shana systems" )