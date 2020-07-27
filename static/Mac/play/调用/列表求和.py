a=[1,2,3,[4,5,6,[7,8,9],(10,11,12)],13,14]
sum_list=[]
def find_element(n):
    for i in n:
        try:
            for j in i:
                find_element(i)
                break
        except Exception:
            sum_list.append(i)
find_element(a)
print(sum_list)
def sum__list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum__list(sum_list))
b=sum_list[0]
print(type(b))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# def 简单的函数(b):
#     b = sum_list[0]
#     for i in range(len(sum_list)):
#         sum_list.append(b)
#         sum_list.pop(0)
#         b+=10
# 简单的函数(sum_list)
# print(sum_list)

def func(n):
    for i in range(len(n)):
        try:
            if n[i]+10 == n[i + 1] :
                continue
            else:
                n[i+1] = n[i]+10
        except:
            pass
    return n

print(func(sum_list))


# def func(n):
#     for i in range(1,len(n)):
#         if n[i]==(n[i-1]-10):
#             continue
#         else:
#             n[i]=n[i-1]-10
#     return n
#
# print(func(sum_list))

def s(n):
    return ([(n[0]-i*10) for i in range(len(n))])
print(s(sum_list))