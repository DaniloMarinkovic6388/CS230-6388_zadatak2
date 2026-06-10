import socket

client = socket.socket()
client.connect(("127.0.0.1", 5002))

username = input("Username: ")
password = input("Password: ")

client.send(username.encode())
client.send(password.encode())

print(client.recv(1024).decode())

client.close()