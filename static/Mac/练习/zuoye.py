# author：xinxinzhang
n = 12  # 凑11元
total = [i for i in range(n)]
v = [1, 3, 5]

for i in range(1, n):
    for j in v:
        if j <= i and (total[i - j] + 1) < total[i]:  # 选比不选好
            total[i] = total[i - j] + 1
print(total[-1])