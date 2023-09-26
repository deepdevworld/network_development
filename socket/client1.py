import socket
import json
HEADER = 1024
PORT = 5050
DISCONNECT_MESSAGE = "DISCONNECT"
FORMAT = "utf-8"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    response = client.recv(1024)
    response = response.decode(FORMAT)
    response = json.loads(response)
    print(response)

send("hi")
send("DISCONNECT")
