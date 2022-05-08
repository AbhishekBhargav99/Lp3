from http import server
import socket;
port = 12345;

primeNumber = 23;
primitiveRoot = 9;

b = int(input('Enter the secret Key for Client : '));
clientPublicKey = primitiveRoot ** b % primeNumber;

s = socket.socket();
s.connect(('127.0.0.1', port));
print("Connected to Server {} at Port {}".format('127.0.0.1', port) );


serverPublicKey = s.recv(1024);
print('\n')
print('Public Key of Server : {}'.format(serverPublicKey));
print('\n')

clientSecretKey = int(serverPublicKey) ** b % primeNumber;
print('\n')
print('Secret Key : {}'.format(clientSecretKey));
print('\n')
s.send(str(clientPublicKey).encode())

s.close();











