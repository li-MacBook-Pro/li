import socket


host = '127.0.0.1'
port = 8081

# tcp socket。socket:本质上是网络连接的抽象，物理连接-->类似文件的对象
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 端口复用
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind
sock.bind((host, port))

# 设置监听
sock.listen(128)

print('tcp 服务器监听在：', host, port)

new_sock, addr = sock.accept()
print('新链接地址：', addr)

recv_data = new_sock.recv(1024) # 收

print(recv_data)

new_sock.send(b'this is a tcp server') # 发

new_sock.close()
