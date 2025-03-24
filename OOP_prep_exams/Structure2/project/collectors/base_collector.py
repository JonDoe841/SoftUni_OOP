from abc import ABC, abstractmethod


class BaseCollector(ABC):
    def __init__(self,name:str,available_money: float,available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts = []

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value):
        # hopefully it works
        value.strip()
        for word in value.split():
            if not word.isalnum():
                raise ValueError("Collector name must contain letters, "
                                 "numbers, and optional white spaces between them!")
        self._name = value

    @property
    def available_money(self) -> float:
        return self._available_money
    @available_money.setter
    def available_money(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self._available_money = value

    @property
    def available_space(self) -> int:
        return self._available_space
    @available_space.setter
    def available_space(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self._available_space = value

    @abstractmethod
    def increase_money(self):
        pass

    def can_purchase(self, artifact_price: float, artifact_space_required: int):
        if self.available_money >= artifact_price:
            if self.available_space >= artifact_space_required:
                return True
        return  False

    def __str__(self):
        sorted_artifacts = sorted(self.purchased_artifacts, key=lambda x: x.name, reverse=True)
        artifacts_str = ", ".join(artifact.name for artifact in sorted_artifacts) if sorted_artifacts else "none"

        return (f"Collector name: {self.name}; "
                f"Money available: {self.available_money:.2f}; "
                f"Space available: {self.available_space}; "
                f"Artifacts: {artifacts_str}")






















































