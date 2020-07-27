from socket import *
import os
def responeHeaders(file,length):
    f = open(file,'r')
    headersText = f.read()
    headersText = headersText % length
    return headersText
def filePath(get):
    if get == '/':
        return '.' + os.sep + 'scratch1.html'
    else:
        paths = get.split('/')
        s = '.'
    for path in paths:
        if path.strip()!='':
            s = s + os.sep + path
    return  s
def main():
    host = ''
    bufferSize = 1024
    port = 9876
    addr = host,port
    tss = socket(AF_INET,SOCK_STREAM)
    tss.bind(addr)
    tss.listen(5)
    while True:
        print('正在等待客户的连接')
        tcs,addr = tss.accept()
        print('客户已经连接')
        data = tcs.recv(bufferSize)
        data = data.decode('utf-8')
        try:
            firstLine = data.split('\n')[0]
            path = firstLine.split(' ')[1]
            print(path)
            path = filePath(path)
            if os.path.exists(path):
                file = open(path,'rb')
                content = file.read()
                file.close()
            else:
                content = '<h1>Page Not Found</h1>'.encode(encoding = 'utf-8')
            print(content)
            rh = responeHeaders('responeHeaders.txt', len(content)) + '\r\n'
            tcs.send(rh.encode(encoding = 'utf-8') + content)
        except Exception as e:
            print(e)
        tcs.close()
    tss.close()

if __name__ == '__main__':
    main()
#http://localhost:9876/
#http://127.0.0.1:9876/