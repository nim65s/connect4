from .game import Player


class ConsolePlayer(Player):
    def play(self, grid):
        print(self.grid)