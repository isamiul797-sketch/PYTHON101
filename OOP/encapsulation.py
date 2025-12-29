class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


obj = BankAccount(1000)   
obj.deposit(5000)
obj.withdraw(1500)
print(obj.get_balance())
