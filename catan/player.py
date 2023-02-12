from dataclasses import dataclass

from catan.development_card import DevelopmentCard
from catan.resource_collection import ResourceCollection


class Player:
    """A player in the game"""
    def __init__(self, *args, **kwargs):
        self.resources: ResourceCollection = ResourceCollection()
        self.development_cards: list[DevelopmentCard] = []
        self.development_points: int = 0
        self.longest_road: int = 0
        self.largest_army: int = 0





