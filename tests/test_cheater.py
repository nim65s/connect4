import unittest

from connect4.game import Cell, Game


class TestCheater(unittest.TestCase):
    @unittest.skip
    def test_cheater(self):
        from connect4.cheater_b import CheaterB
        from connect4.dumb_ia import DumbIA

        ai_a = DumbIA()
        ai_b = CheaterB()
        game = Game(ai_a, ai_b)
        self.assertFalse(game.play(ai_a, Cell.A))
        self.assertTrue(game.play(ai_b, Cell.B))


if __name__ == "__main__":
    unittest.main()
