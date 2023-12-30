##server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.AF_INET - comunicação via internet
#socket.SOCK_STREAM - TCP (Transmission Control Protocol) para transmitir as mensagens
#TCP - sequencial - manda mensagem uma de cada vez; a ordem pela qual o agente manda é a ordem pelo qual o outro agente recebe

import socket

#HOST = socket.gethostbyname(socket.gethostname())
HOST = '' #Mantem o HOST como vazio para aceitar conexões de qualquer endereçoIP
PORT = 9090 #mesma para client

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode() #1024:number of bytes; decode the message
    print(f"Message from client is: {message}")
    communication_socket.send("Got your message! Thank you!".encode('utf-8'))
    communication_socket.send("".encode('utf-8'))
    communication_socket.close()
    print(f"Communication with {address} ended!")