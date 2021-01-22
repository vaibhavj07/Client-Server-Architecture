import socket 
import threading

HEADER = 1024
PORT = input("Enter the Port number: ")
PORT = int(PORT)
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADMINU = "ADMIN"
PASSU = "APASS"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send(str.encode('ENTER USERNAME : ')) # Request Username
    name = conn.recv(2048)
    conn.send(str.encode('ENTER PASSWORD : ')) # Request Password
    password = conn.recv(2048)
    password = password.decode()
    name = name.decode()
    if name ==  ADMINU and password == PASSU:
        connected = True
        conn.send(str.encode("Login Successful: "))
        print("Login Successful")
        
        '''while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False'''


    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
