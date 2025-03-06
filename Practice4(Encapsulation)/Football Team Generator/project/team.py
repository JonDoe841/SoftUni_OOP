from typing import List

from project.player import Player


class Team:
    def __init__(self,name,rating):
        self.__rating = rating
        self.__name = name
        self.__players: List[Player] = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"
    def remove_player(self,player_name):
        player = next((p for p in self.__players if p.name == player_name), None)
        if player:
            self.__players.remove(player)
            return player
        return f"Player {player_name} not found"