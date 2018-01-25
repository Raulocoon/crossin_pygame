import random
import pygame
from sys import exit

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load("bullet.jpg").convert_alpha()
        self.active = False

    def restart(self):
        #重置子弹位置
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.x = mouse_x - self.image.get_width() / 2
        self.y = mouse_y - self.image.get_height() / 2
        #激活子弹
        self.active = True



    def move(self):
        if self.active:
            #向上移动
            self.y -= 2

        if self.y < 0:
            self.active = False

class Enemy:
    def restart(self):
        #重置敌机位置
        self.x = random.randint(0, 600)
        self.y = random.randint(-200, -50)
        self.speed = random.random() + 0.1

    def __init__(self):
        #初始化
        self.restart()
        self.image = pygame.image.load("enemy.jpg").convert_alpha()

    def move(self):
        if self.y < 800:
            # 向下移动
            self.y += self.speed
        else:
            self.restart()

#命中敌机
def checkHit(enemy, bullet):
    #子弹在敌机范围内
    if(bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (
                    bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
        #重置敌机
        enemy.restart()
        #重置子弹
        bullet.active = False

#命中飞机
def checkCrash(enemy, plane):
    if(plane.x + 0.7*plane.image.get_width() > enemy.x) and (
                    plane.x + 0.3*plane.image.get_width() < enemy.x + enemy.image.get_width()) and (
                    plane.y + 0.7*plane.image.get_height() >enemy.y) and (
                    plane.y + 0.3*plane.image.get_height() < enemy.y + enemy.image.get_width()):
        return True
    return False

pygame.init()
scn = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("大吉大利，今晚吃鸡")
bgpic = pygame.image.load('bg.jpg').convert()
plane = pygame.image.load("plane2.jpg").convert_alpha()
#多发子弹
bullets = []
for i in range(5):
    bullets.append(Bullet())

#多架敌机
enemies = []
for i in range(5):
    enemies.append(Enemy())

game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    scn.blit(bgpic, (0, 0))


    for b in bullets:
        # 处于激活状态的子弹，移动位置并绘制
        if b.active:
            for e in enemies:
                checkHit(e, b)

            b.move()
            scn.blit(b.image, (b.x, b.y))
        else:
            b.restart()

    #敌机运动
    for e in enemies:
        e.move()
        scn.blit(e.image, (e.x, e.y))

    x, y = pygame.mouse.get_pos()
    x -= plane.get_width()/2
    y -= plane.get_height()/2
    scn.blit(plane, (x, y))
    pygame.display.update()
