from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    def __init__(self,name: str, elevation: int):
        super().__init__(name,elevation)
    def get_recommended_gear(self):
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
    def calculate_difficulty_level(self):
        #TODO check
        difficulty = self.elevation
        if difficulty > 2500:
            return "Extreme"
        return "Advanced"