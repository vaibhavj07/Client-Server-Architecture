import socket


HEADER = 1024
PORT = input("Enter the port number you want to connect: ")
PORT = int(PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#SERVER = "192.168.29.48"
SERVER = socket.gethostname()
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


# Accessing Employee Info
def Employee_Info():
    response = client.recv(2048)
    option = input(response.decode())
    client.send(str.encode(option))


#Add Employee
def Add_Employee():
    response = client.recv(2048)
    option = input(response.decode())
    client.send(str.encode(option))


# downloading file
def Download_files():
    response = client.recv(2048)
    option = input(response.decode())
    client.send(str.encode(option))
    filename = client.recv(2048).decode()
    print(filename)
    file = open(filename,"w")
    client.send(str.encode("FileName Received"))
    data = client.recv(2048).decode()
    print("File Data recived")
    file.write(data)
    client.send(str.encode("File Data received"))
    file.close()

#Access Logs
def Access_Logs():
    filename = client.recv(2048).decode()
    print(filename)
    file = open(filename,"w")
    client.send(str.encode("FileName Received"))
    data = client.recv(2048).decode()
    print("File Data recived")
    file.write(data)
    client.send(str.encode("File Data received"))
    file.close()
    
# Receive response
admin_access = False
while True:
    response = client.recv(2048)
    decoded_response = response.decode()
    if ('ADMIN ACCESS' in decoded_response):
        admin_access = True
    elif('NOMRAL ACCESS' in decoded_response):
        admin_access = False
    option = input(decoded_response)
    client.send(str.encode(option))
    if admin_access == True:
        if option == "a":
            Download_files()
        elif option =="b":
             Employee_Info()
        elif option =="c":
            Access_Logs()
        elif option == "d":
            print("Logged Out Successfully")
            client.close()
            admin_access = False
            break
    else:
        if option == "a":
            Download_files()
        elif option =="b":
             Employee_Info()
        elif option == "c":
            print("Logged Out Successfully")
            client.close()
            admin_access = False
            break



                




