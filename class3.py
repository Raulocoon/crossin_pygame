# -*- coding:cp936 -*-
import pygame
from sys import exit

pygame.init()
scn = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption("大吉大利，今晚吃鸡！")
bgpic = pygame.image.load("bg.jpg").convert()
plane = pygame.image.load("plane2.jpg").convert_alpha()
bullet = pygame.image.load("bullet.jpg").convert_alpha()
#子弹初始位置
bullet_x = 0
bullet_y = -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        scn.blit(bgpic,(0,0))
        plane_x, plane_y = pygame.mouse.get_pos()

        #设置为鼠标坐标
        if bullet_y < 0:
            bullet_x = plane_x - bullet.get_width()/2
            bullet_y = plane_y - bullet.get_height()/2
        else:
            bullet_y -= 5

        #子弹
        scn.blit(bullet, (bullet_x, bullet_y))

        plane_x -= plane.get_width()/2
        plane_y -= plane.get_height()/2
        scn.blit(plane, (plane_x, plane_y))

        pygame.display.update()


