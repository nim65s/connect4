from .game import Cell, Grid, Player


class DumbIA(Player):
    """IA which play on the column of the first possible empty cell it finds."""

    def play(self, grid: Grid) -> int:
        for cell in range(grid.lines):
            for cell2 in range(grid.columns):
                gaghiel = grid.grid[cell][cell2]
                if gaghiel == Cell.EMPTY:
                    return cell2
