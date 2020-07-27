import sys
import cfg
import pygame
import random
from pygame.locals import *


'''滑雪者类'''
@@ -18,9 +18,9 @@ def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# 滑雪者的朝向(-2到2)
		self.direction = 0
		self.imgs = ["./images/skier_forward.png", "./images/skier_right1.png", "./images/skier_right2.png", "./images/skier_left2.png", "./images/skier_left1.png"]
		self.person = pygame.image.load(self.imgs[self.direction])
		self.rect = self.person.get_rect()
		self.imagepaths = cfg.SKIER_IMAGE_PATHS[:-1]
		self.image = pygame.image.load(self.imagepaths[self.direction])
		self.rect = self.image.get_rect()
		self.rect.center = [320, 100]
		self.speed = [self.direction, 6-abs(self.direction)*2]
	'''改变滑雪者的朝向. 负数为向左，正数为向右，0为向前'''

@@ -29,8 +29,8 @@ def turn(self, num):
		self.direction = max(-2, self.direction)
		self.direction = min(2, self.direction)
		center = self.rect.center
		self.person = pygame.image.load(self.imgs[self.direction])
		self.rect = self.person.get_rect()
		self.image = pygame.image.load(self.imagepaths[self.direction])
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.speed = [self.direction, 6-abs(self.direction)*2]
		return self.speed
@@ -39,6 +39,13 @@ def move(self):
		self.rect.centerx += self.speed[0]
		self.rect.centerx = max(20, self.rect.centerx)
		self.rect.centerx = min(620, self.rect.centerx)
	'''设置为摔倒状态'''
	def setFall(self):
		self.image = pygame.image.load(cfg.SKIER_IMAGE_PATHS[-1])
	'''设置为站立状态'''
	def setForward(self):
		self.direction = 0
		self.image = pygame.image.load(self.imagepaths[self.direction])



@@ -65,7 +72,7 @@ def move(self, num):

'''创建障碍物'''
def create_obstacles(s, e, num=10):
def createObstacles(s, e, num=10):
	obstacles = pygame.sprite.Group()
	locations = []
	for i in range(num):
@@ -74,8 +81,8 @@ def create_obstacles(s, e, num=10):
		location  = [col*64+20, row*64+20]
		if location not in locations:
			locations.append(location)
			attribute = random.choice(["tree", "flag"])
			img_path = './images/tree.png' if attribute=="tree" else './images/flag.png'
			attribute = random.choice(list(cfg.OBSTACLE_PATHS.keys()))
			img_path = cfg.OBSTACLE_PATHS[attribute]
			obstacle = ObstacleClass(img_path, location, attribute)
			obstacles.add(obstacle)
	return obstacles
@@ -92,110 +99,118 @@ def AddObstacles(obstacles0, obstacles1):


