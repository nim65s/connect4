from .game import Grid, Player


class CheaterB(Player):
    def play(self, grid: Grid) -> int:
        ...
