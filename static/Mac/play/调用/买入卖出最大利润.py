import random,copy
Stock=[]
for i in range(6):
    Stock.append(random.randint(1,10))
print(Stock)
Max__profit = -1
#买入点考虑
buy = 0
for i in range(len(Stock)):
    for j in range(i+1,len(Stock)):
        if Stock[j] - Stock[i] >Max__profit:
            Max__profit = Stock[j] - Stock[i]
            buy = i
            sell = j

print(Max__profit,buy+1,sell+1)

#卖出点考虑
min__cost = Stock[0]
for i in Stock:
    Max__profit = max(Max__profit, i - min__cost)
    min__cost = min(min__cost, i)
print(Max__profit)