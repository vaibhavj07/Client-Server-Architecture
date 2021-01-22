import socket

HEADER = 1024
PORT = input("Enter the port number you want to connect: ")
PORT = int(PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.29.48"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

response = client.recv(2048)

name = input(response.decode())	
client.send(str.encode(name))
response = client.recv(2048)
# Input Password
password = input(response.decode())	
client.send(str.encode(password))
''' Response : Status of Connection :
	1 : Registeration successful 
	2 : Connection Successful
	3 : Login Failed
'''
# Receive response 
response = client.recv(2048)
response = response.decode()
print(response)



