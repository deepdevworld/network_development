from typing import Literal, Optional, Type
import socket

import threading

connection_types = Literal["server", None]


class ConnectionManager:
    def __init__(self, ip_address: str = socket.gethostbyname(socket.gethostname()), port: int = 8080):
        self.server: Optional[socket.socket] = None
        self.client: Optional[socket.socket] = None
        self.ip_address = ip_address
        self.port = port
        self.bind_address = (self.ip_address, self.port)
        self.no_of_connected_client: int = threading.active_count() - 1

    def connect(self, connection_type: connection_types):
        """By default, the connection is set to client"""
        try:
            if connection_type == "Server":
                self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.server.bind(self.bind_address)
            else:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client.connect(self.bind_address)
        except Exception as e:
            print(e)
            pass

    def start(self):
        self.server.listen()
        print(f"[SERVER] server is listening on {self.server}:{self.port}")
        while True:
            conn, addr = self.server.accept()
            conn.recv()
            thread = threading.Thread(target=self.handel_client, args=(conn, addr))
            thread.start()

    def handel_client(self, conn: Type[socket.socket], addr):
        connected = True
        while connected:
            msg = conn.recv

    def convert_json_to_string(self):
        pass

    def convert_string_to_json(self):
        pass


class Server(ConnectionManager):
    pass


class Client:
    pass
