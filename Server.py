import socket 
import threading
import time



PORT = input("Enter the Port number: ")
PORT = int(PORT)
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
ADMINU = "ADMIN"
PASSU = "PASSA"
NORMALU = "NORMAL"
PASSN = "PASSN"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
global EMPLOYEE_NAME
global EMPLOYEE_PhoneNumber
global Employee_Id
EMPLOYEE_NAME = ["ADITYA","ARAVINDAN","BRANDOM", "VAIBHAV"]
EMPLOYEE_PhoneNumber = ["9876543271","4738493849", "6574839203", "54637284938"]
Employee_Id = ["12345", "87463", "64382", "98437"]
 

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    named_tuple = time.localtime() # get struct_time
    Time = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    f = open("Logs.txt","a")
    f.write("[NEW CONNECTION] " + str(addr) + "connected at " + str(Time) + "\n")
    f.close()
    conn.send(str.encode('ENTER USERNAME : ')) # Request Username
    name = conn.recv(2048)
    conn.send(str.encode('ENTER PASSWORD : ')) # Request Password
    password = conn.recv(2048)
    password = password.decode()
    name = name.decode()
    if name ==  ADMINU and password == PASSU:
        connected = True
        while connected:
            conn.send(str.encode('Login Successful:ADMIN ACCESS\n --------------------------------------------------- \nOptions:\na. Download File\nb. Access Employee Info\nc. Access Logs \nd. Log Out:  '))
            option_selected = conn.recv(2048)
            option_selected = option_selected.decode()
            if (option_selected == "a"):
                transfer_file(conn, addr)
            elif (option_selected == "b"):
                Access_Employee_Info(conn, addr)
            elif(option_selected == "c"):
                Access_Logs(conn, addr)
            elif(option_selected == "d"):
                connected = False
                print("Log out")
                conn.close()       
    elif name == NORMALU and password == PASSN:
        connected = True
        while connected:
            conn.send(str.encode('Login Successful:NORMAL ACCESS\n --------------------------------------------------- \nOptions:\na. Download File\nb. Access Employee Info\nc. Log Out: '))
            option_selected = conn.recv(2048)
            option_selected = option_selected.decode()
            if (option_selected == "a"):
                transfer_file(conn, addr)
            elif (option_selected == "b"):
                Access_Employee_Info(conn, addr)
            elif(option_selected == "c"):
                connected = False
                print("Log out")
                conn.close()       
    else:
        conn.send(str.encode("INVALID CREDENTIALS... CONNECTION CLOSED"))
        print("UNAUTHORIZED ACCESS..CONNECTION CLOSED")
        conn.close()
                    

def transfer_file(conn, addr):
    conn.send(str.encode('Select the file download: \nOptions:\na. SOP1\nb. SOP2\nc. SOP3: '))
    file_selected = conn.recv(2048)
    file_Selected = file_selected.decode()
    if(file_Selected == "a"):
        file = open("SOP1.txt", "r")
        data = file.read(2048)
        conn.send(str.encode("SOP1.txt"))
        msg = conn.recv(2048).decode()
        print(msg)
        conn.send(str.encode(data))
        msg = conn.recv(2048).decode()
        print(msg)
        file.close()
        pass
    elif(file_Selected == "b"):
        file = open("SOP2.txt", "r")
        data = file.read(2048)
        conn.send(str.encode("SOP2.txt"))
        msg = conn.recv(2048).decode()
        print(msg)
        conn.send(str.encode(data))
        msg = conn.recv(2048).decode()
        print(msg)
        file.close()
        pass
    elif(file_Selected == "c"):
        file = open("SOP3.txt", "r")
        data = file.read(2048)
        conn.send(str.encode("SOP3.txt"))
        msg = conn.recv(2048).decode()
        print(msg)
        conn.send(str.encode(data))
        msg = conn.recv(2048).decode()
        print(msg)
        file.close()
        pass
    else:
        conn.send(str.encode("Invalid Option"))
        conn.close()
        pass

def Access_Employee_Info(conn, addr):
    conn.send(str.encode('Enter the Employee Name: '))
    name_selected = conn.recv(2048)
    name_selected = name_selected.decode()
    name_selected = name_selected.upper()
    index = EMPLOYEE_NAME.index(name_selected)
    PhoneNumber = EMPLOYEE_PhoneNumber[index]
    EmpId = Employee_Id[index]
    Info = "Name: " +  name_selected +"\n" +  "EmpId: " + EmpId + "\n" + "Phone Number: " + PhoneNumber
    conn.send(str.encode(Info))
    print("Employee Info Sent")


'''def Add_Employee(conn, addr):
    conn.send(str.encode('Enter Employee Name'))
    name = conn.recv(2048)
    name = name.decode()
    name = name.upper()
    EMPLOYEE_NAME.append(name)
    print("Employee Name Added")
    print(EMPLOYEE_NAME)'''

    
def Access_Logs(conn, addr):
    file = open("Logs.txt","r")
    data = file.read(2048)
    conn.send(str.encode("Logs.txt"))
    msg = conn.recv(2048).decode()
    print(msg)
    conn.send(str.encode(data))
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
