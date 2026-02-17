#Method over loading : Not suppored by python 
# Method overridding supports in pythonnnnnnnnnnnnnnnn
#hierrrachial inheritance
class Father:
    Bank_Name = "SBI"  #class Variable 

    def sleep(self):
        return " father is sleeping"

    def work(self):
        return " father is working"


class Child(Father):  # inheriting from parent class
    def sleep(self):
        return "child is sleeping"

    def father_sleep(self):
        return Father.sleep()
       

    def work(self):
        return "child is working"

class Child1(Father): # inheriting from parent class
    def sleep(self):
        return "child1 is sleeping"
    def father_sleep(self):
        return Father.sleep(self)

    def work(self):
        return "child1 is working"
    
    
#-------------------Main Function-----------------------------
def main():
    f = Child1()
    print(f.work())
    print(f.father_sleep())
        
    
if __name__=="__main__":
    main()
