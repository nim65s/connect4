# Connect 4

TP n°1 de Conception Orientée Objet pour le M2 auro.

## Objectifs

1. commenter le décorateur `skip` pour `tests.test_game.TestGame.test_dumb_6` et implémenter
   `connect4.dump_ia.DumbIA.play` jusqu’à ce que `python -m unittest` fonctionne à nouveau
2. commenter le décorateur `skip` pour `tests.test_game.TestGame.test_column_win` et améliorer
   `connect4.game.Grid.win` jusqu’à ce que `python -m unittest` fonctionne à nouveau
3. commenter le décorateur `skip` pour `tests.test_game.TestGame.test_tie` et implémenter
   `connect4.game.Grid.tie` jusqu’à ce que `python -m unittest` fonctionne à nouveau. `python -m connect4` devrait
   également fonctionner.
4. implémenter `connect4.console_player.ConsolePlayer.play` jusqu’à ce que que le jeu soit utilisable avec
   `python -m connect4 --player-a ConsolePlayer`
