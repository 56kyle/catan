
import random

from enum import StrEnum, auto
from typing import Self


class Resource(StrEnum):
    """A resource type in the game of Catan"""
    SHEEP = auto()
    WHEAT = auto()
    WOOD = auto()
    BRICK = auto()
    ORE = auto()

    @classmethod
    def random(cls) -> Self:
        return random.choice(list(cls))









