from .game import Grid, Player


class ConsolePlayer(Player):
    def play(self, grid: Grid) -> int:
        ...
