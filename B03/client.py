import socket                

port = 5005

prime_number = 23
premetive_root = 5

q = int(input("Enter a Private Key: "))

s = socket.socket()          
print("Socket created...")
 
s.connect(('127.0.0.1', port)) 

client_publickey = (premetive_root ** q) % prime_number             
server_publickey = s.recv(1024) 
print("\n")
print("Received Public key from Server:",int(server_publickey))
print("\n")

s.send(str(client_publickey).encode())
client_secret = (int(server_publickey) ** q) % prime_number
print ("Final Secret Key: ", client_secret)
print("\n")

s.close()