'''显示游戏开始界面'''
def Show_Start_Interface(Demo, width, height):
	Demo.fill((255, 255, 255))
	tfont = pygame.font.Font('./font/simkai.ttf', width//4)
	cfont = pygame.font.Font('./font/simkai.ttf', width//20)
def ShowStartInterface(screen, screensize):
	screen.fill((255, 255, 255))
	tfont = pygame.font.Font(cfg.FONTPATH, screensize[0]//5)
	cfont = pygame.font.Font(cfg.FONTPATH, screensize[0]//20)
	title = tfont.render(u'滑雪游戏', True, (255, 0, 0))
	content = cfont.render(u'按任意键开始游戏', True, (0, 0, 255))
	trect = title.get_rect()
	trect.midtop = (width/2, height/10)
	trect.midtop = (screensize[0]/2, screensize[1]/5)
	crect = content.get_rect()
	crect.midtop = (width/2, height/2.2)
	Demo.blit(title, trect)
	Demo.blit(content, crect)
	pygame.display.update()
	crect.midtop = (screensize[0]/2, screensize[1]/2)
	screen.blit(title, trect)
	screen.blit(content, crect)
while True:
		for event in pygame.event.get():
			if event.type == QUIT:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				return
		pygame.display.update()


'''显示分数'''
def showScore(screen, score, pos=(10, 10)):
	font = pygame.font.Font(cfg.FONTPATH, 30)
	score_text = font.render("Score: %s" % score, True, (0, 0, 0))
	screen.blit(score_text, pos)


'''更新当前帧的游戏画面'''
def updateFrame(screen, obstacles, skier, score):
	screen.fill((255, 255, 255))
	obstacles.draw(screen)
	screen.blit(skier.image, skier.rect)
	showScore(screen, score)
	pygame.display.update()




'''主程序'''
def main():
	# 初始化
	# 游戏初始化
	pygame.init()
	# 声音
	pygame.mixer.init()
	pygame.mixer.music.load("./music/bg_music.mp3")
	pygame.mixer.music.load(cfg.BGMPATH)
	pygame.mixer.music.set_volume(0.4)
	pygame.mixer.music.play(-1)
	# 屏幕
	screen = pygame.display.set_mode([640, 640])
	pygame.display.set_caption('滑雪游戏-公众号:Charles的皮卡丘')
	# 主频
	clock = pygame.time.Clock()
	# 滑雪者
	# 设置屏幕
	screen = pygame.display.set_mode(cfg.SCREENSIZE)
	pygame.display.set_caption('滑雪游戏 —— 微信公众号:Charles的皮卡丘')
	# 游戏开始界面
	ShowStartInterface(screen, cfg.SCREENSIZE)
	# 实例化游戏精灵
	# --滑雪者
	skier = SkierClass()
	# 记录滑雪的距离
	distance = 0
	# 创建障碍物
	obstacles0 = create_obstacles(20, 29)
	obstacles1 = create_obstacles(10, 19)
	# --创建障碍物
	obstacles0 = createObstacles(20, 29)
	obstacles1 = createObstacles(10, 19)
	obstaclesflag = 0
	obstacles = AddObstacles(obstacles0, obstacles1)
    # 分数
	font = pygame.font.Font(None, 50)
	# 游戏clock
	clock = pygame.time.Clock()
	# 记录滑雪的距离
	distance = 0
	# 记录当前的分数
	score = 0
	score_text = font.render("Score: "+str(score), 1, (0, 0, 0))
	# 速度
	# 记录当前的速度
	speed = [0, 6]
	Show_Start_Interface(screen, 640, 640)
	# 更新屏幕
	def update():
		screen.fill([255, 255, 255])
		pygame.display.update(obstacles.draw(screen))
		screen.blit(skier.person, skier.rect)
		screen.blit(score_text, [10, 10])
		pygame.display.flip()
	# 主循环
# 游戏主循环
	while True:
		# 左右键控制人物方向
		# --事件捕获
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					speed = skier.turn(-1)
				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					speed = skier.turn(1)
		# --更新当前游戏帧的数据
		skier.move()
		distance += speed[1]
		if distance >= 640 and obstaclesflag == 0:
			obstaclesflag = 1
			obstacles0 = create_obstacles(20, 29)
			obstacles0 = createObstacles(20, 29)
			obstacles = AddObstacles(obstacles0, obstacles1)
		if distance >= 1280 and obstaclesflag == 1:
			obstaclesflag = 0
			distance -= 1280
			for obstacle in obstacles0:
				obstacle.location[1] = obstacle.location[1] - 1280
			obstacles1 = create_obstacles(10, 19)
			obstacles1 = createObstacles(10, 19)
			obstacles = AddObstacles(obstacles0, obstacles1)
		# 用于碰撞检测
		for obstacle in obstacles:
			obstacle.move(distance)
# 碰撞检测
		is_hit = pygame.sprite.spritecollide(skier, obstacles, False)
		if is_hit:
			if is_hit[0].attribute == "tree" and not is_hit[0].passed:
		# --碰撞检测
		hitted_obstacles = pygame.sprite.spritecollide(skier, obstacles, False)
		if hitted_obstacles:
			if hitted_obstacles[0].attribute == "tree" and not hitted_obstacles[0].passed:
				score -= 50
				skier.person = pygame.image.load("./images/skier_fall.png")
				update()
				# 摔倒后暂停一会再站起来
				skier.setFall()
				updateFrame(screen, obstacles, skier, score)
				pygame.time.delay(1000)
				skier.person = pygame.image.load("./images/skier_forward.png")
				skier.direction = 0
				skier.setForward()
				speed = [0, 6]
				is_hit[0].passed = True
			elif is_hit[0].attribute == "flag" and not is_hit[0].passed:
				hitted_obstacles[0].passed = True
			elif hitted_obstacles[0].attribute == "flag" and not hitted_obstacles[0].passed:
				score += 10
				obstacles.remove(is_hit[0])
		score_text = font.render("Score: "+str(score), 1, (0, 0, 0))
		update()
		clock.tick(40)
				obstacles.remove(hitted_obstacles[0])
		# --更新屏幕
		updateFrame(screen, obstacles, skier, score)
		clock.tick(cfg.FPS)
'''配置文件'''
import os


'''FPS'''
FPS = 40
'''游戏屏幕大小'''
SCREENSIZE = (640, 640)
'''图片路径'''
SKIER_IMAGE_PATHS = [os.path.join(os.getcwd(), 'resources/images/skier_forward.png'),
					 os.path.join(os.getcwd(), 'resources/images/skier_right1.png'),
					 os.path.join(os.getcwd(), 'resources/images/skier_right2.png'),
					 os.path.join(os.getcwd(), 'resources/images/skier_left2.png'),
					 os.path.join(os.getcwd(), 'resources/images/skier_left1.png'),
					 os.path.join(os.getcwd(), 'resources/images/skier_fall.png')]
OBSTACLE_PATHS = {
					'tree': os.path.join(os.getcwd(), 'resources/images/tree.png'),
					'flag': os.path.join(os.getcwd(), 'resources/images/flag.png')
				}
'''背景音乐路径'''
BGMPATH = os.path.join(os.getcwd(), 'resources/music/bgm.mp3')
'''字体路径'''
FONTPATH = os.path.join(os.getcwd(), 'resources/font/FZSTK.TTF')