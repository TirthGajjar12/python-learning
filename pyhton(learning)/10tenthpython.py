class Employee():

    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary

    
    def get_salary(self):
        return self.base_salary



class Developer(Employee):

    def __init__(self,name,base_salary):

        super().__init__(name,base_salary)

    def calculate_bonus(self):
         
        bonus = self.get_salary() * 0.10 

        return bonus
class Manager(Employee):

    def __init__(self,name,base_salary):

        super().__init__(name,base_salary)

    def calculate_bonus(self):
         
        bonus = self.get_salary() * 0.20 

        return bonus

dev_Tirth = Developer("Tirth",50000)
Manager_abhi = Manager("yash",80000)

print(f"here is the developer name : - {dev_Tirth.name} and here is their bonus:- {dev_Tirth.calculate_bonus()}")
print(f"here is the developer name : - {Manager_abhi.name} and here is their bonus:- {Manager_abhi.calculate_bonus()}")


#practice for replace map and filter 

messy_salaries = ["$40,000", "$65,000", "$90,000", "$45,000"]

for salary_string in messy_salaries:


    clean_salaries = int(salary_string.replace("$","").replace(",",""))

    if clean_salaries < 50000:
        print(f"high salarys found {clean_salaries}")


#task 1 for class
class Thermostat():

    def __init__(self,current_temp,target_temp):
        self.current_temp = current_temp
        self.target_temp = target_temp


    def increase_temp(self):

        self.current_temp += 1
        print(self.current_temp)

    def decrease_temp(self):

        self.current_temp -= 1
            


    def status(self):

        if (self.current_temp < self.target_temp):

            print("Heater needs to turn on")

        elif (self.current_temp > self.target_temp):    

            print("Ac needs to turn on")

        else:

            print("Temperature is perfact")   

my_house = Thermostat(70,75)

my_house.status()
my_house.increase_temp()
my_house.increase_temp()
my_house.increase_temp()
my_house.increase_temp()
my_house.increase_temp()
my_house.increase_temp()
my_house.status()


#task file operations how to copy one file to another 

with open('8eightpython.py','r') as python_file ,  open('copyFile.py',"w") as copy_file :

        file_content = python_file.read()

        copy_file.write(file_content)


