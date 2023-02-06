import time
import socket
import pickle
import random
from  _thread import *
from player import Player


adress = '25.3.133.206'
port = 7777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((adress, port))
    print("Servidor iniciado!")
except:
    print("Não foi possível iniciar o servidor!")

#users = int(input("Quantos jogadores?\n"))



server.listen()

players = []

def threaded_client(conection, player):

    global players
    global currentPlayer

    conection.send(f'{players[player].ID}'.encode("utf-8"))
    
    while True:
        try:
            data = pickle.loads(conection.recv(2048))
            players[player] = data

            if not data:
                print("Desconectado! <Dados>")
                break
            else:
                if(len(players)>1):
                    for i in range(len(players)):
                        time.sleep(0.0001)
                        if ((i != player)):
                            conection.send(pickle.dumps(players[i]))
                else:
                    conection.send(pickle.dumps(None))

        except:
            break

    print("Não foi possível manter a conexão")
    conection.close()
    
currentPlayer = 0

while True:
    
    conn, addrs = server.accept()
    p = Player(0,0,50,50,(random.randint(0,255),random.randint(0,255),random.randint(0,255)), 0)
    p.ID = addrs[1]
    players.append(p)
    print("Conexão aceita. Conectado a: ", addrs[1])
    start_new_thread(threaded_client, (conn,  currentPlayer))

    currentPlayer += 1

   



