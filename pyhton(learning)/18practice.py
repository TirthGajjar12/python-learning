from abc import ABC,abstractmethod


class bank(ABC):
    def __init__(self,owner,balance=0):
      self.owner = owner
      self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self,amount):
        self._balance += amount 

    @abstractmethod
    def calculatemethod():
        pass


class savings_acount(bank):
    def calculatemethod(self):
        return self._balance * 0.05

class current_account(bank):
    def calculatemethod(self):
        return 0

account = savings_acount("tirth",5000)
account1 = current_account("daksh",5000)

print(account.owner,account.calculatemethod())
print(account1.owner,account1.calculatemethod())
print(account._balance)