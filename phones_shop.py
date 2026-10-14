import csv


class Item:
    discount = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        """Initialize an Item with name, price, and quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity

        assert self.price >= 0, f"Price {self.price} must be >= 0"
        assert self.quantity >= 0, f"Quantity {self.quantity} must be >= 0"

        Item.all.append(self)

    def apply_discount(self):
        return self.discount * self.price

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}, {self.price}, {self.quantity}"

    def item_stock_value(self):
        return self.price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=int(item.get("price")),
                quantity=int(item.get("quantity")),
            )


Item.instantiate_from_csv()
print(Item.all)


#print(item1)                            # phone, 100, 1
#print(f"\n{item1.item_stock_value()}")  # 100

#print(item1.apply_discount())


#print(Item.all)              # raw list via __repr__

#print()                      # blank line

#for item in Item.all:        # one per line via __str__
 #   print(item)