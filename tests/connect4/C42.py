from .game import Cell, Grid, Player


class DumbIA(Player):
    """IA which play on the column of the first possible empty cell it finds."""

    def play(self, grid: Grid) -> int:
        for cell in range(6):
            for cell2 in range(7):
                test = grid.grid[cell][cell2]

                if reite(cell, cell2, grid) == True:
                    return cell2 + 3
                elif seizonsenryaku(cell, cell2, grid) == True:
                    return cell2 + 3
                elif seizonsenryaku2(cell, cell2, grid) == True:
                    return cell2

                # elif(seizonsenryaku3(cell,cell2,grid) == True):
                # return (cell2+3)

        for cell in range(6):
            for cell2 in range(7):
                testo = grid.grid[cell][cell2]
                if testo == Cell.EMPTY:
                    return cell2


def reite(line: int, column: int, grid) -> bool:
    adjacent = 0
    # Horizontal
    column3 = column + 3
    column0 = column - 3
    if column3 < 7:
        for cell in range(column, column3):
            if grid.grid[line][cell] == Cell.B:
                adjacent += 1
                if adjacent == 3 and grid.grid[line][column3] == Cell.EMPTY:
                    return True
            else:
                adjacent = 0


def seizonsenryaku(line: int, column: int, grid) -> bool:
    adjacent = 0
    # Horizontal
    column3 = column + 3
    if column3 < 7:
        for cell in range(column, column3):
            if grid.grid[line][cell] == Cell.A:
                adjacent += 1
                if adjacent == 3 and grid.grid[line][column3] == Cell.EMPTY:
                    return True
            else:
                adjacent = 0


def seizonsenryaku2(line: int, column: int, grid) -> bool:
    eva00 = 0
    # vertical
    line3 = line + 3
    if line3 < 6:
        for cell in range(line, line3):
            if grid.grid[cell][column] == Cell.A:
                eva00 += 1
                if eva00 == 3 and grid.grid[line3][column] == Cell.EMPTY:
                    return True
            else:
                eva00 = 0


def seizonsenryaku2(line: int, column: int, grid) -> bool:
    eva00 = 0
    # vertical
    line3 = line + 3
    if line3 < 6:
        for cell in range(line, line3):
            if grid.grid[cell][column] == Cell.A:
                eva00 += 1
                if eva00 == 3 and grid.grid[line3][column] == Cell.EMPTY:
                    return True
            else:
                eva00 = 0


"""
def seizonsenryaku3(line: int, column: int, grid) -> bool:
            eva00 = 0
            # vertical
            line3=line+3
            i=0
            if grid.grid[line][column] == Cell.A :
                eva00 += 1
                while(i<4):
                    if ((line+1) < 7 and (column+1) < 6 and grid.grid[line+1][column+1] == Cell.A):
                        eva00 += 1
                        if eva00  == 3 and grid.grid[line3][column] == Cell.EMPTY :
                            return True
                    else:
                        eva00 = 1
                    i += 1
            else:
                eva00 = 0
"""
