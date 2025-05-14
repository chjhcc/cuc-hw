#导入需要的模块
import pygame, sys
from pygame.locals import *
from math import pi
#初始化pygame
pygame.init()
#设置窗口的大小，单位为像素
screen = pygame.display.set_mode((400,300))
#设置窗口标题
pygame.display.set_caption('Drawing')
 #定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# 设置背景颜色
screen.fill(WHITE)

pygame.draw.circle(screen,BLACK,(200,150),30,width=2)
pygame.draw.rect(screen,RED,[387,287,13,13],width=0)
pygame.draw.circle(screen,RED,(8,287),8,width=0)

#程序主循环
while True:
#获取事件
    for event in pygame.event.get():
    #判断事件是否为退出事件
        if event.type == QUIT:
            pygame.quit()				#退出pygame
            sys.exit()   				#退出系统
    pygame.display.update()				#绘制屏幕内容