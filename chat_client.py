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
            if message.lower() == 'exit':
                print("Exiting chat.")
                sock.close()
                break
            sock.send(message.encode())
        except Exception as e:
            print("Error sending data.")
            break

if len(sys.argv) != 3:
    print("Usage: python chat_client.py <IP> <Port>")
    sys.exit()

IP_address = sys.argv[1]
Port = int(sys.argv[2])
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP_address, Port))
except Exception as e:
    print(f"Connection failed: {e}")
    sys.exit()

print("Connected to chat server. Type your messages below:\n")

# Start receiving and sending threads
threading.Thread(target=receive_messages, args=(server,), daemon=True).start()
send_messages(server)

server.close()
