import pygame
import random
from sys import exit

class Plane:
    def restart(self):
        self.x = 200
        self.y = 600

    def __init__(self):
        #x, y = pygame.mouse.get_pos()
        self.restart()
        self.image = pygame.image.load("plane2.jpg").convert_alpha()


    def move(self):
        x, y = pygame.mouse.get_pos()
        x -= self.image.get_width()/2
        y -= self.image.get_height()/2
        self.x = x
        self.y = y

class Bullet:
    def __init__(self):
        self.x = 0
        self.y = -1
        self.image = pygame.image.load("bullet.jpg").convert_alpha()
        self.active = False

    def move(self):
        if self.active:
            self.y -= 0.8
        if self.y < 0:
            self.active = False

    def restart(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.x = mouse_x - self.image.get_width()/2
        self.y = mouse_y - self.image.get_height()/2
        self.active = True

class Enemy:
    def restart(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(-200, -50)
        self.speed = random.random() + 0.1

    def __init__(self):
        self.restart()
        self.image = pygame.image.load("enemy.jpg").convert_alpha()

    def move(self):
        if self.y < 800:
            self.y += self.speed
        else:
            self.restart()

def check_hit(enemy, bullet):
    if(bullet.x > enemy.x and bullet.x < enemy.x + enemy.image.get_width()) and (
        bullet.y > enemy.y and bullet.y < enemy.y + enemy.image.get_height()):
        enemy.restart()
        bullet.active = False
        return True
    return False

def check_crash(enemy, plane):
    if(plane.x + 0.7*plane.image.get_width() > enemy.x) and (
        plane.x + 0.3*plane.image.get_width() < enemy.x + enemy.image.get_width()) and (
        plane.y + 0.7*plane.image.get_height() > enemy.y) and (
        plane.y + 0.3*plane.image.get_height() < enemy.y + enemy.image.get_height()):
        return True
    return False


pygame.init()
scn = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption("大吉大利，今晚吃鸡")
bgpic = pygame.image.load('bg.jpg').convert()

plane = Plane()
bullets = []
for i in range(10):
    bullets.append(Bullet())
count_b = len(bullets)
index_b = 0
interval_b = 0

#bullet = Bullet()
#enemy = Enemy()
enemies = []
for j in range(5):
    enemies.append(Enemy())

gameOver = False
score = 0
font = pygame.font.Font(None, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if gameOver and event.type == pygame.MOUSEBUTTONDOWN:
            plane.restart()
            for e in enemies:
                e.restart()
            for b in bullets:
                b.active = False

            score = 0
            gameOver = False

    scn.blit(bgpic, (0, 0))

    if not gameOver:
        interval_b -= 1
        if interval_b < 0:
            bullets[index_b].restart()
            interval_b = 200
            index_b = (index_b + 1) % count_b
        #bullet.move()
        #scn.blit(bullet.image, (bullet.x, bullet.y))
        for b in bullets:
            if b.active:
                for e in enemies:
                    if check_hit(e, b):
                        score += 100
                b.move()
                scn.blit(b.image, (b.x, b.y))

        #enemy.move()
        #scn.blit(enemy.image, (enemy.x, enemy.y))
        for e in enemies:
            if check_crash(e, plane):
                gameOver = True
            e.move()
            scn.blit(e.image, (e.x, e.y))

        plane.move()
        scn.blit(plane.image, (plane.x, plane.y))

        text = font.render("Score: %d" %score, 1, (0, 0, 0))
        scn.blit(text, (0, 0))
    else:
        text = font.render("Score: %d" %score, 1, (0, 0, 0))
        scn.blit(text, (350, 250))
        pass

    pygame.display.update()