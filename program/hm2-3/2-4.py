#导入需要的模块
import pygame, sys
from pygame.locals import *
#初始化pygame
pygame.init()
# 设置帧率（屏幕每秒刷新的次数）
FPS = 30
#获得pygame的时钟
fpsClock = pygame.time.Clock()
#设置窗口大小
screen = pygame.display.set_mode((500, 400), 0, 32)
#设置标题
pygame.display.set_caption('Animation')
#定义颜色
WHITE = (255, 255, 255)
#加载一张图片
img = pygame.image.load('./pic.png')
#初始化图片的位置
imgx = 10
imgy = 10

#程序主循环
while True:
    #每次都要重新绘制背景白色
    screen.fill(WHITE)
    #判断移动的方向，并对相应的坐标做加减
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if(event.key==K_UP):
                print("上")
                imgy -= 5
            if(event.key==K_DOWN):
                print("下")
                imgy += 5
            if(event.key==K_LEFT):
                print("左")
                imgx -= 5
            if(event.key==K_RIGHT):
                print("右")
                imgx += 5
            #按下键盘的Esc键退出
            if(event.key==K_ESCAPE):
                #退出pygame
                pygame.quit()
                #退出系统
                sys.exit()

    #该方法将用于图片绘制到相应的坐标中
    screen.blit(img, (imgx, imgy))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #刷新屏幕
    pygame.display.update()
    #设置pygame时钟的间隔时间
    fpsClock.tick(FPS)