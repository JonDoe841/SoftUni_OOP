from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    TIME_TO_CATCH = 90
    def __init__(self,name,points):
        super().__init__(name,points,self.TIME_TO_CATCH)
    def fish_details(self):
        return f"{self.__class__.__name__}: {self.name} [Points: {self.points}, Time to Catch: {self.TIME_TO_CATCH} seconds]"