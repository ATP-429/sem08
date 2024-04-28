import socket
import threading

s = socket.socket()

s.bind(('', 1000))
s.listen(5)
print("Listening at port 1000")

clients = {}
i = 0

def threaded_interact(client, id, addr):
    print(f"Client {id} address : {addr}")
    print("Sending information")
    client.send('Hello Client'.encode())
    print(f"Information sent to client {id}")
    while True:
        info = client.recv(1024)
        if info == 0:
            print(f"Connection with client {id} closed")
        else:
            print(f"Information received from client {id} :")
            print(info.decode())
    

while True:
    client, addr = s.accept()
    clients[i] = client
    print("Client {i} connected!")
    threading.Thread(target=threaded_interact, args=(clients[i], i, addr)).start()
    i += 1

