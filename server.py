from http import client
from multiprocessing.connection import Client
import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
clients = {}
BUFFER_SIZE = 4096

def setup():

    print("\n\t\t\t\t\t\t\t\ SHARE YOUR MUSIC \n")

    global IP_ADDRESS
    global PORT
    global SERVER
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)

    print("\t\t\t\t SERVER IS WAITING FOR INCOMING REQUESTS......\n")

    acceptConnections()


setup_thread = Thread(target= setup)
setup_thread.start()

def acceptConnections():
    global SERVER
    global client

    while True:
        client, addr = SERVER.accept()
        client_name = client.recv(4096).decode().lower()
        clients[client_name] = {
            "client": client,
            "address": addr,
            "connected_with": "",
            "file_name": "",
            "file_size": 4096
        }   
        print(f"Connection established with {client_name} : {addr}")

        thread = Thread(target= handleClient, args=(client, client_name))