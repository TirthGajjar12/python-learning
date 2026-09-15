class Invaild_Limit_OrBalance(Exception):
    "this used for either the trasnsaction limit reached or insufficient balance "

class Bank:
    def withdraw(self,amount):
        if self._transactions_count  >=  self._max_transactions or self._max_amount < amount:
                raise Invaild_Limit_OrBalance("the trasnsaction limit reached or insufficient balance in your account")

        else:
            self._transactions_count += 1
            self._max_amount =  self._max_amount - amount
            print("successful transaction")
            print(f"{self._transactions_count}")
            print(f"{self._max_amount}")


class HDFCBank(Bank):
    def __init__(self):
        self._max_transactions = 3
        self._max_amount = 20000
        self._transactions_count = 0


class AXISBank(Bank):
    def __init__(self):
        self._max_transactions = 5
        self._max_amount = 30000
        self._transactions_count = 0




class ATM:
    def inputAmount(self):
        select_bank = int(input("Enter the bank you want to select 1 for HDFC and 2 for AXIS: "))

        if select_bank == 1:
            bank = HDFCBank()
        elif select_bank == 2:
            bank = AXISBank()
        else:
            print("Invalid choice. Select from the given options.")
            return

        while True:
            amount = int(input("Enter the amount to withdraw..."))
            try:
                bank.withdraw(amount)
            except Invaild_Limit_OrBalance as error:
                print(error)

            for_another = input("Do you want another transaction? yes or no (Yes/No): ").strip().lower()
            if for_another == "yes":
                continue
            elif for_another == "no":
                break
            else:
                print("Enter something valid")
                continue     

atm = ATM()
atm.inputAmount()