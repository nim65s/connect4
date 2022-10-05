from enum import Enum



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
            print("colonne :", column)
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
        # Vertical
        for colonne in range(self.columns): # Tu parcoure les colonnes une par une
            for line in range(self.lines): # et pour chaque colonne tu parcoure les lignes une par une
                if self.grid[line][colonne] == color: # et on verifie si on a un enchainement de 4 cases de la meme couleur
                    adjacent += 1
                    if adjacent == 4:
                        return True
                else:
                    adjacent = 0
        # diagonal
        for colonne in range(0, 4, 1): # Tu parcoure les colonnes une par une
            for line in range(0, 3, 1): # et pour chaque colonne tu parcoure les lignes une par une
                if (self.grid[line][colonne]== color) and (self.grid[line+1][colonne+1]== color) \
                        and (self.grid[line+2][colonne+2]==color) \
                        and (self.grid[line+3][colonne+3]) == color: # en allant du bas à gauche à haut à droite de (1,1) à (6,7)
                        return True

        for colonne in range(6, 2, -1):  # Tu parcoure les colonnes une par une
            for line in range(0, 3, 1):  # et pour chaque colonne tu parcoure les lignes une par une
                if (self.grid[line][colonne]==color) and (self.grid[line + 1][colonne - 1]==color) \
                     and (self.grid[line + 2][colonne - 2]==color) \
                     and (self.grid[line + 3][colonne - 3] == color):
                    return True


        return False


        # TODO: Diagonal


    def tie(self) -> bool:
        """Check if the grid is full."""
        # TODO
        for line in range(0,5,1):
            for colonne in range(0,6,1):
                if self.grid[line][colonne] != Cell.EMPTY:
                    print(f"la case :[{line}][{colonne}]= {self.grid[line][colonne]} :)")
                    print("La grille n'est pas encore pleine :) jouez encore")

                    return False
                elif (self.grid[line][colonne] == Cell.A) or (self.grid[line][colonne] == Cell.A):
                    print("La grille est  pleine :( ")
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
