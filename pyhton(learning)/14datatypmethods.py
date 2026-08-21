#strings methods


upper = "honda".upper() #turns strings to upper case 

print(upper)
lower = "lower".lower() #turns stirng to lower case 

print(lower)
space_remove = "  tirth ".strip() #removes empty spaces from the strings

print(space_remove)
replace = "hi it was not me".replace('i','t') #replaces the string given string to existing string

print(replace)
split = "hello it me".split() #used for splting a string Default behavior → If you don’t give any separator, it splits on whitespace (spaces, tabs, newlines). You can specify a character or substring (like ",", "|", ".", etc.), and Python will split wherever that exact sequence appears.

print(split)
join_method = " ".join(["hello","world"]) #used for joing two element in string 

print(join_method)
find = "yes it is tirth and i am here".find("a") # cheack weather the given string exist in the given string

print(find)
count = "used for counting the stiring including spaces".count("i") #counts how many times the string reapetes 

print(count)

#list methods

cars = ["Honda", "Toyota", "Tesla"]


cars.append("ford") #adds an value in the last of the list 
print(cars) 

cars.extend(["bmw","audi"]) #adds more items in the list 
print(cars)

cars.remove("Honda") #Removes the first matching item
print(cars)

saved_element = cars.pop() #this removes the last element from list
print(cars)
print(saved_element)

saved_indexed = cars.pop(-1) #Removes and returns an indexed item
print(cars)
print(saved_indexed)

cars.count("bmw") #Counts an itemes
print(cars)

carst = cars.index("ford")
print(carst)


number = [3,5,44,99,85,42,65,56,248,3,485,1284,4]

number.sort()
print(number)

cars.reverse()
print(cars)

backup = cars.copy()
print(backup)

#tuple methodes it does not have a lot of methodes it has only two methods 

numbers = (23,56,78)
 
 #so this method of tuple finds the index of the  given number in this case its 2 
print(numbers.index(78)) #2


counts = number.count(56) #this methods of tuple finds where this element first appered on the tuple and finds its index number 
print(counts) # 1

#set datatype

color = {"red","blue","yellow"}

print(color)

color.add('black')
print(color)

color.update(['white','green'])
print(color)

color.remove('black') #will cause an error
print(color)

color.discard('green') #will not cause an error while removing it
print(color)

color.pop()
print(color)

#dictionary datatype

vehicle = {
    "vin": "1HGCM82633A123456",
    "make": "Honda",
    "model": "Accord",
    "price": 28000,
}


print(vehicle.get("color","unknown"))

print(vehicle.keys()) #return keys 

print(vehicle.values()) #returns value

print(vehicle.items()) #return key value pair 

vehicle.update({"color":"black"}) #if element does not exist in dictionary then it creates it and if it does then it updates it
print(vehicle)

print(vehicle.popitem()) #Removes the last inserted pair


students = [("Ravi", 82), ("Anu", 91), ("Kabir", 75)]
by_score = sorted(students, key=lambda s: s[1], reverse=True)
print(by_score)

word = ["tirth","hii","today","daksha","Y/N","sdfdsfd","wadddddddd"]

sorted_word = sorted(word,key=len)
print(sorted_word) 

#some practices

raw_model = "   tesla model 3   "
print(type(raw_model))
print(raw_model.strip()) #remove the unneccery spaces 

cars = ["honda","toyota","tesla"]

cars.append("ford")
cars.pop(1)
cars.sort()
print(cars)

prices = [12000, 25000, 31000, 18000, 45000]
new_list = sorted([i for i in prices if i>= 25000]) 
print(new_list)

vehiclet = {"make": "Honda", "model": "Civic", "price": 22000}

vehiclet.update({"year":2026})
vehiclet.update(prices=22500)
vehiclet.get("color","unknown")
print(vehiclet)
print(vehiclet.keys())

showroom_a = {"Honda", "Toyota", "Tesla"}
showroom_b = {"Tesla", "Ford", "BMW"}

print(showroom_a.intersection(showroom_b))

print(showroom_a.difference(showroom_b))

def calculate_total(price):
    return(price + price*0.08) 

print(calculate_total(30000))

vehiclestf = [
    {"make": "Honda", "price": 28000},
    {"make": "Tesla", "price": 42000},
    {"make": "Ford", "price": 26000},
]

new_vehicles = [i for i in vehiclestf if i["price"] < 30000 ]
print(new_vehicles)


vehicles = [
    {"make": "Honda", "price": 28000},
    {"make": "Tesla", "price": 42000},
    {"make": "Ford", "price": 26000},
]

average_price = sum(prices) / len(prices)
print(average_price)

#practice for key in sort method

colors = ["red", "blue", "green", "yellow", "black"]

colors.sort(key = len)
print(colors)

#2

cart = [{"item": "laptop", "price": 1200}, {"item": "mouse", "price": 25}, {"item": "keyboard", "price": 85}]

cart.sort(key = lambda x:x["price"] , reverse=True)
print(cart)

#3

athletes = [("Zane", 90), ("Aaron", 85), ("Maya", 90), ("Chloe", 85)]

athletes.sort(key = lambda x: (-x[1] , x[0] ) ) 

print(athletes)

