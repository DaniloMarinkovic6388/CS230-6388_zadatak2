import socket
import time

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

for i in range(10, -1, -1):
    poruka = f"{i} sends remaining..."
    client.send(poruka.encode(), socket.MSG_OOB)
    print(poruka)
    time.sleep(5)

client.close()