from socket import *

serverName = '127.0.0.1'
serverPort = 12000

while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    sentence = input('Escriba una frase en minúsculas:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
    clientSocket.close()