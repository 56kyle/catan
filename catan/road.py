
from dataclasses import dataclass, field

from catan.resource import Resource
from catan.resource_collection import ResourceCollection
from catan.structure import Structure


@dataclass(frozen=True)
class Road(Structure):
    """A road on the board"""
    cost: ResourceCollection = field(init=False, default_factory=lambda: ResourceCollection({
        Resource.BRICK: 1,
        Resource.WOOD: 1,
    }))




