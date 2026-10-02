class Coffee:
    """initialize Coffee class """

    def __init__(self, roast_level, blend_name):
        if blend_name not in COFFEE_ROASTS[roast_level]:
            raise ValueError(f"{blend_name} is not a {roast_level} roast")
        self.roast_level = roast_level
        self.blend_name = blend_name

    def __str__(self):
        return f"Coffee({self.roast_level}: {self.blend_name})"


COFFEE_ROASTS = {
    "light": ["Light City", "Half City", "Cinnamon", "New England"],
    "medium": ["City", "American", "Breakfast", "Medium"],
    "medium_dark": ["Full City", "After Dinner", "Vienna", "Continental"],
    "dark": ["French", "Italian", "Espresso", "Spanish", "High"],
    "specialty": ["Blonde", "Decaf", "Omni", "Filter"]
}

import random
level = random.choice(list(COFFEE_ROASTS.keys()))
blend = random.choice(COFFEE_ROASTS[level])   # picks one from the list

morning_cup = Coffee(level, blend)

message = f"In the morning I like {morning_cup}"
print(message)
