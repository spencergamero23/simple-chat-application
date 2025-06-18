import socket
import sys
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(2048)
            if not message:
                print("Disconnected from server.")
                break
            print("\n" + message.decode())
        except:
            print("Error receiving data.")
            break

def send_messages(sock):
    while True:
        try:
            message = input()
            sock.send(message.encode())
        except:
            print("Error sending data.")
            break

if len(sys.argv) != 3:
    print("Usage: python chat_client.py <IP> <Port>")
    sys.exit()

IP_address = sys.argv[1]
Port = int(sys.argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP_address, Port))

print("Connected to chat server. Type your messages below:\n")

# Start receiving and sending threads
threading.Thread(target=receive_messages, args=(server,), daemon=True).start()
send_messages(server)

server.close()
