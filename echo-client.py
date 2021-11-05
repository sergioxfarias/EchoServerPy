#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Direccion IP o hostname del servidor
PORT = 65432        # Puerto usado por el servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hola, mundo')
    data = s.recv(1024)

print('Recibido', repr(data))