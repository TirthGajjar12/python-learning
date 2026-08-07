#ch-6_Network and socket IO

#server side here 

import socket


server = socket.socket()  
server.bind(('localhost',5555))

server.listen(5)


conn, addr = server.accept()
print(f'connected from {addr}')

data = conn.recv(1024)
print(f"data recived{data.decode()}")

conn.send(b"got your message!")
conn.close()