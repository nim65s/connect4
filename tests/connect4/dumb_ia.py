from .game import Grid, Player


class DumbIA(Player):
    def play(self, grid: Grid) -> int:
        for cell in self.grid[line]:
            
