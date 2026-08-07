#exception handling 

#exercise 1


try:

    runs = int(input("Enter how many runs scored: "))

    balls = int(input("Enter how many balls were played: "))

    run_rate = runs/balls * 100
    print(f"This players runrate is {run_rate}")

except  ValueError:
    print("Please enter valid number")


except   ZeroDivisionError:
    print("please enter number more than zero")

#exercise 2

grid = {"p1": "Verstappen", "p2": "Norris", "p3": "Leclerc"}

try: 
   Enter_grid = input("Enter the postion you want to view: ")

   print(grid[Enter_grid])

except KeyError:   
    print('Invaild grid postions')

finally:
    print('Grid search closed')    

#exercise 3

class InvalidFileNameError(Exception):
    pass


try:
    check = input('Enter the file name you want to submit: ')
    if 'homeid' not in check:
        raise InvalidFileNameError('File name is wrong please edit the file name! ')
except InvalidFileNameError as e:        
    print(e)
    

