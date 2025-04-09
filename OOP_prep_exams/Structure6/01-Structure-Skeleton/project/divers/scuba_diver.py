from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXY = 540
    def __init__(self,name):
        super().__init__(name,self.INITIAL_OXY)
        #self.catch = []
    def miss(self,time_to_catch):
        oxygen_to_decrease = round(time_to_catch * 0.6)

        # Reduce oxygen level but ensure it doesn't fall below 0
        new_oxygen_level = self.oxygen_level - oxygen_to_decrease
        if new_oxygen_level < 0:
            self.oxygen_level = 0  # Set to 0 if it's negative
        else:
            self.oxygen_level = new_oxygen_level
    def renew_oxy(self):
        self.INITIAL_OXY = 540
        self.oxygen_level = self.INITIAL_OXY