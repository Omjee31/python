# Polymorphism using common method name

class Car:
    def move(self):
        print("Car drives on road")

class Boat:
    def move(self):
        print("Boat sails on water")

class Plane:
    def move(self):
        print("Plane flies in sky")

# Polymorphism in action
vehicles = [Car(), Boat(), Plane()]

for v in vehicles:
    v.move()   # same method → different output
