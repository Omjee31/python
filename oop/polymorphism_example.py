# Polymorphism using method overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):  # same method name
        print("Dog barks")

class Cat(Animal):
    def sound(self):  # same method name
        print("Cat meows")

# Creating objects
a = Animal()
d = Dog()
c = Cat()

# Same method name → different behavior (Polymorphism)
a.sound()
d.sound()
c.sound()
