from .game import Grid, Player


class CheaterB(Player):
    """This IA cheats and modify the grid to ensure player B wins."""

    def play(self, grid: Grid) -> int:
        ...
