class Item:
    def __init__(self, name: str, price: float, quantity=0):
        """Initialize an Item with name, price, and quantity."""
        # instantiate variables
        self.name = name
        self.price = price
        self.quantity = quantity

        # assert numeric values are non-negative
        assert self.price >= 0, f"Price {self.price} must be >= 0"
        assert self.quantity >= 0, f"Quantity {self.quantity} must be >= 0"

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.name}, {self.price}, {self.quantity}"

    def item_stock_value(self):
        """Return the total stock value (price * quantity)."""
        return self.price * self.quantity


item_1 = Item("nokia", 300, 5)
print(item_1)                            # nokia, 300, 5
print(f"\n{item_1.item_stock_value()}")  # 1500