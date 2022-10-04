from .game import Grid, Player, Cell


class DumbIA(Player):
    def play(self, grid: Grid) -> int:
        i=0
        for cell in range(6):
            for cell2 in range(7):
                ramiel = grid[cell][cell2]
                if(ramiel == "." and (i%2)== 0):
                    grid[cell][cell2] = [Cell.A]
                else:
                    grid[cell][cell2] = [Cell.B]
                i +=1
                
