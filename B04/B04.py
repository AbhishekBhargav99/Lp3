import random
import socket

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calculate_d(e, phi):
    i = 1
    while ((phi*i)+1) % e != 0:
        i = i+1
        
    d = ((phi*i) + 1) / e
    return d

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5), 2):
        if num % n == 0:
            return False
    return True

def generate_key(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('P and Q cannot be equal')

    n = p*q
    phi = (p-1)*(q-1)
    g = 0
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    print("e",e)
    d = calculate_d(e, phi)
    print("d",d)
    return e, d, n

def encrypt(key, n, plaintext):
    cipher = int(int(plaintext ** key)%n) 

    return cipher

def decrypt(key, n, ciphertext):
    plain = int(int(ciphertext ** key)%n)

    return plain

choice = int(input("Enter 1 to send encrypted data\nEnter 2 to decrypt received data\n"))
port = 5007

if choice == 1:
    s = socket.socket()          
    print("Socket created...")

    s.bind(('127.0.0.1', port))
    s.listen(1)                 
    c, addr = s.accept()                                                           # [1361,1789,1753,2053]

    public = c.recv(1024)
    n = c.recv(1024)

    print("Received public key: (", public, ", ", n, ")\n")

    message = input("Enter a message to encrypt with your public key: ")

    encrypted_msg = encrypt(int(public), int(n), message)
    print("Your encrypted message is: ")
    print(encrypted_msg, "\n")

    c.send(str(encrypted_msg))

    print("Encrypted message sent") 

elif choice == 2:
    s = socket.socket()          
    print("Socket created...")
    s.connect(('127.0.0.1', port))

    p = int(input("Enter public prime number:"))
    q = int(input("Enter private prime number: "))

    print("Generating your public/private keypairs now . . .")
    public, private, n = generate_key(p, q)

    print("Your public key is (", public , ", ", n, ") and your private key is (", private, ", ", n, ")")

    s.send(str(public))
    s.send(str(n))
    print("Public Key Sent")

    print("Waiting to receive encrypted data...")

    content = s.recv(1024)
    content = int(content)

    print("Received message: ", content)

    print("\nDecrypting received message with private key . . .")
    decrypted_msg = decrypt(private, n, content)
    print("\nYour message is: ", decrypted_msg)

else:
    print ("Enter valid choice")

s.close()