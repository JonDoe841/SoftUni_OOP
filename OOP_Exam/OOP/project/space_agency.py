from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    def __init__(self):
        self.astronauts = []
        self.stations = []
    def add_astronaut(self,astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        if astronaut_type not in ["EngineerAstronaut", "ScientistAstronaut"]:
            raise ValueError("Invalid astronaut type!")
        if any(a.id_number == astronaut_id_number for a in self.astronauts):
            raise ValueError(f"{astronaut_id_number} has been already added!")
        if astronaut_type == "EngineerAstronaut":
            aus = EngineerAstronaut(astronaut_id_number,astronaut_salary)
        else:
            aus = ScientistAstronaut(astronaut_id_number, astronaut_salary)
        self.astronauts.append(aus)
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self,station_type: str, station_name: str):
        if station_type not in ["ResearchStation","MaintenanceStation"]:
            raise ValueError("Invalid station type!")
        if any(station_name == s.name for s in self.stations):
            raise ValueError(f"{station_name} has been already added!")
        if station_type == "ResearchStation":
            station = ResearchStation(station_name)
        else:
            station = MaintenanceStation(station_name)
        self.stations.append(station)
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self,station_name: str, astronaut_type: str):
        station = next((s for s in self.stations if s.name == station_name), None)
        if not station:
            raise ValueError(f"Station {station_name} does not exist!")
        if station.capacity <= 0:
            return "This station has no available capacity."

        astronaut = next(
            (a for a in self.astronauts
             if a.specialization == astronaut_type),
            None)
        if not astronaut:
            raise ValueError("No available astronauts of the type!")

        self.astronauts.remove(astronaut)
        station.astronauts.append(astronaut)
        station.capacity -= 1
        return f"{astronaut.id_number} was assigned to {station_name}."

    def train_astronauts(self,station: BaseStation, sessions_number: int):
        for _ in range(sessions_number):
            for astronaut in station.astronauts:
                astronaut.train()
        total_stamina = sum(a.stamina for a in station.astronauts)
        return (f"{station.name} astronauts have {total_stamina} total stamina "
                f"after {sessions_number} training session/s.")
    def retire_astronaut(self,station: BaseStation, astronaut_id_number: str):
        astronaut = next(
            (a for a in station.astronauts
             if a.id_number == astronaut_id_number),
            None)

        if not astronaut or astronaut.stamina == 100:
            return "The retirement process was canceled."

        station.astronauts.remove(astronaut)
        station.capacity += 1
        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self,min_value: float):
        for station in self.stations:
            station.update_salaries(min_value)
        result = "*Space Agency Up-to-Date Report*\n"
        available_astronauts_count = len(self.astronauts)
        stations_total_count = len(self.stations)
        total_available_capacity = sum(s.capacity for s in self.stations)

        result += f"Total number of available astronauts: {available_astronauts_count}\n"
        result += f"**Stations count: {stations_total_count}; Total available capacity: {total_available_capacity}**\n"

        sorted_stations = sorted(
            self.stations,
            key=lambda s: (-len(s.astronauts), s.name)
        )

        for station in sorted_stations:
            if station.astronauts:
                astronaut_ids = sorted(a.id_number for a in station.astronauts)
                astronauts_str = " #".join(astronaut_ids)
            else:
                astronauts_str = "N/A"
            total_salaries = sum(a.salary for a in station.astronauts)
            result += f"Station name: {station.name}; Astronauts: {astronauts_str}; Total salaries: {total_salaries:.2f}\n"

        return result.strip()