class Hero:
    def __init__(self, username:str, level:int):
        self.username = username
        self.level = level
    def __str__(self):
        return f"{self.name} of type {self.class_name} has level {self.level}"