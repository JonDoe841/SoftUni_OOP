from abc import ABC,abstractmethod

from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):
    def __init__(self,name: str, strength: float):
        self.name = name
        self.strength = strength
        self.is_prepared = True
        self.conquered_peaks = []
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value
    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value
    @abstractmethod
    def can_climb(self):
        pass
    @abstractmethod
    def climb(self,peak : BasePeak):
        pass
    def rest(self):
        self.strength += 15
    def __str__(self):
        result = f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: {self.strength} *"
        result += f"Conquered peaks: " + ", ".join(p for p in self.conquered_peaks) + " ///"
        return result