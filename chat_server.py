# Python program to implement server side of chat room. 
import socket 
import select 
import sys 
from _thread import *

# creates a TCP/IP socket
# AF_INET is the address family for IPv4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# checks whether sufficient arguments have been provided 
if len(sys.argv) != 3: 
    print ("Correct usage: script, IP address, port number")
    exit() 

# takes the first argument from command prompt as IP address 
IP_address = str(sys.argv[1]) 

# takes second argument from command prompt as port number 
Port = int(sys.argv[2]) 

# binds the server to an IP address and a port number
server.bind((IP_address, Port)) 

# server listens for incoming connections, the argument specifies""
server.listen(100) 

list_of_clients = [] 

def clientthread(conn, addr): 

    # sends a message to the client whose user object is conn 
    conn.send("Welcome to this chatroom!".encode())
    while True: 
            try: 
                message = conn.recv(2048) 
                if message: 
                    message = message.decode()
                    
                    # print the message and address of the user
                    print ("<" + addr[0] + "> " + message) 

                    # Calls broadcast function to send message to all 
                    broadcast("<" + addr[0] + "> " + message, conn) 

                else: 
                    # if the message is not received, the user has 
                    # disconnected, remove them from the list
                    remove(conn) 
                    break

            except: 
                continue

# The following function shows the message to all clients.
def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                clients.send(message.encode()) 
            except Exception as e: 
                print(f"Error sending message to {clients}: {e}")
                clients.remove(clients)
                clients.close() 

                # if the link is broken, we remove the client 
                remove(clients) 
# Removes the object from the list.
def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 

while True: 

    # Accepts a connection from a client
    conn, addr = server.accept() 
    # maintains a list of clients
    list_of_clients.append(conn) 

    # prints the address of the user that just connected 
    print (addr[0] + " connected")

    # creates and individual thread for every user 
    # that connects 
    start_new_thread(clientthread,(conn,addr))     

conn.close() 
server.close()