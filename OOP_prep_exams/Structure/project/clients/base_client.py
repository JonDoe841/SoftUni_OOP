from abc import ABC, abstractmethod


class BaseClient(ABC):
    def __init__(self, name:str,phone_number:str):
        self.name = name
        self.discount = 0.0
        self.phone_number = phone_number
        self.total_orders = 0
    @property
    def name(self) ->str:
        return self._name
    @name.setter
    def name(self, value:str):
        value = value.strip()
        if len(value) < 2:
            raise ValueError("Name must be at least two characters long!")
        self._name = value

    @property
    def phone_number(self) -> str:
        return self._phone_number
    @phone_number.setter
    def phone_number(self, value: str):
        if not value.isdigit():
            raise ValueError("Phone number can contain only digits!")
        self._phone_number = value


    @abstractmethod
    def update_discount(self):
        pass

    def update_total_orders(self):
        self.total_orders += 1
    def client_details(self):
        return f"Client: {self.name}, Phone number: {self.phone_number}, Orders count: {self.total_orders}, Discount: {round(self.discount)}%"
