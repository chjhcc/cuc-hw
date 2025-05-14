#导入所需的模块 
import pygame, sys
#导入所有pygame.locals里的变量（比如下面大写的QUIT变量） 
from pygame.locals import *
#初始化pygame 
pygame.init()
#设置窗口的大小，单位为像素
screen = pygame.display.set_mode((1000, 600))
#创建一个背景图片
background = pygame.image.load("./微信图片_20231014222451.jpg")
#设置窗口标题
pygame.display.set_caption('Hello World')
#程序主循环 
while True:
    screen.blit(background, (100,50))			#把背景复制到窗口的(0,0)处开始贴进去
    #获取事件
    for event in pygame.event.get():
    #判断事件是否为退出事件
        if event.type == QUIT:
            pygame.quit()				#退出pygame
            sys.exit()					#退出系统
    pygame.display.update() 			#绘制屏幕内容
