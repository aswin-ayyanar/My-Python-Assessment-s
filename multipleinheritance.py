class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
class Leader:
    def __init__(self, team_size):
        self.team_size = team_size
    def display_leadership_info(self):
        print(f"Team Size: {self.team_size}")
class Manager(Employee, Leader):
    def __init__(self, name, age, employee_id, team_size):
        Employee.__init__(self, name, age, employee_id)
        Leader.__init__(self, team_size)
    def display_info(self):
        super().display_info()
        self.display_leadership_info()
n=input("Enter your Name: ")
a=input("Enter your Age: ")
emp_id=int(input("Enter your emp_ID: "))
ts=int(input("Enter your Team size: "))
manager = Manager(n, a, emp_id, ts)
manager.display_info()