import tkinter as tk
from tkinter import scrolledtext
import socket
import sys
import threading

class GUI:
    def __init__(self, ip, port):
        # Connecting to server
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.connect((ip, port))
        except Exception as e:
            print(f"Connection failed: {e}")
            sys.exit(1)

        self.root  = tk.Tk()
        self.root.title("Simple Chat Application")

        # Configuring grid weights
        self.root.configure(bg="gray17")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Textbox configs
        self.textbox = scrolledtext.ScrolledText(self.root,wrap=tk.WORD,bg="gray28", fg="white", insertbackground="white")
        self.textbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Entry and Button configs
        self.entry = tk.Entry(self.root,fg="white", bg="gray29", insertbackground="white")
        self.entry.grid(row=1, column=0, padx=10, pady=(0,10), sticky="ew")
        self.entry.bind("<Return>", lambda event: self.send_messages())

        self.send_button = tk.Button(self.root, text="Send", command=self.send_messages)
        self.send_button.grid(row=1, column=1, padx=(0,10), pady=(0,10), sticky="ew")

        # Make row 1's column exampand too
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_columnconfigure(0, weight=1)

        threading.Thread(target=self.receive_messages, daemon=True).start()
        self.root.mainloop()

    def receive_messages(self):
        while True:
            try:
                message = self.server.recv(2048)
                if not message:
                    print("Disconnected from server.")
                    break
                self.textbox.insert(tk.END, f"{message.decode()}\n")
                self.textbox.see(tk.END)  # Scroll to the end
            except Exception as e:
                print(f"Error receiving data: {e}")
                break        
    
    def send_messages(self):
        message = self.entry.get()
        if message:
            try:
                self.server.send(message.encode())
                self.textbox.insert(tk.END, f"You: {message}\n")  # Optional: show your own message
                self.entry.delete(0, tk.END)  # Clear the entry box
            except Exception as e:
                print(f"Error sending data: {e}")

#Start the GUI
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python chat_client.py <IP> <Port>")
        sys.exit()

    ip = sys.argv[1]
    port = int(sys.argv[2])
    GUI(ip, port)
