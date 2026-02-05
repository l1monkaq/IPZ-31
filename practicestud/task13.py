class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

account = BankAccount("Артем", 5000)
account.deposit(1500)
account.withdraw(2000)

print(f"Власник: {account.owner}")
print(f"Поточний баланс: {account.get_balance()} грн")

try:
    print(account.__balance)
except AttributeError:
    print("Доступ заблоковано: приватний атрибут захищено.")