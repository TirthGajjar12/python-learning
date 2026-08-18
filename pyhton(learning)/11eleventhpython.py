#task 1 data cleaner 

laptops = [
    {"brand": "Dell", "price": 800, "in_stock": True},
    {"brand": "MacBook", "price": 1200, "in_stock": False},
    {"brand": "Lenovo", "price": 600, "in_stock": True},
    {"brand": "HP", "price": 500, "in_stock": False}
]


new_list = list(filter(lambda x : x["in_stock"]  == True,laptops))

final_list = list(map(lambda x : x["brand"] , new_list ))

print(final_list)


#task 2 the security log basecaly add names of visitor in the society

while True:
        visitor_name = input("Enter visitor name or Type quit to stop: ").lower()

        if visitor_name == "quit":
            break
        else:
            with open("log.txt",'a') as log_file:
                    log_file.write(f"{visitor_name}\n")

print('log saved')

#task 3 this is an video game challange where players can drive different types if vehicles 

class Vehicles:

    def __init__(self,brand,color):

            self.brand = brand
            self.color = color
            self.__fuel_level = 100

    def drive(self):

        if self.__fuel_level > 0:

            print("Driving...")

            self.__fuel_level -= 10

        else:
            print("Out of gas!")

    def refuel(self):

        self.__fuel_level = 100



class ElectricCar(Vehicles):

    def recharge(self):

        print("Battery fully charged")


car = Vehicles('toyota','red')
car.drive()
car.drive()
car.drive()
car.refuel()

tesla = ElectricCar('tesla','white')
car.drive()
car.drive()
car.drive()
tesla.recharge()

