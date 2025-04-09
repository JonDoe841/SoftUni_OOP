from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self,name: str):
        super().__init__(name,200)
    def can_climb(self):
        if self.strength >= 100:
            return True
        return False
    def climb(self,peak : BasePeak):
        reduce = 20
        if peak.difficulty_level == "Extreme":
            reduce *= 2
            self.strength -= reduce
        else:
            reduce *= 1.5
            self.strength -= reduce
        self.conquered_peaks.append(peak.name)