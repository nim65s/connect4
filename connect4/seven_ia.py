from .game import Grid, Player
from .game import Cell

class SevenIA(Player):
    """IA which play all its turns on the seventh column."""

    def play(self, grid: Grid) -> int:
                return 6
