from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    BUDGET = 2500.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)
        self.campaign_id_list = []
    def check_eligibility(self, engagement_rate: float):
        checker = engagement_rate * 0.9
        if self.required_engagement <= checker:
            return True
        return False