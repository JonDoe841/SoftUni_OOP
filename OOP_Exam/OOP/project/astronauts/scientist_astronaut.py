from project.astronauts.base_astronaut import BaseAstronaut


class ScientistAstronaut(BaseAstronaut):
    _STAMINA = 3
    def __init__(self,id_number: str, salary: float):
        super().__init__(id_number,salary,"ScientistAstronaut",70)
    def train(self):
        self.stamina = min(self.stamina + self._STAMINA, 100)