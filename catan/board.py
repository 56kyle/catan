
from dataclasses import dataclass, field
from typing import Set

from catan.city import City
from catan.port import Port
from catan.resource import Resource
from catan.road import Road
from catan.settlement import Settlement
from catan.structure import Structure
from catan.tile import Tile


@dataclass
class Board:
    """A Catan board"""
    tiles: Set[Tile] = field(default_factory=set)
    roads: Set[Road] = field(default_factory=set)
    settlements: Set[Settlement] = field(default_factory=set)
    cities: Set[City] = field(default_factory=set)
    robber: Tile = field(default=None)
    ports: Set[Port] = field(default_factory=set)

    @property
    def structures(self) -> Set[Structure]:
        """Get all structures on the board"""
        return self.roads | self.settlements | self.cities

    def get_adjacent_tiles(self, tile: Tile) -> Set[Tile]:
        """Get the tiles adjacent to the given tile"""
        return {t for t in self.tiles if t.coor in tile.coor.neighbors}

    def get_tiles_with_resource(self, resource: Resource) -> Set[Tile]:
        """Get the tiles with the given resource"""
        return {t for t in self.tiles if t.resource == resource}

    def structures_by_tile(self, tile: Tile) -> Set[Structure]:
        """Get the structures on the given tile"""
        return {s for s in self.structures if tile in s.tiles}



