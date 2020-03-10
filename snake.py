import pygame, random, time
from pygame.locals import *
import globaler

class Point():
	x, y = 0, 0
	def __init__(self, xx, yy):
		self.x = xx
		self.y = yy
	def copy(self):
		return Point(self.x, self.y)

globaler.init()
Colbak = (154, 255, 154)
White = (255, 255, 255)
globaler.set("Right", 600)
globaler.set("Down", 600)
Right = globaler.get("Right")
Down = globaler.get("Down")
globaler.set("head", Point(Right / 2 - 10, Down / 2 - 10))
globaler.set("add", 5)
globaler.set("dir", 'left')
globaler.set("snake", [])
globaler.set("food", Point(100, 100))
globaler.set("mark", 0)

# 当前文件变量
pygame.init()
sleepTime = 30  # 最大帧率
display = pygame.display
event = pygame.event
clock = pygame.time.Clock()
draw = pygame.draw
screen = display.set_mode([Right, Down])
display.set_caption("Snake!")
display.set_icon(pygame.image.load("title.ico"))
dir = globaler.get("dir")

def pause():
	while 1:
		j = event.wait()
		if j.type == KEYDOWN and j.key == K_SPACE:
			op = 0
			break

import talk, fun
talk.open()
running = 1

while running:
	# 操作
	clock.tick(sleepTime)
	for i in event.get():
		if i.type == KEYDOWN:
			if i.key == K_ESCAPE: running = 0
			if i.key == K_w and (dir == 'left' or dir == 'right'): dir = 'up'
			if i.key == K_s and (dir == 'left' or dir == 'right'): dir = 'down'
			if i.key == K_a and (dir == 'up' or dir == 'down'): dir = 'left'
			if i.key == K_d and (dir == 'up' or dir == 'down'): dir = 'right'
			if i.key == K_RETURN: sleepTime = 60
			if i.key == K_SPACE: pause()
		elif i.type == KEYUP and i.key == K_RETURN:
			sleepTime = 30
	globaler.upd("dir", dir)
	# 吃食物
	fun.eat()
	# 移动
	fun.move()
	# 绘制
	fun.rect()
	# 判断死亡
	if fun.dead(): running = 0
talk.last()