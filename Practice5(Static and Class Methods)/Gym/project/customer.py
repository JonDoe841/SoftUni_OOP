class Customer:
    id = 1

    def __init__(self,name: str, address: str, email: str):
        self.name = name
        self.email = email
        self.address = address
        self.id = Customer.id
        self.increment_id()

    @staticmethod
    def get_next_id():
        return Customer.id

    @classmethod
    def increment_id(cls):
        cls.id += 1