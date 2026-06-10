import socket

HOST = "127.0.0.1"
PORT = 5002

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("Server ceka klijenta...")
conn, addr = server.accept()

username = conn.recv(1024).decode()
password = conn.recv(1024).decode()

log = open("audit_log.txt", "a", encoding="utf-8")

if username == "admin" and password == "admin":
    conn.send("Uspesna prijava".encode())
    log.write(f"User '{username}' successfully logged in.\n")
else:
    conn.send("Neuspesna prijava".encode())
    log.write(f"User '{username}' failed login attempt.\n")

log.close()
conn.close()
server.close()