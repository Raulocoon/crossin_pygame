import pygame
from sys import exit

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load("bullet.jpg").convert_alpha()

    def move(self):
        if self.y < 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.x = mouse_x - self.image.get_width()/2
            self.y = mouse_y - self.image.get_height()/2
        else:
            #子弹向上移动
            self.y -= 5

pygame.init()
scn = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("大吉大利，今晚吃鸡")
bgpic = pygame.image.load("bg.jpg").convert()
plane = pygame.image.load("plane2.jpg").convert_alpha()
bullet = Bullet()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    scn.blit(bgpic, (0,0))
    bullet.move()
    scn.blit(bullet.image, (bullet.x, bullet.y))
    x, y = pygame.mouse.get_pos()
    x -= plane.get_width()/2
    y -= plane.get_height()/2
    scn.blit(plane, (x, y))

    pygame.display.update()
