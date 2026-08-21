#Problem 1 
print("Tirth")
print("21")
print("ahmedabad")
print("maths")

length = 10
width = 5
print(f"{length*width}")

firstname = "tirth"
lastname = "gajjar"

print(f"{firstname} and {lastname}")

#x = 4


product = "car"
price = 40000
quantity = 55
In_stock = True

print(type(product))
print(type(price))
print(type(quantity))
print(type(In_stock))


random_list = [65, 81, 74, 92, 88]

sumof = sum(random_list)
print(sumof)
sumof = max(random_list)
sumof = min(random_list)


#output =  15,105,string 

#practice api

import requests

api_url = "https://api.agify.io?name=michael"

response = requests.get(api_url)

if response.status_code == 200:

    data = response.json()


    print(f"Name: {data.get('name')}")
    print(f"Estimated age: {data.get('age')}")

else:
    print(f"Error! the kiten sent back code: {response.status_code} ")


#practicse 1

players = [{"name": "Shubman", "points": 120}, {"name": "Rashid", "points": 145}, {"name": "Sudarshan", "points": 120}, {"name": "Miller", "points": 90}]

players.sort(key = lambda x: (-x["points"],x["name"]))
print(players)

#practices 2
from datetime import datetime,timedelta

exam_date = "18-November-2026"


new_exam_date = datetime.strptime(exam_date,"%d-%B-%Y")
print(new_exam_date)


