from project.clients.base_client import BaseClient

class RegularClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, "Regular")  # Directly pass membership type

    def earning_points(self, order_amount: float) -> int:
        points = int(order_amount // 10)
        self.points += points
        return points