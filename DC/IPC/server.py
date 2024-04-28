import socket
import socketserver

s = socket.socket()

s.bind(('', 1000))
s.listen(5)
print("Listening at port 1000")
while True:
    c, addr = s.accept()
    print("Client connected!")
    print(addr)
    print("Sending information")
    c.send('Hello Client!'.encode())
    print("Information sent")

