
from collections import Counter
from typing import Iterable

from catan.resource import Resource


class ResourceCollection(Counter):
    def __init__(self, iterable: Iterable[Resource] = None, /, **kwargs):
        super().__init__(iterable, **kwargs)




