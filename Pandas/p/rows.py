import pandas as pd

df = pd.read_json("Pandas\p\sample_Data.json")
print(df)
c = df.head(10) #here we get first 5 rows if we dont give any value in the perameter
print(c)
d = df.tail(10) # here we get last 5 rows if we dont give any value in the perameter
print(d)

#we can get info about a data

print(df.info())

data = {
    "name": [
        "Rahul", "Priya", "Amit", "Neha", "Karan",
        "Sneha", "Arjun", "Pooja", "Vikas", "Anjali",
        "Rohan", "Meera", "Yash", "Kavya", "Jay"
    ],

    "age": [
        25, 28, 32, 24, 30,
        27, 35, 29, 26, 31,
        23, 34, 28, 22, 33
    ],

    "salary": [
        30000, 45000, 60000, 28000, 55000,
        40000, 75000, 48000, 35000, 65000,
        25000, 70000, 42000, 27000, 62000
    ],

    "performance_score": [
        78, 92, 85, 70, 88,
        95, 82, 76, 68, 90,
        72, 89, 84, 96, 80
    ]
}

cf = pd.DataFrame(data)

print(cf)

print(f"discriptive statastics : {cf.describe()} ")

print(f"shape of our dataset : {cf.shape}") #this is an attribute that returns a tuple that give as rows and colums

print(f"colums of our dataset : {cf.columns}  ")


print(f"columns Names : {cf[["salary" ,"name"]]}") #this was a coulmns filters

print(f"{cf[(cf["salary"] > 50000) & (cf["age"] > 30)]}") #this is rows filter and applys condition that checks if the and retruns boolean values if the conditions meets
#we have to use tuple to make sure we can write more condtions

#using or condition 
print(f"{cf[(cf["performance_score"] > 90 ) | (cf["age"] > 35)]}") 
