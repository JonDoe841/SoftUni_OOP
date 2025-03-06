class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25
    def __init__(self, fuel:float, horse_power: int, ):
        self.horse_power = horse_power
        self.fuel = fuel
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int):
        fuel_consumed = kilometers * self.fuel_consumption
        if self.fuel >= fuel_consumed:
            self.fuel -= fuel_consumed