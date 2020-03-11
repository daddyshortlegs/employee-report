class EmployeeReport:
    def __init__(self, employees):
        self.employees = employees

    def generate(self):
        if len(self.employees) == 0:
            return []

        old_enough = list(filter(lambda employee: (employee.age > 18), self.employees))
        return list(map(lambda employee: (employee.name), old_enough))


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age