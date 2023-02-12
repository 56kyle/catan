

from dataclasses import dataclass, field

from catan.resource_collection import ResourceCollection
from catan.structure import Structure


@dataclass(frozen=True)
class Settlement(Structure):
    cost: ResourceCollection = field(
        init=False,
        default_factory=lambda: ResourceCollection(wood=1, brick=1, sheep=1, wheat=1)
    )


