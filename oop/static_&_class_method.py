"""
Student Management System
Demonstrates:
- Class & Instance variables
- Inheritance
- Class method
- Static method
"""

class Student:
    """Main Parent Class"""

    school_name = "OCS"   # Class variable

    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    @classmethod
    def change_school_name(cls, new_name):
        """Class method to update school name"""
        cls.school_name = new_name


class Details(Student):
    """Child Class inheriting Student"""

    def __init__(self, names, ages, roll_numbers, marks):
        super().__init__(None, None, None)
        self.names = names
        self.ages = ages
        self.roll_numbers = roll_numbers
        self.marks = marks

    def show_result(self):
        """Display students result"""
        print(f"\n{self.school_name} Result:\n")
        for name, mark in zip(self.names, self.marks):
            print(f"{name} : {mark}")

    @staticmethod
    def total_marks(marks):
        """Static method to calculate total marks"""
        return sum(marks)


if __name__ == "__main__":

    names = ['A', 'B', 'C', 'D', 'E', 'F']
    ages = [16, 18, 19, 14, 15, 20]
    roll_numbers = [1001, 1002, 1003, 1004, 1005, 1006]
    marks = [45, 67, 44, 23, 58, 90]   # fixed length

    s1 = Student('Omjee Singh', 16, 1001)
    s2 = Details(names, ages, roll_numbers, marks)

    s2.show_result()

    print("\nTotal Marks:", s2.total_marks(marks))

    print("\nBefore changing school name:", s1.school_name)
    Student.change_school_name("ABR")
    print("After changing school name:", s1.school_name)
