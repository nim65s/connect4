import argparse

from .game import Game, Player

PLAYERS = ["DumbIA", "ConsolePlayer", "CheaterB", "ClientPlayer"]


def get_player(player: str) -> Player:
    if player == "DumbIA":
        from .dumb_ia import DumbIA

        return DumbIA()
    if player == "ConsolePlayer":
        from .console_player import ConsolePlayer

        return ConsolePlayer()
    if player == "CheaterB":
        from .cheater_b import CheaterB

        return CheaterB()
    if player == "ClientPlayer":
        from .client_player import ClientPlayer

        return ClientPlayer()

    raise ValueError(f"available players are {PLAYERS}")


parser = argparse.ArgumentParser(description="Start a Connect 4 game.")
parser.add_argument("--player-a", choices=PLAYERS, default="DumbIA")
parser.add_argument("--player-b", choices=PLAYERS, default="DumbIA")


if __name__ == "__main__":
    args = parser.parse_args()
    game = Game(get_player(args.player_a), get_player(args.player_b))
    game.main()
