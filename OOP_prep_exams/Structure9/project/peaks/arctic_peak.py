from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    def __init__(self,name: str, elevation: int):
        super().__init__(name,elevation)
    def get_recommended_gear(self):
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
    def calculate_difficulty_level(self):
        difficulty = self.elevation
        if difficulty > 3000:
            return "Extreme"
        return "Advanced"