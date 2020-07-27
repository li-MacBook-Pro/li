def Hat(func):
    def a():
        print('~~~~~~~~~欢迎光临曾同学卖报摊~~~~~~~~~')
        money=float(input('请输入你现有的钱数：').strip())
        num=int(input('请输入需要购买的报纸数量（温馨提示，要输入整份报纸的数量):').strip())
        曾同学=func(money,num)
        if 曾同学>0:
            if money == 0:
                print('没钱还买什么报纸，是喜欢读报纸吗？可以给你一份看着')
            if num>1:
                print('你需要的{}份报纸共计需要{}元CHN，您的钱不够哟。可以考虑一下少购买几份报纸。'.format(num,cost))
            elif num==1 and money!=0:
                print('你需要的{}份报纸共计需要{}元CHN，您的钱不够哟。那这样吧，就这些钱卖给你了。'.format(num,cost))
        elif 曾同学<=0:
            if cost == 0:
                if num == 0:
                    print('你怕是来砸场子的!!!')
            else:
                print('这是您要的{}份报纸，收您{}元CHN，找您{}元CHN，欢迎下次光临！'.format(num,cost,-曾同学))
    return a
@Hat
def newspaper(money,num):
    global price, cost
    price = 0.5
    if num < 5:
        cost = num * price
    elif num >= 5 and num < 10:
        cost = num * price * 0.9
    elif num >= 10:
        cost = num * price * 0.8
    return cost-money
newspaper()