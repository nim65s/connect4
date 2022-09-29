import socket

from .game import Player

# from .serde import serialize_grid

HOST = "localhost"
PORT = 50011


class ClientPlayer(Player):
    def play(self, grid) -> int:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(grid.encode())
            return s.recv(1)
