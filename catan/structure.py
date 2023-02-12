from dataclasses import dataclass, field
from typing import Set

from catan.resource_collection import ResourceCollection
from catan.player import Player
from catan.tile import Tile


@dataclass(frozen=True)
class Structure:
    """A structure on the board"""
    player: Player
    tiles: Set[Tile]
    cost: ResourceCollection



