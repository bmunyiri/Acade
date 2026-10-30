class Vitu:
    """A class for stock control"""
    all = []

    def __init__(self, name:str, price:float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

        Vitu.all.append(self)

    def __str__(self):
        return f"'Name'{self.name},'Price' {self.price},'Quantity'{self.quantity}"

    def __repr__(self):
            return f"'Name'{self.name},'Price' {self.price},'Quantity'{self.quantity}"
    @classmethod
    def instantiate_from_csv(cls):
        import csv
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Vitu(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )


Vitu.instantiate_from_csv()
print(Vitu.all)

for instance in Vitu.all:
    print(instance.name)