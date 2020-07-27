def subString(strs):
    result=strs[0]
    for i in range(1,len(strs)):
        while (strs[i].startswith(result)==False):
            result=result[0:len(result)-1]
            if len(result)==0:
                return "无公共前缀"
    return result
try:
    while 1:
        a = input('请输入字符串，用空格隔开：')
        a = a.split()
        result = subString(a)
        print(result)
except:
    pass


# def longstCommonPrefix(*strs):
#     import os
#     return os.path.commonprefix(strs)
# print(longstCommonPrefix('abcacc','abvasd','abaaa'))



# while True:
#     try:
#         for i in range(len(n)):
#             if n[i][j]!=n