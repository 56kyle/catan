from dataclasses import dataclass
from enum import Enum
from typing import Self, Set


@dataclass(frozen=True)
class Hex:
    """An axial coordinate for a hex board"""
    q: int
    r: int

    @property
    def s(self) -> int:
        return -self.q - self.r

    @property
    def neighbors(self) -> Set[Self]:
        return {self + d for d in Direction}

    def __add__(self, other: Self) -> Self:
        return Hex(self.q + other.q, self.r + other.r)

    def __sub__(self, other: Self) -> Self:
        return Hex(self.q - other.q, self.r - other.r)


class Direction(Hex, Enum):
    """Direction on a hex board"""
    NORTH_EAST = Hex(1, -1)
    EAST = Hex(1, 0)
    SOUTH_EAST = Hex(0, 1)
    SOUTH_WEST = Hex(-1, 1)
    WEST = Hex(-1, 0)
    NORTH_WEST = Hex(0, -1)














