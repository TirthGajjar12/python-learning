#encapsulation practice

class batter:

    def __init__(self,name):
            self.name = name
            self.__runs = 0

    def add_runs(self,run_scored):
        if 0 <= run_scored <= 6:
            self.__runs += run_scored
        else:
             print('invalid runs must between 0 to 6')

    def show_status(self):
        print(f"{self.name},{self.__runs}")


a = batter('sachin')
a.show_status()

a.add_runs(4)
a.add_runs(5)
a.show_status()

a.add_runs(10)
a.show_status()


#polymorphism 


class c_plus_plus():
    def speed(self):
        print('its an fast language then python')

    def usage(self):
         print('used in a lot places very diffrent then python')

class java():

    def speed(self):
        print('its not that fast as java it is same as python')

    def usage(self):
         print('it used very lesser now a day but its still used')


def language(self):
     self.speed()
     self.usage() 

c_plus = c_plus_plus()
ja_va = java()


language(c_plus)
language(ja_va)

