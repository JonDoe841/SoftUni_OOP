from abc import ABC,abstractmethod


class BaseCampaign(ABC):
    def __init__(self,campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.brand = brand
        self.budget = budget
        self.campaign_id = campaign_id
        self.required_engagement = required_engagement
        self.approved_influencers = []
        self.campaign_id_list = []

    @property
    def campaign_id(self):
        return self.__campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        if value < 0:
            raise ValueError("Campaign ID must be a positive integer greater than zero.")
        self.__campaign_id = value
        if value in self.campaign_id_list:
            raise ValueError(f"Campaign with ID {value} already exists. Campaign IDs must be unique.")
        self.campaign_id_list.append(value)

    @abstractmethod
    def check_eligibility(self, engagement_rate: float):
        pass