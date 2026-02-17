#Method over loading : Not suppored by python 
# Method overridding supports in pythonnnnnnnnnnnnnnnn
#Single inheritance
class Father:
    Bank_Name = "SBI"  #class Variable 

    def sleep(self):
        return "father is sleeping"

    def work(self):
        return "father is working"


class Child(Father):
    def sleep(self):
        self.f = Father.sleep(self)  # calling parent class method
        return f"child is sleeping {self.f}"

       

    def work(self):
        return "child is working"

    
    
#-------------------Main Function-----------------------------
def main():
    f = Child()
    print(f.work())
    print(f.sleep())

        
    
if __name__=="__main__":
    main()
