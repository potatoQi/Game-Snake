import pygame, random
import globaler

class Point():
	x, y = 0, 0
	def __init__(self, xx, yy):
		self.x = xx
		self.y = yy
	def copy(self):
		return Point(self.x, self.y)

pygame.init()
Right = globaler.get("Right")
Down = globaler.get("Down")
Colbak = (154, 255, 154)
Brown = (139, 105, 20)
Red = (205, 85, 85)
Orange = (255, 127, 0)
Yellow = (255, 255, 0)
Green = (34, 139, 34)
Blue = (0, 0, 255)
Qing = (0, 205, 102)
Purple = (148, 0, 211)
Black = (0, 0, 0)
display = pygame.display
screen = display.set_mode([Right, Down])
draw = pygame.draw

def rectT(point, col, size=10):
	draw.rect(screen, col, (point.x, point.y, size, size))

def rect():
	head = globaler.get("head")
	food = globaler.get("food")
	snake = globaler.get("snake")
	draw.rect(screen, Colbak, (0, 0, Right, Down))
	rectT(head, Red)
	rectT(food, Brown)
	tim = 0
	for body in snake:
		tim = tim + 1
		if tim <= 9: rectT(body, Red)
		elif tim <= 20: rectT(body, Orange)
		elif tim <= 30: rectT(body, Yellow)
		elif tim <= 40: rectT(body, Green)
		elif tim <= 50: rectT(body, Blue)
		elif tim <= 60: rectT(body, Qing)
		elif tim <= 70: rectT(body, Purple)
		if tim == 70: tim = 0
	display.update()

def move():
	dir = globaler.get("dir")
	head = globaler.get("head")
	add = globaler.get("add")
	if dir == 'left': head.x -= add
	if dir == 'right': head.x += add
	if dir == 'up': head.y -= add
	if dir == 'down': head.y += add
	head.x = int(head.x)
	head.y = int(head.y)
	globaler.upd("dir", dir)
	globaler.upd("head", head)

def getFood():
	snake = globaler.get("snake")
	head = globaler.get("head")
	while 1:
		tmp = Point(random.randint(10, Right - 20), random.randint(10, Down - 20))
		tag = 0
		if tmp == head: continue
		for body in snake:
			if tmp == body:
				tag = 1
				break
		if not tag: break
	return tmp

def eat():
	food = globaler.get("food")
	head = globaler.get("head")
	snake = globaler.get("snake")
	mark = globaler.get("mark")
	dir = globaler.get("dir")
	flag = abs(head.y - food.y) <= 4 and abs(head.x - food.x) <= 4
	if flag:
		mark += 1
		snake.append(food.copy())
		food = getFood()
	else:
		snake.insert(0, head.copy())
		snake.pop()
	globaler.upd("food", food)
	globaler.upd("head", head)
	globaler.upd("snake", snake)
	globaler.upd("mark", mark)

def dead():
	head = globaler.get("head")
	snake = globaler.get("snake")
	dead = 0
	if head.x < 0 or head.y < 0 or head.x >= Right or head.y >= Down: dead = 1
	for body in snake:
		if head.x == body.x and head.y == body.y:
			dead = 1
			break
	if dead: return 1
	return 0