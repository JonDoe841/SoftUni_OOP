from typing import List, Type

from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_coefficient(self) -> float:
        return 0.25

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"

class Hen(Bird):
    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat,Vegetable,Fruit,Seed]

    @property
    def weight_coefficient(self) -> float:
        return 0.35
    @staticmethod
    def make_sound() -> str:
        return "Cluck"

