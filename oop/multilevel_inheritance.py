class GrandFather:  #parent

    def house(self):
        return"Big House"

class Father(GrandFather): #child1 inheriting from parent
    def car(self):
        return "Car "
class Son(Father):  # child 2 inheriting from his parents 
    def bike(self):
        self.f = Father.car(self)
        self.g = GrandFather.house(self)
        return f"bike {self.f} {self.g}"

s = Son()
print(s.bike())
