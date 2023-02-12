
import random

from dataclasses import dataclass
from typing import Literal, Self

from catan.geometry.hex import Hex
from catan.resource import Resource


@dataclass(frozen=True)
class Tile:
    """A tile on the board"""
    coor: Hex
    resource: Resource
    die_roll: Literal[2, 3, 4, 5, 6, 8, 9, 10, 11, 12]

    @classmethod
    def random(cls, coor: Hex) -> Self:
        """Create a random tile"""
        # Literal typing requires a value from the set of possible values, not randint
        return cls(coor=coor, resource=Resource.random(), die_roll=random.choice([2, 3, 4, 5, 6, 8, 9, 10, 11, 12]))





