def 整数求和():
    a=input('输入一组整数，用空格隔开：')
    a=a.split()
    b=[]
    c=0
    for i in a:
        b.append(i)
        c+=int(i)
    print(c)
整数求和()