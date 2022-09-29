import argparse

from .game import Game, Player


PLAYERS = ["DumbIA", "ConsolePlayer", "CheaterB", "ClientPlayer"]


def get_player(player: str) -> Player:
    match player:
        case "DumbIA":
            from .dumb_ia import DumbIA

            return DumbIA()
        case "ConsolePlayer":
            from .console_player import ConsolePlayer

            return ConsolePlayer()
        case "CheaterB":
            from .cheater_b import CheaterB

            return CheaterB()
        case "ClientPlayer":
            from .client_player import ClientPlayer

            return ClientPlayer()


parser = argparse.ArgumentParser(description="Start a Connect 4 game.")
parser.add_argument("--player-a", choices=PLAYERS, default="DumbIA")
parser.add_argument("--player-b", choices=PLAYERS, default="DumbIA")


if __name__ == "__main__":
    args = parser.parse_args()
    game = Game(get_player(args.player_a), get_player(args.player_b))
    game.main()
