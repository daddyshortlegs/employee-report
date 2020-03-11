class EmployeeReport:
    def __init__(self, employees):
        self.employees = employees

    def generate(self):
        old_enough = list(filter(lambda employee: (employee.age > 18), self.employees))
        return sorted(list(map(lambda employee: employee.name.upper(), old_enough)), reverse=True)


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age