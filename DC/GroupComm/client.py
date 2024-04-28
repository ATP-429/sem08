import socket

s = socket.socket()
s.connect(('127.0.0.1', 1000))
print("Connected with server!")
print("Information received :")
print(s.recv(1024))

while True:
    msg = input("Enter information to send to server : ")
    s.send(msg.encode())
