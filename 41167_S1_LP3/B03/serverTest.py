from http import client
import socket
port = 12345;

primeNumber = 23;
primitiveRoot = 9;

a = int(input('Enter the secret Key for server : '));
serverPublicKey = primitiveRoot ** a % primeNumber;


s = socket.socket();
s.bind(('127.0.0.1', port));
print('Socket binded to port : {port}'.format(port=port));

s.listen(5);
c, addr = s.accept();
print("Got Connection Request from {}".format(addr));

c.send(str(serverPublicKey).encode());
clientPublicKey = c.recv(1024);


print('\n')
print('Public Key of Client : {}'.format(clientPublicKey));
print('\n')


serverSecretKey = int(clientPublicKey) ** a % primeNumber;
print('\n')
print('Secret Key : {}'.format(serverSecretKey));
print('\n')
c.close();





