class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance   # private variable (Encapsulation)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.__balance}")


# Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print("Interest added successfully!")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # Method Overriding
    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            # Accessing private variable through public method
            new_balance = self.get_balance() - amount
            # Hacky but safe way using deposit logic
            super().deposit(-amount)
            print(f"Withdrawn with overdraft: {amount}")
        else:
            print("Overdraft limit exceeded!")


# Savings Account
s1 = SavingsAccount("Omjee", 10000, 5)
s1.add_interest()
s1.display_account_info()

print("\n")

# Current Account
c1 = CurrentAccount("Rahul", 5000, 2000)
c1.withdraw(6000)  # within overdraft
c1.display_account_info()
