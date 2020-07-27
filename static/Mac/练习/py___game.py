import sys,pygame
# from settings
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()# 初始化背景，让pygame正确工作
    screen=pygame.display.set_mode((1200,800))# 显示窗口，游戏元素
    pygame.display.set_caption("Alien Invasion")
    bg_color=(230,230,230)# 设置背景颜色
    while True:# 开始游戏主循环
        for event in pygame.event.get():# 监视键盘和鼠标事件
            if event.type==pygame.QUIT:
                sys.exit()# 退出游戏
        screen.fill(bg_color)# 每次循环时都重新绘制屏幕
        pygame.display.flip()# 让绘制的屏幕可见
run_game()