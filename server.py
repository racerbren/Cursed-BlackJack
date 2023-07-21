import socket
from _thread import *
import sys
import pickle
from multiplayer_game import Game

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
    global IDCount
    conn.send(str.encode(str(player)))
    reply = ""

    while True:
        data = conn.recv(4096).decode()
        if gameID in games:
            game = games[gameID]
            if not data:
                break
            else:
                if data == "reset":
                    pass
                elif data != "get":
                    game.play(player, data)
                reply = game
                conn.sendall(pickle.dumps(reply))
        else:
            break
    print("Lost Connection.")
    try:
        del games[gameID]
        print("Closing Game ", gameID)
    except:
        pass
    IDCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    IDCount += 1
    player = 0
    gameID = (IDCount - 1) // 2

    if IDCount % 2 == 1:
        games[gameID] = Game(gameID)
        print("Creating a new game...")
    else:
        games[gameID].ready = True
        player = 1

    start_new_thread(threaded_client, (conn, player, gameID))

