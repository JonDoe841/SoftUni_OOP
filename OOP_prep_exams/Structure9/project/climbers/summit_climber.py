from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    def __init__(self,name:str):
        super().__init__(name,150)

    def can_climb(self):
        if self.strength >= 75:
            return True
        return False

    def climb(self, peak: BasePeak):
        reduce = 30
        if peak.difficulty_level == "Advanced":
            reduce *= 1.3
            self.strength -= reduce
        else:
            reduce *= 2.5
            self.strength -= reduce
        self.conquered_peaks.append(peak.name)
