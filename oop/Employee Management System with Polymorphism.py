class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self._base_salary = base_salary   # protected variable

    def calculate_salary(self):
        return self._base_salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.calculate_salary()}")


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary, bonus):
        super().__init__(name, emp_id, base_salary)
        self.bonus = bonus

    # Method Overriding (Polymorphism)
    def calculate_salary(self):
        return self._base_salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id, 0)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    # Method Overriding
    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


emp1 = FullTimeEmployee("Omjee", 101, 30000, 5000)
emp2 = PartTimeEmployee("Rahul", 102, 80, 500)

employees = [emp1, emp2]

for emp in employees:
    print("-------------")
    emp.display_info()
