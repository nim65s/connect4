from .game import Player


class DumbIA(Player):
    def play(self, grid,line,column):
        for cell in grid[line][column]:
            print(cell)
