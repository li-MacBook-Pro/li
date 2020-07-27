import socket


host = '127.0.0.1'
port = 8081
# tcp socket
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 端口复用
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.connect((host, port))

sock.send(b'hello world tcp server')

data = sock.recv(1024)

print(data)

sock.close()