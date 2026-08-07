#this is client side

import socket 

client = socket.socket()
client.connect(('localhost',5555))

client.send(b"hi,server its tirth")
replay = client.recv(1024)

print(f"server replied: {replay.decode()}")

client.close()

