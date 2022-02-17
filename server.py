import json
import socket

from server_operations import Server
from services import initialize_PostgresDB


server = Server()
db = initialize_PostgresDB()
HOST = "127.0.0.1"
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
connection, address = s.accept()