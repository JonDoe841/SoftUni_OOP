from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):
    _SALARY = 5000.0

    def __init__(self, name: str):
        super().__init__(name, 5)

    def update_salaries(self, min_value: float):
        for astronaut in self.astronauts:
            if (astronaut.salary <= min_value and
                    astronaut.specialization == "ScientistAstronaut"):
                astronaut.salary += self._SALARY
