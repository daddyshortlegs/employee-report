class EmployeeReport:
    def __init__(self, employees):
        self.employees = employees

    def generate(self):
        return ["Mike"]


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age