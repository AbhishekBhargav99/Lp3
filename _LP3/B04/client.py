import random
import socket;
port = 12349;

P = int(input("Enter Prime Number 1 :")); 
Q = int(input("Enter Prime Number 2 :"));


def isPrime(n):
    if(n == 2) :
        return True;
    if(n < 2 or  n % 2 == 0):
        return False;
    for i in range(3, int(n/2 + 1), 2):
        if(n % i == 0):
            return False;
    return True;
    


def phi(a, b):
    return (a - 1) * (b - 1);

def gcd(a, b):
    if a == 0 :
        return b;
    return gcd(b%a, a);

def calculated(phin, e):
    i = 1;
    while ((phin * i + 1) % e != 0):
        i = i + 1;
    d = int( (phin * i + 1) / e);
    return d;

def generateKeys(P, Q):
    if(not isPrime(P) or not isPrime(Q) or P == Q):
        print('Enter Valid Prime Numbers')
        exit(1);
    
    n = P * Q;
    phin = phi(P, Q);
    g = 0;
    while g != 1:
        e = random.randrange(1, phin);
        g = gcd(e, phin);
    
    print("Public Key : {} , {} ".format(e, n));

    d = calculated(phin, e);
    print('phin : ', phin);
    print('e : ', e);
    print('privaye key : ', d);
    return e, d, n; 


public, private, n =generateKeys(P, Q);

s = socket.socket();
s.connect(('127.0.0.1', port));
print('Client connected to Server {} at port {}'.format('127.0.0.1', port));


s.send(str(public).encode());
s.recv(1024);
s.send(str(n).encode());
print("Public Key sent : {}, {}".format(public, n));

cipherText = s.recv(1024).decode();
print("Received Cipher Text : ", cipherText);


modRes = int(cipherText);
for i in range(1, int(private)):
    modRes  = (modRes * int(cipherText)) % int(n);

plainText = modRes;

print("Decrypted Text : ", plainText)
s.close();





