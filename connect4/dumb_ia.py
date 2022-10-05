from .game import Grid, Player


class DumbIA(Player):
    """IA which play on the column of the first possible empty cell it finds."""

    def play(self, grid: Grid) -> int:
        ...
