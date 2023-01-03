from WildFarm.project.animals.animal import Mammal
from WildFarm.project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "Squeak"

    def feed(self, food: (Vegetable, Fruit)):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.weight += food.quantity * 0.10
            self.food_eaten += food.quantity
        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Meat):
        if isinstance(food, Meat):
            self.weight += food.quantity * 0.40
            self.food_eaten += food.quantity
        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "Meow"

    def feed(self, food: (Vegetable, Meat)):
        if isinstance(food, Vegetable) or isinstance(food, Meat):
            self.weight += food.quantity * 0.30
            self.food_eaten += food.quantity
        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Meat):
        if isinstance(food, Meat):
            self.weight += food.quantity * 1.00
            self.food_eaten += food.quantity
        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"

    def __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
