import random

from typing import Self, Iterable

from catan.board import Board
from catan.player import Player


class Game:
    def __init__(self, players: Iterable[Player], **kwargs):
        self.players: Iterable[Player] = players
        self.board: Board

    @classmethod
    def start(cls, players: Iterable[Player], **kwargs) -> Self:
        """Start a new game"""
        random.shuffle(*players)
        return cls(players=players, **kwargs)








