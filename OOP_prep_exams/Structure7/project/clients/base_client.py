from abc import ABC, abstractmethod


class BaseClient(ABC):
    def __init__(self, name: str, membership_type: str = None):
        self.name = name
        self.points = 0
        if membership_type:  # Only validate if provided
            self.membership_type = membership_type

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in ["Regular", "VIP"]:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float):
        pass

    def apply_discount(self):
        if self.points >= 100:
            discount = 10
            self.points -= 100
        elif 50 <= self.points < 100:
            discount = 5
            self.points -= 50
        else:
            discount = 0

        return discount, self.points