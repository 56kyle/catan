from dataclasses import dataclass, field

from catan.resource_collection import ResourceCollection
from catan.settlement import Settlement


@dataclass(frozen=True)
class City(Settlement):
    cost: ResourceCollection = field(init=False, default_factory=lambda: ResourceCollection(wheat=2, ore=3))








