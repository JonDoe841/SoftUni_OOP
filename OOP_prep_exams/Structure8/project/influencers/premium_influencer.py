from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    PAYMENT = 0.85
    def __init__(self,username: str, followers: int, engagement_rate: float):
        super().__init__(username,followers,engagement_rate)
    def calculate_payment(self,campaign: BaseCampaign):
        payment = campaign.budget * self.PAYMENT
        return payment
    def reached_followers(self,campaign_type: str):
        pass