from abc import ABC, abstractmethod


class BasePlant(ABC):
    def __init__(self, name:str, price: float, water_needed: int):
        self.name = name
        self.price = price
        self.water_needed = water_needed
    @property
    def name(self) ->str:
        return self._name
    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Plant name cannot be null or empty!")
        self._name = value
    @property
    def price(self) -> str:
        return self._price
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero!")
        self._price = value
    @property
    def water_needed(self):
        return self._water_needed
    @water_needed.setter
    def water_needed(self, value):
        if not 1 <= value <= 2000:
            raise ValueError("Water needed must be "
                             "between 1 and 2000 ml!")
        self._water_needed = value
    @abstractmethod
    def plant_details(self):
        pass

