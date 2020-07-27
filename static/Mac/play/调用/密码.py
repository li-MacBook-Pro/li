def 密码(n):
    global 计次数
    计次数=0
    mima = 'xiaoming1995'
    for i in range(len(mima)):
        if chr(ord(n[i]) - 1) == mima[i]:
            continue
        elif n[i] == 'a':
            if chr(ord(n[i])+26)==mima[i]:
                continue
        elif '0' <= n[i] <= '9' and mima[i] == n[i]:
            continue
        else:
            计次数+=1
            return '密码错误'
    print('密码正确')

while True:
    b=input('请输入十二位密码:')
    b=b.lower()
    try:
        if len(b) >= 12:
            密码(b)
        else:
            print('？？？')
        if 计次数 == 0:
            break
    except:
        pass

#利用字典{a:b,b:c.....z:a}
#遍历