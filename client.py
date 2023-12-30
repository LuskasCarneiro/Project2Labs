##client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.AF_INET - comunicação via internet
#socket.SOCK_STREAM - TCP (Transmission Control Protocol) para transmitir as mensagens
#TCP - sequencial - manda mensagem uma de cada vez; a ordem pela qual o agente manda é a ordem pelo qual o outro agente recebe

import socket

HOST = '192.168.1.79' #se for noutro pc e estiver a comunicar comigo tem de ter o HOST do meu pc
PORT = 9090 #mesma para server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

client.send("Hello World!".encode('utf-8'))
print(client.recv(1024).decode())


# Desta maneira nao comunica entre dois computadores, estou a tentar utilizar IPv4 do meu pc - endereço IP público do meu roteador ou da minha conexão com a Internet