class Solution(object):
    def reverse(self, x):
        ans = 0
        flag = 1
        if x <0:
            x = -x
            flag = -flag

        while x  != 0:
            cur = x % 10
            ans = ans*10 + cur
            x //= 10
        return ans*flag if -2**31 <ans*flag <2**31 else 0
'''
''''''
def reverse_force(x: int) -> int:
    if -10 < x < 10:
        return x
    str_x = str(x)
    if str_x[0] != "-":
        str_x = str_x[::-1]
        x = int(str_x)
    else:
        str_x = str_x[:0:-1]
        x = int(str_x)
        x = -x
    return x if -2147483648 < x < 2147483647 else 0
print(reverse_force(-120))
''''''
'''
def reverse_better(x: int) -> int:
    y, res = abs(x), 0
    # 则其数值范围为 [−2^31,  2^31 − 1]
    boundry = (1 << 31) - 1 if x > 0 else 1 << 31
    while y != 0:
        res = res * 10 + y % 10
        if res > boundry:
            return 0
        y //= 10
    return res if x > 0 else -res
'''
''''''
def bb(a):
    a=str(a)
    k=0
    for i in a[::-1]:
        if i != '0':
            continue
        else:
            k+=1
    a=a[:len(a)-k]
    if a[0]=='-':
        a=a[0]+a[:0:-1]
    else:
        a=a[::-1]
    a=eval(a)
    print(a)
bb(102)'''

print(reverse_better(0))
print(reverse_better(10))
print(reverse_better(-10))
print(reverse_better(-102))
print(reverse_better(102))
