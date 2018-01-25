#-*- coding: cp936 -*-
import pygame
import random
from sys import exit

pygame.init()
scn = pygame.display.set_mode((800, 600),0, 32)
pygame.display.set_caption("大吉大利，今晚吃鸡！！！")
bgpic = pygame.image.load("bg.jpg").convert()
plane = pygame.image.load("plane2.jpg").convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    scn.blit(bgpic, (0,0))

    x, y = pygame.mouse.get_pos()
    #获取鼠标位置
    x -= plane.get_width()/2
    y -= plane.get_height()/2
    #飞机出现位置
    scn.blit(plane, (x,y))

    pygame.display.update()