from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    BUDGET = 5000.0
    def __init__(self,campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id,brand,self.BUDGET,required_engagement,)
        self.campaign_id_list = []
    def check_eligibility(self, engagement_rate: float):
        checker = engagement_rate * 1.2
        if self.required_engagement <= checker:
            return True
        return False
