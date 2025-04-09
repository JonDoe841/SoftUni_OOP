from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    def __init__(self):
        self.influencers = []
        self.campaigns = []
    def register_influencer(self,influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in ["PremiumInfluencer","StandardInfluencer"]:
            return f"{influencer_type} is not an allowed influencer type."
        if any(i.username == username for i in self.influencers):
            return f"{username} is already registered."
        if influencer_type == "PremiumInfluencer":
            info =PremiumInfluencer(username,followers,engagement_rate)
        else:
            info = StandardInfluencer(username,followers,engagement_rate)
        self.influencers.append(info)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self,campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in ["HighBudgetCampaign","LowBudgetCampaign"]:
            return f"{campaign_type} is not a valid campaign type."
        if any (c.campaign_id == campaign_id for c in self.campaigns):
            return f"Campaign ID {campaign_id} has already been created."
        if campaign_type == "HighBudgetCampaign":
            info = HighBudgetCampaign(campaign_id,brand,required_engagement)
        else:
            info = LowBudgetCampaign(campaign_id,brand,required_engagement)
        self.campaigns.append(info)



    def participate_in_campaign(self,influencer_username: str, campaign_id: int):
        pass
    def calculate_total_reached_followers(self):
        pass
    def influencer_campaign_report(self,username: str):
        pass
    def campaign_statistics(self):
        pass