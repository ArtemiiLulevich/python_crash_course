class Employee:
    """Simple Employee class"""
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def give_raise(self, increase=5000):
        self.salary += increase

