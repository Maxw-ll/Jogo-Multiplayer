import socket
import pickle

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '25.3.133.206'
        self.port = 7777
        self.adrrs = (self.server, self.port)


    def connect(self):
        try: 
            self.client.connect(self.adrrs)
            print("Cliente conectado ao servidor!")
            return int(self.client.recv(2048).decode("utf-8"))
           
        except:
            print("Não foi possível se conectar ao servidor")


    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
        except:
            print("Não foi possível enviar os dados")

    def receive(self):
        try:
            
            return pickle.loads(self.client.recv(2048))
           
        except:
            print("Não foi possível receber dados")
    
    





