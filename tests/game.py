from enum import Enum
from tkinter.tix import CELL


class Cell(Enum):
    EMPTY = "."
    A = "X"
    B = "O"


class Grid:
    lines = 6
    columns = 7

    def __init__(self):
        self.grid = [[Cell.EMPTY] * self.columns for _ in range(self.lines)]

    def __str__(self):
        ret = ""
        for line in range(self.lines - 1, -1, -1):
            ret += "|"
            for column in range(self.columns):
                ret += self.grid[line][column].value
            ret += "|\n"
        ret += "+" + "-" * self.columns + "+\n"
        ret += " " + "".join(str(i) for i in range(self.columns)) + "\n"
        return ret

    def place(self, column: int, cell: Cell) -> int:
        for line in range(self.lines):
            if self.grid[line][column] == Cell.EMPTY:
                self.grid[line][column] = cell
                return line
        raise ValueError(f"Column {column} is empty.")

    def win(self, line: int, column: int) -> bool:
        eva00 = 0
        eva01 = 0
        eva02 = 0
        color = self.grid[line][column]
        # Horizontal
        for cell in self.grid[line]:
            if cell == color:
                eva00 += 1
                if eva00 == 4:
                    return True
            else:
                eva00 = 0

        # TODO: Vertical

        for cell in self.grid[column]:
            if cell == color:
                eva01 += 1
                if eva01 == 4:
                    return True
            else:
                eva01 = 0
        # TODO: Diagonal
        eva02 = 0
        for cell in self.grid[line][column]:
            i = 1
            if cell == color:
                eva02 += 1
                while i < 4:
                    if self.grid[line + 1][column + 1] == color:
                        eva02 += 1
                    else:
                        eva02 = 0
                        break
                    i += 1
                i = 0
                while i < 4:
                    if self.grid[line - 1][column - 1] == color:
                        eva02 += 1
                    else:
                        eva02 = 0
                        break
                    i += 1
                i = 0
                while i < 4:
                    if self.grid[line - 1][column + 1] == color:
                        eva02 += 1
                    else:
                        eva02 = 0
                        break
                    i += 1
                i = 0
                while i < 4:
                    if self.grid[line + 1][column - 1] == color:
                        eva03 += 1
                    else:
                        eva03 = 0
                        break
                    i += 1
            else:
                eva03 = 0
        return False

    def tie(self, line: int, column: int):
        # TODO

        return False


class Player:
    def play(self, grid):
        raise NotImplementedError


class Game:
    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.player_b = player_b
        self.grid = Grid()

    def main(self):
        while True:
            if self.play(self.player_a, Cell.A):
                print(self.grid)
                print("A wins !")
                break
            if self.grid.tie():
                print(self.grid)
                print("Tie.")
                break
            if self.play(self.player_b, Cell.B):
                print(self.grid)
                print("B wins !")
                break
            if self.grid.tie():
                print(self.grid)
                print("Tie.")
                break

    def play(self, player: Player, cell: Cell) -> bool:
        column = player.play(self.grid)
        line = self.grid.place(column, cell)
        return self.grid.win(line, column)
