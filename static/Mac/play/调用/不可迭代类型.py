#a=[1,2,3,[4,5,6,[7,8,9],(10,11,12)],13,14]
# #第一种
# s=set()
# def find_element(n):
#     for i in n:
#         try:
#             for j in i:
#                 find_element(i)
#         except Exception:
#             s.add(i)
# find_element(a)
# print(s)
#第二种
# def find_element(n):
#     for i in n:
#         try:
#             for j in i:
#                 find_element(i)
#                 break
#         except Exception:
#             print(i)
# find_element(a)
# #第三种
def print_list(lst):
    for i in lst:
        print('!!!!i!!!!')
        print(i)
        try:
            for j in print_list(i):
                print('~~~j~~~')
                print(i)
                print(j)
                yield j

        except Exception:
            print('ii')
            print(i)
            yield i


a = [1,2,3,[4,5,6],[7,8,9],(10,11,12,(13,14,15))]
for i in print_list(a):
    print('nnnnnnnnnnnnnn')
    print(i)
    print('!!!!~~~~~~~~~~~~~~~~~~~~~')