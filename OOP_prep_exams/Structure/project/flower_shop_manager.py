from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant
from project.clients.regular_client import RegularClient
from project.clients.business_client import BusinessClient
class FlowerShopManager:
    def __init__(self):
        self.income = 0.0
        self.plants = []
        self.clients = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int,
                  plant_extra_data: str):
        if plant_type not in ["Flower", "LeafPlant"]:
            raise ValueError("Unknown plant type!")

        if plant_type == "Flower":
            plant = Flower(plant_name, plant_price, plant_water_needed, plant_extra_data)
        else:
            plant = LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data)

        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in ["RegularClient", "BusinessClient"]:
            raise ValueError("Unknown client type!")

        if any(client.phone_number == client_phone_number for client in self.clients):
            raise ValueError("This phone number has been used!")

        if client_type == "RegularClient":
            client = RegularClient(client_name, client_phone_number)
        else:
            client = BusinessClient(client_name, client_phone_number)

        self.clients.append(client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self,client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if not client:
            raise ValueError("Client not found!")

        matching_plants = [p for p in self.plants if p.name == plant_name]
        if not matching_plants:
            raise ValueError("Plants not found!")

        if len(matching_plants) < plant_quantity:
            return "Not enough plant quantity."

        plant_price = matching_plants[0].price if matching_plants else 0

        for _ in range(plant_quantity):
            self.plants.remove(matching_plants.pop(0))


        order_amount = plant_price * plant_quantity * (1 - client.discount / 100)
        self.income += order_amount

        client.update_total_orders()
        client.update_discount()

        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_clients(self):
        removed_clients = [client for client in self.clients if client.total_orders == 0]
        self.clients = [client for client in self.clients if client.total_orders > 0]
        return f"{len(removed_clients)} client/s removed."
    #possibly broken
    def remove_plant(self, plant_name: str):

        plant_to_remove = next((plant for plant in self.plants if plant.name == plant_name), None)
        if not plant_to_remove:
            return "No such plant name."
        self.plants.remove(plant_to_remove)


        return f"Removed {plant_to_remove.plant_details()}"

    def shop_report(self):
        unsold_plants = {}
        for plant in self.plants:
            if plant.name not in unsold_plants:
                unsold_plants[plant.name] = 1
            else:
                unsold_plants[plant.name] += 1

        sorted_unsold_plants = sorted(unsold_plants.items(), key=lambda x: (-x[1], x[0]))
        sorted_clients = sorted(self.clients, key=lambda x: (-x.total_orders, x.phone_number))

        total_orders = sum(client.total_orders for client in self.clients)
        num_of_clients = len(self.clients)
        unsold_plants_count = len(self.plants)

        report = f"~Flower Shop Report~\n"
        report += f"Income: {self.income:.2f}\n"
        report += f"Count of orders: {total_orders}\n"
        report += f"~~Unsold plants: {unsold_plants_count}~~\n"

        for plant_name, count in sorted_unsold_plants:
            report += f"{plant_name}: {count}\n"

        report += f"~~Clients number: {num_of_clients}~~\n"

        for client in sorted_clients:
            report += f"{client.client_details()}\n"

        return report


















































