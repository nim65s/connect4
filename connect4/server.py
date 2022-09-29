import socket

from .console_player import ConsolePlayer
from .game import Player

# from .serde import deserialize_grid

HOST = "localhost"
PORT = 50011


class Server(Player):
    def __init__(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((HOST, PORT))
                while True:
                    s.listen()
                    conn, addr = s.accept()
                    with conn:
                        while True:
                            data = conn.recv(1000)
                            if not data:
                                break
                            grid = data.decode()
                            column = self.play(grid)
                            conn.sendall(column.encode())
            except KeyboardInterrupt:
                s.close()


class ConsoleServer(Server, ConsolePlayer):
    pass


if __name__ == "__main__":
    ConsoleServer()
