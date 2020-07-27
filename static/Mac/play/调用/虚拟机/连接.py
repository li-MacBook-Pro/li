from socket import*
host = ''
bufferSize = 1024
port = 9876
addr = host, port
tcpServerSocket = socket(AF_INET, SOCK_STREAM)
tcpServerSocket.bind(addr)
tcpServerSocket.listen(2)
print('Server port:9876')
print('正在等待客户端连接')
while True:
    tcpClientSocket, addr = tcpServerSocket.accept()
    print('客户端已经连接','addr','=',addr)
    data = tcpClientSocket.revc(bufferSize)
    print(data.decode('utf-8'))
    tcpClientSocket.send('你好，同学。\n'.encode(encoding='utf-8'))
    tcpClientSocket.close()
tcpServerSocket.close()