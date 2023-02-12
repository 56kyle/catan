

from dataclasses import dataclass, field
from typing import Set

from catan.geometry.hex import Hex


class Port:
    tiles: Set[Hex]


