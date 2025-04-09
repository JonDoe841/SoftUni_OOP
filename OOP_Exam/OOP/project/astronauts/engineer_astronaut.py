from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):
    _STAMINA = 5
    def __init__(self,id_number: str, salary: float):
        super().__init__(id_number,salary,"EngineerAstronaut", 80)
    def train(self):
        self.stamina = min(self.stamina + self._STAMINA, 100)