import socket                

port = 5005

prime_number = 23
premetive_root = 5

p = int(input("Enter a Private key: "))

s = socket.socket()          
print("Socket created...")
 
s.bind(('127.0.0.1', port))

s.listen(1)                 

c, addr = s.accept()      
print("\n")
print('Got a connection from', addr) 
print("\n")

server_publickey = (premetive_root ** p) % prime_number
c.send(str(server_publickey).encode()) 

client_publickey = c.recv(1024)
print("Received Public key from Client:",int(client_publickey))
print("\n")

server_secret = (int(client_publickey) ** p) % prime_number

print ("Final Secret Key: ", server_secret)
print("\n")
c.close()