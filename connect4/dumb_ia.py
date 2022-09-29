from .game import Player
from .game import Cell



class DumbIA(Player):
    def play(self, grid) -> int:
        for line in range(grid.lines):# on parcoure les lignes de la grille
            for colonne in range(grid.columns):#on parcoure les colonnes de la grille
                if grid.grid[line][colonne] == Cell.EMPTY:#on teste si la case qui correspond à la ligne et la colonne est vide
                    print("YUPIIIII on a trouvé une colonne vide")#on dit que c'est bon
                    return colonne#on retourne la premiere colonne dans laquelle on peut mettre un jeton

