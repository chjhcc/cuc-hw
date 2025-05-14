# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time
import random

# 子弹类
class Bullet(object):
    def __init__(self, screen_temp, x, y):  
        self.x = x + 40  
        self.y = y - 20  
        self.screen = screen_temp  
        self.image = pygame.image.load("./bullet.png")

    def display(self):  
        self.screen.blit(self.image, (self.x, self.y))  

    def move(self): 
        self.y -= 10  

    def judge(self):    
        if self.y < 0:   
            return True 
        else:
            return False 

# 飞机类
class Aircraft_obj(object):
    def __init__(self, screen_temp):   
        self.x = 190    
        self.y = 708    
        self.screen = screen_temp   
        self.image = pygame.image.load("./hero1.png")
        self.bullet_list = [] 
        self.bullet_count = 5  

    def display(self):  
        self.screen.blit(self.image, (self.x, self.y))  
        for bullet in self.bullet_list:
            bullet.display()    
            bullet.move()   
            if bullet.judge():
                self.bullet_list.remove(bullet) 

    def move_left(self):    
        if self.x < 10:     
            pass            
        else:
            self.x -= 10    

    def move_right(self):   
        if self.x > 1200 - 100 - 10: 
            pass            
        else:               
            self.x += 10    

    def move_up(self):
        if self.y < 400:
            pass
        else:
            self.y -= 10

    def move_down(self):
        if self.y > 700:
            pass
        else:
            self.y += 10

    def fire(self): 
        if self.bullet_count > 0: 
            self.bullet_list.append(Bullet(self.screen, self.x, self.y)) 
            self.bullet_count -= 1  
        else:
            print("你的子弹已耗尽")
            

# 敌机类
class EnemyPlane(object):
    def __init__(self, screen_temp):   
        self.x = random.randint(0, 1200 - 150)  
        self.y = -150  
        self.screen = screen_temp   
        self.image = pygame.image.load("./enemy0.png")
        self.direction = random.choice(["right", "left"])   
        self.hit = False 
        self.bomb_lists = [] 
        self.__crate_images() 
        self.image_num = 0
        self.image_index = 0
        self.speed = random.randint(1, 3)

    def __crate_images(self):   
        self.bomb_lists.append(pygame.image.load("./enemy0_down1.png"))
        self.bomb_lists.append(pygame.image.load("./enemy0_down2.png"))
        self.bomb_lists.append(pygame.image.load("./enemy0_down3.png"))
        self.bomb_lists.append(pygame.image.load("./enemy0_down4.png"))

    def blast(self, x1, x2, y):
        if ((x1 >= self.x and x2 <= self.x + 150) or x2 == self.x or x1 == self.x + 150) and y < 150:
            self.hit = True

    def display(self):  
        if self.hit == True:    
            self.screen.blit(self.bomb_lists[self.image_index], (self.x, self.y))
            self.image_num += 1   
            if self.image_num == 7: 
                self.image_num = 0    
                self.image_index += 1 
            if self.image_index > 3:  
                print("恭喜，你赢了！")
                time.sleep(1)       
                exit()  
        else:   
            self.screen.blit(self.image,(self.x, self.y))

    def move(self): 
        if self.hit == True: 
            pass
        else:
            if self.direction == "right":   
                self.x += self.speed    
            elif self.direction == "left":    
                self.x -= self.speed   

            self.y += self.speed  # 垂直方向移动

            if self.x > 1200:  
                self.x = -150 
            elif self.x < -150:     
                self.x = 1200   
            if self.y > 852:  # 重置敌机位置
                self.y = -150
                self.x = random.randint(0, 1200 - 150)
                self.direction = random.choice(["right", "left"])
                self.speed = random.randint(1, 3)

def key_control(aircraft_temp):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")   
            exit()  
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')   
                aircraft_temp.move_left()   
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')  
                aircraft_temp.move_right()  
            elif event.key == K_w or event.key == K_UP:
                print("up")
                aircraft_temp.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                print("down")
                aircraft_temp.move_down()      
            elif event.key == K_SPACE:
                print('space')  
                aircraft_temp.fire()    

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200,852),0,32)
    background = pygame.image.load("./background.png")
    aircraft = Aircraft_obj(screen)

    enemies = []
    clock = pygame.time.Clock()
    enemy_frequency = 0

    while True:
        screen.blit(background, (0,0))  
        aircraft.display()  

        if enemy_frequency % 60 == 0:
            enemy = EnemyPlane(screen)
            enemies.append(enemy)

        for enemy in enemies:
            enemy.display()
            enemy.move()

        for bullet in aircraft.bullet_list: 
            x1 = bullet.x       
            x2 = bullet.x + 150  
            y1 = bullet.y       
            for enemy in enemies:
                enemy.blast(x1, x2, y1)    

        for enemy in enemies:
            if enemy.hit == True:
                break
            if (aircraft.x < enemy.x + 100 and aircraft.x + 100 > enemy.x and
                aircraft.y < enemy.y + 100 and aircraft.y + 100 > enemy.y):
                print("很遗憾，你输了！")
                time.sleep(1)       
                exit()  

        pygame.display.update() 
        key_control(aircraft)   
        time.sleep(0.01)    
        enemy_frequency += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")   
                exit()  

        clock.tick(70)  

main()

