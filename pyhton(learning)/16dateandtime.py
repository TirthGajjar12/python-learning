#date and time module 
from datetime import datetime , timedelta

current_method = datetime.now()
print(current_method) #current_method is python object not a string even tho it does look like a string 

today  = datetime.now()

#to add time in existing time we use timedelta fucntion 


thirty_days = timedelta(days=30)

expairation_date = today + thirty_days

print(f"your product expires on {expairation_date}")

#there are two ways we can date into a string
#metod 1

today = datetime.now()

pretty_date = today.strftime("%y-%m-%d")
print(pretty_date)

#method 2 this are used when we need data from the databse or from input or from the function but it is not stirng that we have to conver it 


database_string = "12/08/2026"

real_date = datetime.strptime(database_string, "%d/%m/%Y")
print(real_date,type(real_date))

#practice 1


def currenttime_func():
    today =  datetime.now()
    today_year = today.strftime("%y")
    today_month = today.strftime("%m")
    print(f"year: {today_year} month: {today_month}") 

currenttime_func()


#practice 2 

def days_active(days_remaning):
    today = datetime.now()
    remaing_time = timedelta(days=days_remaning)
    final_remaningtime = today + remaing_time
    print(f"user subscription will end on: {final_remaningtime}")


days_active(8)


