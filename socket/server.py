import socket
import threading
from typing import Tuple
import json

HEADER = 1024
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "DISCONNECT"
FORMAT = "utf-8"
print(SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)
data = {"name": "sushil"}
reply_message = {"hi": "sushil", "hello": "pema"}


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(1024).decode(FORMAT)
        if not msg:
            continue
        if msg == DISCONNECT_MESSAGE:
            connected = False
        print(f"[{addr}] {msg}")
        # reply = reply_message.get(msg, "{default}")
        reply = json.dumps(data)
        response = reply.encode(FORMAT)
        conn.send(response)
    print(f"[DISCONNECTED] .{addr}")
    conn.close()


def start_server():
    server.listen()
    print(f"[SERVER] server is listening on {SERVER}:{PORT}...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count() - 1}")


if __name__ == "__main__":
    print("[STARTING] server is starting...")
    start_server()
