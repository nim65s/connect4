import os.path
import sys
import unittest

# sys.path.append('C:/Users/Madtec/Downloads/connect4-main/connect4-main')
# sys.path.append('../connect4')
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from connect4.game import Cell, Game, Grid

GRID_DUMB_6 = """
|.......|
|.......|
|.......|
|.......|
|.......|
|XOXOXO.|
+-------+
 0123456
"""


class TestModeles(unittest.TestCase):
    def test_grid_str(self):
        grid = Grid()
        print(type(Cell))
        grid.grid[0] = [Cell.A, Cell.B, Cell.A, Cell.B, Cell.A, Cell.B, Cell.EMPTY]
        self.assertEqual("\n" + str(grid), GRID_DUMB_6)

    @unittest.skip
    def test_dumb_6(self):
        from connect4.dumb_ia import DumbIA

        ai_a = DumbIA()
        ai_b = DumbIA()
        game = Game(ai_a, ai_b)
        for _ in range(3):
            game.play(ai_a, Cell.A)
            game.play(ai_b, Cell.B)
        self.assertEqual("\n" + str(game.grid), GRID_DUMB_6)

    # @unittest.skip
    def test_line_win(self):
        grid = Grid()
        grid.grid[0] = [Cell.A, Cell.A, Cell.A, Cell.A, Cell.B, Cell.B, Cell.B]
        self.assertTrue(grid.win(0, 0))
        self.assertFalse(grid.win(0, 6))

    # unittest.skip
    def test_column_win(self):
        grid = Grid()
        for line in range(4):
            grid.grid[line][0] = Cell.A
            grid.grid[line][1] = Cell.B if line == 0 else Cell.A
        # self.assertTrue(grid.win(0, 0))
        # self.assertTrue(grid.win(1, 0))
        self.assertFalse(grid.win(0, 1))
        print(grid)

    # @unittest.skip
    def test_diag_win(self):
        grid = Grid()
        for lig_col in range(4):
            grid.grid[lig_col][lig_col] = Cell.A
            grid.grid[lig_col][lig_col + 1] = Cell.B if lig_col == 0 else Cell.A
        # self.assertTrue(grid.win(0, 0))
        self.assertFalse(grid.win(0, 1))
        print(grid)

    @unittest.skip
    def test_tie(self):
        from connect4.dumb_ia import DumbIA

        ai_a = DumbIA()
        ai_b = DumbIA()
        game = Game(ai_a, ai_b)
        self.assertFalse(game.grid.tie())
        for _ in range(21):
            game.play(ai_a, Cell.A)
            game.play(ai_b, Cell.B)
        self.assertTrue(game.grid.tie())


if __name__ == "__main__":
    unittest.main()
