from abc import ABC, abstractmethod


class BaseArtifact(ABC):
    def __init__(self,name:str, price:float,space_required: int):
        self.name = name
        self.price = price
        self.space_required = space_required

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Artifact name cannot be null or empty!")
        self._name = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Artifact price should be more than 0.0!")
        self._price = value

    @property
    def space_required(self):
        return self._space_required
    @space_required.setter
    def space_required(self, value):
        if not 1 <= value <= 1_000:
            raise ValueError("Space required for the artifact exhibition must be between 1 and 1000!")
        self._space_required = value

    @abstractmethod
    def artifact_information(self):
        pass

    def __str__(self):
        return (f"Artifact name: {self.name}; "
                f"Money available: {self.price:.2f}; "
                f"Space available: {self.space_required};")



















