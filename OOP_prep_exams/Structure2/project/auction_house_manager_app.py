from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact

class AuctionHouseManagerApp:
    def __init__(self):
        self.artifacts = []
        self.collectors = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in ["ContemporaryArtifact", "RenaissanceArtifact"]:
            raise ValueError("Unknown artifact type!")
        if any(artifact.name == artifact_name for artifact in self.artifacts):
            raise ValueError(f"{artifact_name} has been already registered!")

        if artifact_type == "ContemporaryArtifact":
            artifact = ContemporaryArtifact(artifact_name,artifact_price,artifact_space)
        else:
            artifact = RenaissanceArtifact(artifact_name, artifact_price, artifact_space)

        self.artifacts.append(artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def get_artifact_by_name(self, artifact_name: str):
        for artifact in self.artifacts:
            if artifact.name == artifact_name:
                return artifact
        return None
    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in ["Museum", "PrivateCollector"]:
            raise ValueError("Unknown collector type!")
        # CHASSSSSSSS
        if any(client.name == collector_name for client in self.collectors):
            raise ValueError(f"{collector_name} has been already registered!")
        if collector_type == "Museum":
            collectors = Museum(collector_name)
        else:
            collectors = PrivateCollector(collector_name)
        self.collectors.append(collectors)
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        client = next((c for c in self.collectors if c.name == collector_name),None)
        artifact = next((a for a in self.artifacts if a.name == artifact_name),None)

        if not client:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")
        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")
        if not client.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact) #bal sam go da raboti
        client.purchased_artifacts.append(artifact)
        client.available_money -= artifact.price
        client.available_space -= artifact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."


    def remove_artifact(self, artifact_name: str):
        artifact_to_remove = next((a for a in self.artifacts if a.name == artifact_name), None)
        if not artifact_to_remove:
            return "No such artifact."
        self.artifacts.remove(artifact_to_remove)
        return f"Removed {artifact_to_remove.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        count = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                count += 1
        return f"{count} collector/s increased their available money."

    def get_auction_report(self):
        total_sold_artifacts = sum(len(c.purchased_artifacts) for c in self.collectors)
        available_artifacts = len(self.artifacts)
        sorted_collectors = sorted(
            self.collectors,
            key=lambda c: (-len(c.purchased_artifacts), c.name))
        report_lines = [
            "**Auction statistics**",
            f"Total number of sold artifacts: {total_sold_artifacts}",
            f"Available artifacts for sale: {available_artifacts}",
            "***"]
        for collector in sorted_collectors:
            report_lines.append(str(collector))

        return "\n".join(report_lines)


















