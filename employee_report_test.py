import unittest

from employee_report import EmployeeReport, Employee

class MyTestCase(unittest.TestCase):
    def test_returns_employees_over_18(self):
        employees = [Employee("Max", 17),
                     Employee("Sepp", 18),
                     Employee("Nina", 15),
                     Employee("Mike", 51)]

        report = EmployeeReport(employees)
        result = report.generate()

        self.assertSequenceEqual(["Mike"], result)

    def test_returns_no_employees(self):
        employees = []

        report = EmployeeReport(employees)
        result = report.generate()

        self.assertSequenceEqual([], result)

    def test_returns_other_employees_over_18(self):
        employees = [Employee("Jon", 43),
                     Employee("Sepp", 18),
                     Employee("Nina", 15),
                     Employee("Mike", 51)]

        report = EmployeeReport(employees)
        result = report.generate()

        self.assertSequenceEqual(["Jon", "Mike"], result)


if __name__ == '__main__':
    unittest.main()
