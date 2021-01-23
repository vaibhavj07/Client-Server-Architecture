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
        conn.send(str.encode('Login Successful: \nOptions:\na. Download File\nb. Access Employee Directory\nc. Access Log Files\nd. Log Out: '))
        option_selected = conn.recv(2048)
        option_selected = option_selected.decode() 
        if (option_selected == "a"):
            transfer_file(conn, addr)
        elif (option_selected == "b"):
            print("2")
        elif (option_selected == "c"):
            print("3")
        elif(option_selected == "d"):
            print("Log out")
    else:
        conn.close()
                
    '''while connected:
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(FORMAT)
                    if msg == DISCONNECT_MESSAGE:
                        connected = False '''      

def transfer_file(conn, addr):
    conn.send(str.encode('Select the file download: \nOptions:\na. SOP1\nb. SOP2\nc. SOP3: '))
    file_selected = conn.recv(2048)
    file_Selected = file_selected.decode()
    if(file_Selected == "a"):
        file = open("SOP1.txt", "r")
        data = file.read(2048)
        conn.send("SOP1.txt".encode(FORMAT))
        msg = conn.recv(2048).decode()
        print(msg)
        conn.send(data.encode(FORMAT))
        msg = conn.recv(2048).decode()
        print(msg)
        file.close()
    elif(file_Selected == "b"):
        file = open("SOP2.txt", "r")
        data = file.read(2048)
        conn.send("SOP2.txt".encode(FORMAT))
        msg = conn.recv(2048).decode()
        print(msg)
        conn.send(data.encode(FORMAT))
        msg = conn.recv(2048).decode()
        print(msg)
        file.close()
    elif(file_Selected == "a"):
        file = open("SOP3.txt", "r")
        data = file.read(2048)
        conn.send("SOP3.txt".encode(FORMAT))
        msg = conn.recv(2048).decode()
        print(msg)
        conn.send(data.encode(FORMAT))
        msg = conn.recv(2048).decode()
        print(msg)
        file.close()
        
        


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
