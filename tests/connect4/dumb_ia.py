from .game import Grid, Player


class DumbIA(Player):
    def play(self, grid: Grid) -> int:
        for cell in range(6):
            for cell2 in range(7):
                ramiel = grid[cell][cell2]
                if ramiel == ".":
                    grid[cell][cell2] = ["."]
                    break
