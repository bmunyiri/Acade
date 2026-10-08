class Population:

    def __init__(self, china,germany,kenya,india):
        self.china = china
        self.germany = germany
        self.kenya = kenya
        self.india = india

    def __str__(self):
        return f"China: {self.china}, Germany: {self.germany}, Kenya: {self.kenya}, India: {self.india}"


    def population_update(self, country, amount):
        # Check if the country is a valid attribute
        if hasattr(self, country):
            setattr(self, country, amount)
        else:
            print(f"Unknown country: {country}")

    # Create an instance
pop = Population(china=120000000, germany=70000, kenya=249000, india=22000000)
print(pop)

# Update Kenya's population
pop.population_update("kenya", 3339000)
print(pop)

