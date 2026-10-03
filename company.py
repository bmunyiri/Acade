# A program to demonstrate the use of classes, objects, methods
# ============================================================

class Company:
    """Represents an employee at a company."""

    def __init__(self, first_name, last_name, age, salary):
        """Initialize employee attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary

    def sal_increment(self, increase_amount):
        """Calculate and apply salary increment from a percentage.
        increase_amount is a fraction, e.g. 0.1 = 10%."""
        if increase_amount > 1.5:  # more than 150% -> flag as error
            print("Error in Salary Increment!")
            return 0
        increment = self.salary * increase_amount
        self.salary += increment
        return increment

    def __str__(self):                       # <-- ADDED
        return (f"{self.first_name} {self.last_name}, "
                f"age {self.age}, salary {self.salary:.2f}")


class Department(Company):
    """A Company employee who also belongs to a department."""

    def __init__(self, first_name, last_name, age, salary, department, colours):
        super().__init__(first_name, last_name, age, salary)
        self.department = department
        self.colours = colours

    def __str__(self):
        return (super().__str__() +
                f", dept: {self.department}, colours: {self.colours}")


# --- Instantiation ---
emp_1 = Department("Michael", "Jackson", 25, 60000,
                   department="accountants", colours="red")
emp_2 = Company("William", "Boxes", 40, 90000)

# --- Selective salary increment ---
emp_1.sal_increment(0.1)   # 10% raise

# --- Output ---
print(emp_1)
print(emp_2)