from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int) -> str:
        if waiter_type not in ["FullTimeWaiter", "HalfTimeWaiter"]:
            return f"{waiter_type} is not a recognized waiter type."

        if any(w.name == waiter_name for w in self.waiters):
            return f"{waiter_name} is already on the staff."

        try:
            if waiter_type == "FullTimeWaiter":
                waiter = FullTimeWaiter(waiter_name, hours_worked)
            else:
                waiter = HalfTimeWaiter(waiter_name, hours_worked)

            self.waiters.append(waiter)
            return f"{waiter_name} is successfully hired as a {waiter_type}."

        except ValueError as e:
            return str(e)

    def admit_client(self, client_type: str, client_name: str) -> str:
        if client_type not in ["RegularClient", "VIPClient"]:
            return f"{client_type} is not a recognized client type."

        if any(c.name == client_name for c in self.clients):
            return f"{client_name} is already a client."

        try:
            if client_type == "RegularClient":
                client = RegularClient(client_name)
            else:
                client = VIPClient(client_name)

            self.clients.append(client)
            return f"{client_name} is successfully admitted as a {client_type}."

        except ValueError as e:
            return str(e)

    def process_shifts(self, waiter_name: str) -> str:
        waiter = next((w for w in self.waiters if w.name == waiter_name), None)
        return waiter.report_shift() if waiter else f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float) -> str:
        client = next((c for c in self.clients if c.name == client_name), None)
        if not client:
            return f"{client_name} is not a registered client."

        points = client.earning_points(order_amount)
        return f"{client_name} earned {points} points from the order."

    def apply_discount_to_client(self, client_name: str) -> str:
        client = next((c for c in self.clients if c.name == client_name), None)
        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount}% discount. Remaining points {remaining_points}"

    def generate_report(self) -> str:
        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)
        total_client_points = sum(client.points for client in self.clients)
        clients_count = len(self.clients)

        report_lines = [
            "$$ Monthly Report $$",
            f"Total Earnings: ${total_earnings:.2f}",
            f"Total Clients Unused Points: {total_client_points}",
            f"Total Clients Count: {clients_count}",
            "** Waiter Details **"
        ]

        sorted_waiters = sorted(self.waiters,
                                key=lambda w: w.calculate_earnings(),
                                reverse=True)

        for waiter in sorted_waiters:
            report_lines.append(f"Name: {waiter.name}, Total earnings: ${waiter.calculate_earnings():.2f}")

        return "\n".join(report_lines)