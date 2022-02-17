import json
import socket

from server_operations import Server

server = Server()
db = db_engine()
HOST = "127.0.0.1"
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
connection, address = s.accept()