# -*- coding: utf-8 -*-
import socket
HOST = '127.0.0.1'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

while True:
    conn, addr = server.accept()
    clientMessage = conn.recv(1024)

    print('Client message is:', clientMessage.decode("utf-8"))

    serverMessage = 'I\'m here!'
    conn.sendall(serverMessage.encode())
    conn.close()
