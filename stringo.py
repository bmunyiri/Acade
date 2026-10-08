class Employees:
    """A class to represent Employees"""
    def __init__(self,first_name,last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    def morning(self):
        """empoyee prep"""
        return f"Good morning {self.first_name}, today is the best day to Shine"

    def __str__(self):
        return f"{self.first_name},{self.last_name}, {self.age}, {self.salary}"


emp1 = Employees("John","smith",30,50000)
print(emp1)
print(emp1.age)
print(emp1.morning())