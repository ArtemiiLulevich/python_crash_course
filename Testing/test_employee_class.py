import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):
    """Simple test class"""

    def test_give_default_raise(self):
        employee = Employee('Artemii', 'Lulevich', 50000)
        employee.give_raise()
        self.assertEqual(employee.salary, 55000)

    def test_give_custom_raise(self):
        employee = Employee('Artemii', 'Lulevich', 50000)
        employee.give_raise(50000)
        self.assertEqual(employee.salary, 100000)


if __name__ == '__main__':
    unittest.main()
