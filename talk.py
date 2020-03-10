import pygame, time
import globaler

pygame.init()
display = pygame.display
font = pygame.font.SysFont("arial", 24)
Right = globaler.get("Right")
Down = globaler.get("Down")
screen = display.set_mode((Right, Down))
Colbak = (154, 255, 154)
Black = (0, 0, 0)

def output(word, x, y):
	obj = font.render(word, True, Black)
	xy = obj.get_rect()
	xy.center = (x, y)
	screen.blit(obj, xy)
	display.update()

def open():
	screen.fill(Colbak)
	output("Snake!", 300, 250)
	output("ZhouQixing(Error_666)", 300, 100)
	output("ESC, SPACE, RETURN", 300, 500)
	time.sleep(3)

def last():
	time.sleep(3)
	screen.fill(Colbak)
	output("Your mark:" + str(globaler.get("mark")), 300, 250)
	time.sleep(3)