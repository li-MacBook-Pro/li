# while 1:
#     try:
#         like=input()
#         list = [like.count(i) for i in like]
#         min_a = min(list)
#         print(''.join([i for (i, j) in zip(like, range(len(list))) if list[j] != min_a ]))
#     except:
#         break
#

n='abcabcab'
def cut__str(n):
    a={}
    for i in n :
        try:
            if a[i]:
                a[i] += 1
        except:
            a[i] = 1
    print(a)
    min_num = min(a.values())
    s=''
    for i in n:
        if a[i] !=  min_num:
            s += i
            print(s)
    return s
print(cut__str(n))


# while True:
#     try:
#         st = input()
#         letterlist = list(st)
#         letterdict = {}
#         for i in letterlist:
#              if i not in letterdict.keys():
#                 letterdict[i] = 1
#              else:
#                 letterdict[i] += 1
#         n = min(letterdict.values())   #求字典的value下的最小值，返回的是value值，
#         for i in st:
#             if n == letterdict[i]:
#                 letterlist.remove(i)
#         print(''.join(letterlist))
#     except:
#         pass




#coding=utf-8
# while True:
#     s=input().lower()
#     while len(s)>20:
#         s=input().lower()
#     d={}
#     #生成字典，key是输入的字符串中每个字符，value是每个字符在字符串中出现的次数
#     for ch in s:
#         d[ch]=s.count(ch)
#     #根据次数进行升序
#     values=[v for v in d.values()]
#     values.sort()
#     #字典中删除次数最少的项
#     item=[k for k,v in d.items() if v==values[0]]
#     for i in item:
#         del d[i]
#     #字符串中和字典中剩余字符相同的字符进行输出
#     keys=[k for k in d.keys()]
#     for ch in s:
#         if ch in keys:
#             print(ch,end='')
#     print()