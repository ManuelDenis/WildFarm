from WildFarm.project.animals.animal import Bird
from WildFarm.project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
        self.food_eaten = 0

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Meat):
        if isinstance(food, Meat):
            self.weight += food.quantity * 0.25
            self.food_eaten += food.quantity
        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)
        self.food_eaten = 0

    def make_sound(self):
        return "Cluck"

    def feed(self, food: (Vegetable, Fruit, Meat, Seed)):
        if isinstance(food, Vegetable) or isinstance(food, Fruit) or isinstance(food, Meat) or isinstance(food, Seed):
            self.weight += food.quantity * 0.35
            self.food_eaten += food.quantity
        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

