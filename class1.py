# -*- coding: UTF-8 -*-
#导入pygame库
import pygame
#退出函数
from sys import exit
import random

#print(dir(pygame))
#初始化pygame
pygame.init()
#创建一个界面
screen = pygame.display.set_mode((600, 170), 0, 32)
#设置标题
pygame.display.set_caption("Hello World!")
#加载图像
house0 = pygame.image.load("game.jpg").convert()
house1 = pygame.image.load("house1.jpg").convert()
house2 = pygame.image.load("house2.jpg").convert()
house3 = pygame.image.load("house3.jpg").convert()
backjpg = [house0, house1, house2, house3]
background = house0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #鼠标按下随机更改房子图片背景
            background = random.choice(backjpg)

    #设置背景
    screen.blit(background, (0, 0))
    #刷新
    pygame.display.update()


