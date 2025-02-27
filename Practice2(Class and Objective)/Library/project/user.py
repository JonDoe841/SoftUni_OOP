class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        return ", ".join(sorted(self.books)) if self.books else "No books rented."

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"