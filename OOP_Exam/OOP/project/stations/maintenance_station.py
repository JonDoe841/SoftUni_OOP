from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    _SALARY = 3000.0

    def __init__(self, name: str):
        super().__init__(name, 3)

    def update_salaries(self, min_value: float):
        for astronaut in self.astronauts:
            if (astronaut.salary <= min_value and
                    astronaut.specialization == "EngineerAstronaut"):
                astronaut.salary += self._SALARY