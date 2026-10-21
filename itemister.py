class Item:
    _all_items = []  # class attribute — shared by every instance

    """constructor for items in shop"""
    def __init__(self, name,price:float,quantity:int):

        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("quantity cannot be negative")
        self.name = name
        self.price = price
        self.quantity = quantity
        Item._all_items.append(self)

    def __str__(self) -> str:
        return f"Item({self.name}, price={self.price}, quantity={self.quantity})"

    # → "Item(Nokia, price=3000, quantity=5)"

    def __repr__(self):
        return f"Items(name={self.name!r}, price={self.price}, quantity={self.quantity})"

    def discounted_price(self):
        return self.price * 0.8


    @classmethod
    def from_string(cls, item_string):
        name,price,quantity = item_string.split(",")
        return cls(name, float(price), int(quantity))

    @classmethod
    def count(cls):
        """How many items exist in total?"""
        return len(cls._all_items)

    @classmethod
    def all_names(cls):
        """List the names of every item ever created."""
        return [item.name for item in cls._all_items]

    @classmethod
    def find_by_name(cls, name):
        """Look up an item by name."""
        for item in cls._all_items:
            if item.name == name:
                return item
        return None

class Phone(Item):
    """subclass for phones"""
    def __init__(self,name,price:float,quantity:int):
        super().__init__(name, price, quantity)
        self.battery_life = 2

    def __str__(self) -> str:
        return f"Phone({self.name}, price={self.price}, quantity={self.quantity})"

    def __repr__(self):
        return f"Phone(name={self.name!r}, price={self.price}, quantity={self.quantity})"

print("From the Phone class")
phone_1 = Phone("xiomi",7000,10 )
phone_1.battery_life = 5
print(phone_1)
print(phone_1.battery_life)
print("=======================================")

print("From the Item class item 1 discounted price")
item_1 = Item("nokia",3000,5)
print(item_1.name)
print(item_1.discounted_price())
print("=======================================")

print("From the Item class item 2")
item_2 =Item.from_string("iphone,2000,3")
print(item_2.name)
print("=======================================")

print("From the Item class")
print(Item.count())              # 2
print(Item.all_names())          # ['Nokia', 'iPhone']
print(Item.find_by_name("nokia"))# Item(name='Nokia', price=3000, quantity=5)
print("=======================================")