from pygments.styles import default


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(  f"{self.restaurant_name},{self.cuisine_type}")

    def __str__(self):
        return f"{self.restaurant_name}, {self.cuisine_type}"

print("#================================================================")

from dataclasses import dataclass, field

@dataclass
class Employee:
    first_name: str
    last_name: str
    age: int
    salary: float
    all_names: list = field(default_factory=list, init=False)   # ← the `=` matters!

    def __post_init__(self):
        self.all_names = [self.first_name, self.last_name]
        print(f"{self.first_name} was created")


emp1 = Employee("John", "Smith", 30, 50000)
print(emp1)

print("#================================================================")
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Employee:
    first_name: str
    last_name: str
    age: int
    salary: float

    registry: ClassVar[list["Employee"]] = []

    def __post_init__(self):
        if self.salary < 0:
            raise ValueError("Salary cannot be negative")
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        type(self).registry.append(self)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # ---------- registry API ----------

    @classmethod
    def all(cls) -> list["Employee"]:
        return list(cls.registry)

    @classmethod
    def count(cls) -> int:
        return len(cls.registry)

    @classmethod
    def find_by_last_name(cls, last_name: str) -> list["Employee"]:
        return [e for e in cls.registry if e.last_name.lower() == last_name.lower()]

    @classmethod
    def with_salary_above(cls, amount: float) -> list["Employee"]:
        return [e for e in cls.registry if e.salary > amount]

    @classmethod
    def average_salary(cls) -> float:
        return sum(e.salary for e in cls.registry) / len(cls.registry) if cls.registry else 0.0

    @classmethod
    def clear_registry(cls) -> None:
        cls.registry.clear()


# ---------- usage ----------

if __name__ == "__main__":
    john = Employee("John", "Smith", 30, 50000)
    mary = Employee("Mary", "Wilson", 20, 35000)
    alex = Employee("Alex", "Smith", 40, 80000)

    print("All employees:")
    for e in Employee.all():
        print(f" - {e.full_name}")

    print(f"\nTotal: {Employee.count()}")
    print(f"Average salary: {Employee.average_salary():,.2f}")

    print("\nEmployees over 40k:")
    for e in Employee.with_salary_above(40_000):
        print(f" - {e.full_name} ({e.salary:,})")


