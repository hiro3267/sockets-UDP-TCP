from socket import *

serverName = '10.0.99.150'
severPort = 1228
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, severPort))
sentence = input('Input lowercase sentence: \n')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()