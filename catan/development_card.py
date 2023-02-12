from abc import ABC

from catan.resource_collection import ResourceCollection


class DevelopmentCard(ABC):
    """A development card"""
    cost: ResourceCollection = ResourceCollection(wheat=1, sheep=1, ore=1)

    def __call__(self):
        raise NotImplementedError("DevelopmentCard is an abstract class")







