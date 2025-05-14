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
#初始化图片的移动方向
direction = 'right'

sound=pygame.mixer.Sound('./bird.wav')

#程序主循环
while True:
    #每次都要重新绘制背景白色
    screen.fill(WHITE)
    #判断移动的方向，并对相应的坐标做加减
    if direction == 'right':
        imgx += 5
        if imgx == 380:
            direction = 'down'
            sound.play()
    elif direction == 'down':
        imgy += 5
        if imgy == 300:
            direction = 'left'
            sound.play()
    elif direction == 'left':
        imgx -= 5
        if imgx == 10:
            direction = 'up'
            sound.play()
    elif direction == 'up':
        imgy -= 5
        if imgy == 10:
            direction = 'right'
            sound.play()
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