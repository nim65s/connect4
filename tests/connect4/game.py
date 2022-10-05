from enum import Enum
from msilib.schema import SelfReg


class Cell(Enum):
    """Enumeration representing a Connect4 Cell."""

    EMPTY = "."
    A = "X"
    B = "O"


class Grid:
    """Grid of 42 Cells."""

    lines = 6
    columns = 7

    def __init__(self):
        """Initialize a "self.grid" member: a list of list of Cells."""
        self.grid = [[Cell.EMPTY] * self.columns for _ in range(self.lines)]

    def __str__(self) -> str:
        """Reprensent this Grid as an ASCII image."""
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
        """Put one Cell into one of the 7 columns of this grid. Return the line where
        the token stops."""
        for line in range(self.lines):
            if self.grid[line][column] == Cell.EMPTY:
                self.grid[line][column] = cell
                return line
        raise ValueError(f"Column {column} is full.")

    def win(self, line: int, column: int) -> bool:
        """Check if the Cell at "line" / "column" is part of 4 Cells from the same
        player in a horizontal / vertical / diagonal line."""
        adjacent = 0
        color = self.grid[line][column]
        # Horizontal
        for cell in self.grid[line]:
            if cell == color:
                adjacent += 1
                if adjacent == 4:

                    return True
            else:
                adjacent = 0

        eva00 = 0
        eva01 = 0
        eva02 = 0
        i = 0
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
            for cell in range(6):
                sachiel = self.grid[cell][column]
                if sachiel == color:
                    eva01 += 1
                    if eva01 == 4:
                        return True
                else:
                    eva01 = 0
            eva02 = 0

        # TODO: Diagonal

        for cell in range(6):
            for cell2 in range(7):
                shamshel = self.grid[cell][cell2]

                if shamshel == color:
                    eva02 += 1
                    while i < 4:

                        if (
                            (cell2 - 1) < 0
                            and (cell - 1) < 0
                            and self.grid[cell - 1][cell2 - 1] == color
                        ):
                            eva02 += 1
                            if eva02 == 4:
                                return True
                        else:
                            eva02 = 0
                            break
                        i += 1
                    i = 0

                    while i < 4:
                        if (
                            (cell2 + 1) < 7
                            and (cell + 1) < 6
                            and self.grid[cell + 1][cell2 + 1] == color
                        ):
                            print(color)
                            eva02 += 1
                            if eva02 == 4:

                                return True
                        else:
                            eva02 = 0
                            break
                        i += 1
                    i = 0

                    while i < 4:
                        if (
                            (cell2 + 1) < 7
                            and (cell - 1) < 0
                            and self.grid[cell - 1][cell2 + 1] == color
                        ):
                            eva02 += 1
                            if eva02 == 4:
                                return True
                        else:
                            eva02 = 0
                            break
                        i += 1
                    i = 0

                    while i < 4:
                        if (
                            (cell + 1) < 6
                            and (cell - 1) < 1
                            and self.grid[cell + 1][cell2 - 1] == color
                        ):
                            eva02 += 1
                            if eva02 == 4:
                                return True
                        else:
                            eva02 = 0
                            break
                        i += 1

                else:
                    eva02 = 0
        return False

    def tie(self) -> bool:
        """Check if the grid is full."""
        # TODO
        for cell in range(6):
            for cell2 in range(7):
                if self.win(cell, cell2) == True:
                    return False
        return True


class Player:
    """Abstract base class for Players in this game."""

    def play(self, grid: Grid) -> int:
        """Main method for the player: show them the current grid, and ask them on which
        column they want to play."""
        raise NotImplementedError


class Game:
    """Main class of this project."""

    def __init__(self, player_a: Player, player_b: Player):
        """Initialize a new game with 2 Players and a Grid."""
        self.player_a = player_a
        self.player_b = player_b
        self.grid = Grid()

    def main(self):
        """Let players play until one of the win or the grid is full."""
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
        """Process one turn for one player.

        Ask the player  on which column they want to play, ask the grid on which line
        the token stops, and check if this was a winning move."""
        column = player.play(self.grid)
        line = self.grid.place(column, cell)
        return self.grid.win(line, column)
