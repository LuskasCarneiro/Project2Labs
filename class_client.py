import socket
import re

class Client:
    def __init__(self, host=None, port = None):  # Defina PORT conforme necessário
        self.host = host
        self.port = port
        self.ag=1

    #codificar
    def stringify_move_ataxx(self, x, y, x2, y2):
        return f"MOVE {x},{y},{x2},{y2}"
    #descodificar
    def decode_stringify_move_ataxx(self, move_message):
        pattern = r"MOVE (\d+),(\d+),(\d+),(\d+)"
        match = re.match(pattern, move_message)
        if match:
            x, y, x2, y2 = map(int, match.groups())
            return x, y, x2, y2
        else:
            return None
    #conectar servividor
    def connect_to_server(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

        response = self.client_socket.recv(1024).decode()
        print(f"Server ResponseINIT: {response}")

        if "1" in response:
            self.ag=1
        else:
            self.ag=2
        # se este cliente é o primeiro jogador
        Game = response[-4:] #nome do jogo
        print("Playing:", Game)
        size = int(Game[1])

        # de quem é a vez

        return size
    
    def get_ag(self):
        return self.ag

