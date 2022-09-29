from enum import Enum



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
        adjacent = 0
        superieur = 0
        valeur = 0
        color = self.grid[line][column]
        # Horizontal
        for cell in self.grid[line]:
            if cell == color:
                adjacent += 1
                if adjacent == 4:
                    return True
            else:
                adjacent = 0


        # TODO: Vertical
        for cell in range(line):
            for compte in range(column):

                if self.grid[cell][compte] == color:
                    superieur +=1
                    if superieur == 4:
                        return True
                    else:
                        superieur = 0
        # TODO: Diagonal
        for cell in self.grid[line]:
            for colomnes in self.grid[cell][column]:
                if cell == color:

                    if (int(cell-1) != color) or (int(cell+1) != color):
                        if (colomnes-1) == color or colomnes+1 == color:
                            valeur +=1
                        else:
                            valeur = 0
                    if (colomnes - 1) != color or (colomnes + 1) != color:
                        if (cell - 1) == color or (cell + 1) == color:
                            valeur += 1
                        else:
                            valeur = 0

                    if valeur == 4:
                        return True
                    else:
                         valeur = 0


        return False

    def tie(self):
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
