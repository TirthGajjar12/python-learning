# task one 


class MaxLimitExceeded(Exception):
    pass


class HDFCBank:

    def __init__(self):
        self.__max_transactions = 3
        self.__max_amount = 20000


    def withdraw(self,amount):
        if self.__max_transactions == 0:
            raise MaxLimitExceeded("Limit Exceeded")
        elif amount > self.__max_amount: 
            raise MaxLimitExceeded("Amount Exceeded")
        else:
            self.__max_transactions  -= 1
            self.__max_amount -= amount  
            print(f"Success! Remaining amount limit: {self.__max_amount}")
            print(f"Remaining transactions: {self.__max_transactions}")

class AXISBank:

    def __init__(self):
        self.__max_transactions = 5
        self.__max_amount = 30000


    def withdraw(self,amount):
        if self.__max_transactions == 0:
            raise MaxLimitExceeded("Limit Exceeded")
        elif amount > self.__max_amount: 
            raise MaxLimitExceeded("Amount Exceeded")
        else:
            self.__max_transactions  -= 1
            self.__max_amount -= amount  
            print(f"Success! Remaining amount limit: {self.__max_amount}")
            print(f"Remaining transactions: {self.__max_transactions}")


class Atm():


    def InputAmount(self):

        Bank = input("Enter the bank you want to choose Hdfc or axis: ").lower()

        if Bank == "hdfc":
            current_bank = HDFCBank()
        elif Bank == 'axis':
            current_bank = AXISBank()
        else:
            print("invalid bank entered")
            return

        while True:
            try:
                amount = int(input("Enter the amount you want to withdraw: "))

                current_bank.withdraw(amount)

                for_another_transaction = (input("Do you want to another transaction Yes of No: ")).lower()

                if for_another_transaction == 'no':
                    print("thank you for using our atm!")
                break

            except MaxLimitExceeded as e:
                print(f'transaction faild {e}')


            except ValueError:
                print('please enter a valid number')


my_atm = Atm()
my_atm.InputAmount()

                
#task two Inheritance 


import random
import sys

class BankInfo():

    def __init__(self,fn,ln,gender,address): 
        self.fn = fn
        self.ln = ln
        self.gender = gender
        self.address = address


class BankAccount():

    def __init__(self,amount,object_bank_info):
        self.amount = amount
        self.object_bank_info = object_bank_info
        self.acno = random.randint(1000000000000,9999999999999)

class savings(BankAccount):

        def __init__(self,amount,object_bank_info):

            super().__init__(amount,object_bank_info)

            self.min_amount = 10000
            self.rate = 6

        def calculate_interest(self,months):    

            interest_earned = (self.amount * self.rate * (months / 12)) / 100

            print(f"Interest earned in {months} months will be: ₹{interest_earned}")

class current(BankAccount):

    def __init__(self, amount, object_bank_info):
        super().__init__(amount, object_bank_info)

        self.min_ammount = 5000
        self.rate = None

# 1. REMOVED class Main(): entirely. This code just sits against the left wall!

fn = input("Enter your first name: ")
ln = input("Enter your last name: ")
gender = input("Enter your gender: ")
address = input("Enter your address: ")

user_Info = BankInfo(fn,ln,gender,address)
Account_type = input('Enter the type of account you need (savings/current): ').lower()

# 2. THE LOOP (Only asks for the money)
for i in range(3):
    amount = int(input("Enter the amount you want to add: "))

    if (Account_type == 'current' and amount < 5000) or (Account_type == 'savings' and amount < 10000):
        print(f"Amount too low! Attempt {i+1} of 3.")
    else:
        break # SUCCESS! We break out of the loop and drop down to the code below.

# 3. EVERYTHING BELOW HERE IS OUTSIDE THE LOOP! (Notice it touches the left wall)

# Did they fail 3 times?
if (Account_type == 'current' and amount < 5000) or (Account_type == 'savings' and amount < 10000):
    sys.exit("Too many failed attempts. Goodbye.")  
    
# Build the account based on their choice
if Account_type == 'savings':
    my_account = savings(amount,user_Info)
    months = int(input("Enter the number of the months you want to save for: "))
    my_account.calculate_interest(months)
    
elif Account_type == 'current':
    my_account = current(amount,user_Info)

# Print the final profile
print("\n--- ACCOUNT PROFILE ---")
print(f"Name: {my_account.object_bank_info.fn} {my_account.object_bank_info.ln}")
print(f"Account No: {my_account.acno}") 
# Added your missing amount print statement!
print(f"Amount: ₹{my_account.amount}")   

