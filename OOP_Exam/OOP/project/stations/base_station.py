from abc import ABC, abstractmethod


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not all(c.isalnum() or c == '-' for c in value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self):
        total = sum(a.salary for a in self.astronauts)
        return f"{total:.2f}"

    def status(self):
        astronaut_ids = sorted(a.id_number for a in self.astronauts)
        astronauts_str = ' #'.join(astronaut_ids) if astronaut_ids else "N/A"
        return (f"Station name: {self.name}; "
                f"Astronauts: {astronauts_str}; "
                f"Total salaries: {self.calculate_total_salaries()}")

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass