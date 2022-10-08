from .game import Cell, Grid, Player


class CheaterB(Player):
    """This IA cheats and modify the grid to ensure player B wins."""

    def play(self, grid: Grid) -> bool:
        i = 0
        j = 0
        for cell in range(grid.lines):
            for cell2 in range(grid.columns):
                gaghiel = grid.grid[cell][cell2]
                if gaghiel == Cell.A:
                    i += 1
                elif gaghiel == Cell.B:
                    j += 1
        print(grid)
        if i < j:
            return False
        elif i == j:
            return True
