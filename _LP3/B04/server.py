from operator import mod
import socket;
port = 12349;

s = socket.socket();
s.bind(('127.0.0.1', port));
print('Socket binded to port : {port}'.format(port=port));

s.listen(1);
c, addr = s.accept();
print('Connection Received from {}'.format(addr));

public = c.recv(1024);
c.send('Dummy'.encode());
n = c.recv(1024);
# n=0

print('Public Key Received from Client : {}, {}'.format(public, n));

data = 45;
print("Data to be encrypted : ", data);

modRes = data;
for i in range(1, int(public)):
    modRes  = (modRes * data) % int(n);


cipherText = modRes;

c.send(str(cipherText).encode());
print("Cipher Text Sent : ", cipherText);

c.close();

