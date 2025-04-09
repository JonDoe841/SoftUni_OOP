from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers = []
        self.fish_list = []
    def dive_into_competition(self,diver_type: str, diver_name: str):
        if diver_type not in ["FreeDiver","ScubaDiver"]:
            return f"{diver_type} is not allowed in our competition."
        if any(d.name == diver_name for d in self.divers):
            return f"{diver_name} is already a participant."
        if diver_type == "FreeDiver":
            diver = FreeDiver(diver_name)
        else:
            diver = ScubaDiver(diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self,fish_type: str, fish_name: str, points: float):
        if fish_type not in ["PredatoryFish","DeepSeaFish"]:
            return f"{fish_type} is forbidden for chasing in our competition."
        if any(f.name == fish_name for f in self.fish_list):
            return f"{fish_name} is already permitted."
        if fish_type == "PredatoryFish":
            fish = PredatoryFish(fish_name,points)
        else:
            fish = DeepSeaFish(fish_name,points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if not diver:
            return f"{diver_name} is not registered for the competition."
        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.oxygen_level <= 0:
            diver.has_health_issue = True
            return f"{diver_name} will not be allowed to dive, due to health issues."
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level <= 0:
                diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level <= 0:
                    diver.has_health_issue = True
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish)
                if diver.oxygen_level <= 0:
                    diver.has_health_issue = True
                return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            if diver.oxygen_level <= 0:
                diver.has_health_issue = True
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for d in self.divers:
            if d.has_health_issue:
                d.has_health_issue = False
                d.renew_oxy()
                count += 1
        return f"Divers recovered: {count}"


    def diver_catch_report(self, diver_name: str):
        #fish_got = BaseDiver()
        result = f"**{diver_name} Catch Report**"
        #result += f"\n{next(f for f in fish_got.catch)}"
        result += f"\n".join(str(f) for f in self.fish_list if any(f in d.catch for d in self.divers))

        return result

    def competition_statistics(self):
        result = "**Nautical Catch Challenge Statistics**\n"
        result += "\n".join(str(d) for d in self.divers if not d.has_health_issue)
        return result