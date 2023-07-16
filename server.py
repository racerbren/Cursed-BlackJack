import socket
from _thread import *
import sys
import pickle

server = socket.gethostbyname(socket.gethostname()) #Grab the IP address to use as server address
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))      #Bind the socket to server and port
except socket.error as e:       #Print an error if there is an issue
    print(e)

s.listen()      #Start the server and listen for new connections
print("Server up and running. Waiting for connections...")

connected = set()
games = {}
IDCount = 0


def threaded_client(conn, player, gameID):
    pass


while True:
    pass
