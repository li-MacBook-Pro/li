def 奇数输出并求和():
    str1=input('请输入整数,请用空格隔开:')
    str1=str1.split()
    list2=[int(i) for i in str1 ]
    print(list2)
    def Number3__sum(parameter1):
        list3 = [x for x in list2 if x % 2 != 0]
        print(list3)
        sum1 = 0
        for i in range(len(list3)):
            sum1 += list3[i]
        print(sum1)
    Number3__sum(list2)
奇数输出并求和()


import random
Stock=[]
for i in range(6):
    Stock.append(random.randint(1,100))
print(Stock)
def Number1(parameter):
    print([x for x in Stock if x % 2 != 0 ])
Number1(Stock)


import random
Stock=[random.randint(1,10) for i in range(6) ]
print(Stock)
def Number1__sum(parameter):
    list1=[x for x in Stock if x % 2 != 0 ]
    print(list1)
    sum=0
    for i in range(len(list1)):
        sum+=list1[i]
    print(sum)
Number1__sum(Stock)

def 查看单个整数的奇偶():
    number = input("Enter a number, and I'll tell you if it's even or odd: ")
    number = int(number)
    if number % 2 == 0:
        print("\nThe number " + str(number) + " is even.")
    else:
        print("\nThe number " + str(number) + " is odd.")
查看单个整数的奇偶()