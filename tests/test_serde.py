import unittest
import random

from connect4.game import Cell, Grid
from connect4.serde import serialize_grid, deserialize_grid


class TestSerde(unittest.TestCase):
    @unittest.skip
    def test_grid_serde(self):
        grid = Grid()
        for line in range(grid.lines):
            for column in range(grid.columns):
                grid.grid[line][column] = random.choice([Cell.EMPTY, Cell.A, Cell.B])
        self.assertEqual(str(grid), str(deserialize_grid(serialize_grid(grid))))


if __name__ == "__main__":
    unittest.main()
