from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers = []
        self.peaks = []
    def register_climber(self,climber_type: str, climber_name: str):
        if climber_type not in ["ArcticClimber","SummitClimber"]:
            return f"{climber_type} doesn't exist in our register."
        if any(c.name == climber_name for c in self.climbers):
            return f"{climber_name} has been already registered."
        if climber_type == "ArcticClimber":
            climber = ArcticClimber(climber_name)
        else:
            climber = SummitClimber(climber_name)
        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self,peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in ["ArcticPeak","SummitPeak"]:
            return f"{peak_type} is an unknown type of peak."
        if peak_type == "ArcticPeak":
            peak = ArcticPeak(peak_name,peak_elevation)
        else:
            peak = SummitPeak(peak_name,peak_elevation)
        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."
    def check_gear(self,climber_name: str, peak_name: str, gear: List[str]):
        recommended_gear = []
        for p in self.peaks:
            recommended_gear.append(p.get_recommended_gear())
        if recommended_gear == gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        climber = next((c for c in self.climbers if climber_name == c.name),None)
        climber.is_prepared = False
        missing_gear = recommended_gear + p.get_recommended_gear()
        missing_gear = [item for sublist in missing_gear for item in (sublist if isinstance(sublist, list) else [sublist])]
        missing_gear = set(missing_gear)
        result = f"{climber_name} is not prepared to climb {peak_name}. Missing gear:"
        result += ", ".join(sorted(missing_gear))
        return result
    def perform_climbing(self, climber_name: str, peak_name: str):
        if not any(c.name == climber_name for c in self.climbers):
            return f"Climber {climber_name} is not registered yet."
        if not any(p.name == peak_name for p in self.peaks):
            return f"Peak {peak_name} is not part of the wish list."
        climber = next((c for c in self.climbers if c.name == climber_name),None)
        peak = next((p for p in self.peaks if p.name == peak_name),None)
        if climber.can_climb:
            if climber.is_prepared:
                return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
            return f"{climber_name} will need to be better prepared next time."
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."
    def get_statistics(self):
        climber = [c for c in self.climbers if c.conquered_peaks]
        result = f"Total climbed peaks: {sum(len(c.conquered_peaks) for c in climber)}"
        result +=  "**Climber's statistics:**"
        for c in sorted(climber, key=lambda x: x.name):
            result += f"{c.name}: {', '.join(sorted(c.conquered_peaks))}\n"
        return result