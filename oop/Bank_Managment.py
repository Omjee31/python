class User:
    Bank_Name = "SBI"  #class Variable 

    def __init__(self, balance, fname, lname):
        self.fname = fname     # indtance 
        self.lname = lname
        self.balance = balance

    @property   # getteer property
    def fullname(self):
        return f"{self.fname} {self.lname}"

    @fullname.setter  # setter property  (funcction name = " ")
    def fullname(self, name):
        parts = name.split()
        self.fname = parts[0]
        self.lname = parts[-1]
    @fullname.deleter   # delete Name 
    def fullname(self):
        print("Delete Name")
        self.fname = None
        self.lname = None
    @property
    def show_balance(self):
        return f"Your Balance in {self.Bank_Name} is {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    @classmethod   # use to change class variable name
    def change_Bank(cls,New_Bank_name):
        cls.Bank_Name = New_Bank_name

    
#-------------------Main Function-----------------------------
def main():
    S1 = User(9000,'Omjee','Singh') # passing Instance to class 
    print(S1.show_balance)  # perform show_balance y using @property
    S1.withdraw(4000)  #perform withdraw Method
    print(S1.show_balance)    # perform show_balance y using @property
    S1.deposit(18000)            #perform deposit Method
    print(S1.show_balance)            # perform show_balance y using @property
    print(S1.fullname)          # performing fullname 
    S1.fullname= "Anup Rajput"   # setting new name by using setter method in class
    print(S1.fname)     # accessing firstname
    print(S1.Bank_Name)  # access Bank name 
    S1.change_Bank("PNB")  # change bank name by performing change method
    print(S1.Bank_Name)
    del S1.fullname     # delete fullname and set first name lastname none

    print(S1.fname)
    print(S1.lname)
        
    
if __name__=="__main__":
    main()
