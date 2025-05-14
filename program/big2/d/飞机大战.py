# -*- coding:utf-8 -*-
import os
import random
import sys
import pandas as pd
from  openpyxl import load_workbook
import pygame  # 导入pygame模块
from pygame.locals import *  # 导入pygame.locals模块
import time  # 导入time模块

# 全局变量，用于存储历来最佳得分和最佳游戏时间
best_score = 0
best_time = 0


# 子弹类
class Bullet(object):
    def __init__(self, screen_temp, x, y):  # 构造方法 初始化子弹对象的属性
        self.x = x + 40  # 子弹起始X坐标
        self.y = y - 20  # 子弹起始Y坐标
        self.screen = screen_temp  # 窗口
        self.image = pygame.image.load("./bullet.png")  # 创建一个子弹图片

    def display(self):  # 显示子弹图片的方法
        self.screen.blit(self.image, (self.x, self.y))  # 将创建的子弹图片按设定的坐标贴到窗口中

    def move(self):  # 子弹移动方法
        self.y -= 10  # 子弹Y坐标自减10

    def judge(self):  # 判断子弹是否越界的方法
        if self.y < 0:  # 如果子弹的Y坐标小于0
            return True  # 返回true正确
        else:
            return False  # 返回false错误


# 飞机类
class Aircraft_obj(object):
    bullet_list = None

    def __init__(self, screen_temp):  # 构造方法 初始化飞机对象的属性
        self.x = 190  # 飞机起始X坐标
        self.y = 708  # 飞机起始Y坐标
        self.screen = screen_temp  # 窗口
        self.image = pygame.image.load("./hero1.png")  # 创建一个飞机图
        self.bullet_list = []  # 存储发射出去的子弹对象引用
        self.bullet_limit = 10  # 子弹限制数量
        self.bullet_count = 0  # 当前子弹数量

    def display(self):  # 显示飞机图片的方法（这里包括了显示子弹的图片）
        self.screen.blit(self.image, (self.x, self.y))  # 将创建的飞机图片按设定的坐标贴到窗口中

        # 显示飞机发射的所有子弹
        for bullet in self.bullet_list:
            bullet.display()  # 显示子弹
            bullet.move()  # 移动子弹
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)  # 将子弹从bullet_list中删除

    def move_left(self):  # 飞机左移方法
        if self.x < 10:  # X坐标小于10（移动距离）
            pass  # 不做任何事
        else:
            self.x -= 10  # X坐标自减少10

    def move_right(self):  # 飞机右移方法
        if self.x > 480 - 100 - 10:  # X坐标大于（窗口宽度-飞机宽度-移动距离）的值
            pass  # 不做任何事
        else:
            self.x += 10  # 坐标自增加10

    # 存储发射子弹的方法
    def fire(self):
        if self.bullet_count < self.bullet_limit:
            self.bullet_list.append(Bullet(self.screen, self.x, self.y))
            self.bullet_count += 1
        else:
            print("Bullet limit reached. Wait for replenishment.")

    def move_up(self):
        if self.y > 10:  # 确保飞机不会移出屏幕上方
            self.y -= 10  # Y坐标减少10

    def move_down(self):
        if self.y < 480 - 100:  # 减去飞机高度，确保飞机不会移出屏幕下方
            self.y += 10  # Y坐标增加10


class EnemyBullet(object):
    def __init__(self, screen_temp, x, y):  # 构造方法 初始化子弹对象的属性
        self.x = x + 40  # 子弹起始X坐标
        self.y = y - 20  # 子弹起始Y坐标
        self.screen = screen_temp  # 窗口
        self.image = pygame.image.load("./bullet.png")  # 创建一个子弹图片

    def display(self):  # 显示子弹图片的方法
        self.screen.blit(self.image, (self.x, self.y))  # 将创建的子弹图片按设定的坐标贴到窗口中

    def move(self):  # 子弹移动方法
        self.y += 10  # 子弹Y坐标自加10

    def judge(self):  # 判断子弹是否越界的方法
        if self.y > 0:  # 如果子弹的Y坐标小于0
            return True  # 返回true正确
        else:
            return False  # 返回false错误


# 敌机类
class EnemyPlane(object):
    def __init__(self, screen_temp):  # 构造方法 初始化敌机对象的属性
        self.x = 0  # 敌机的起始X坐标
        self.y = 0  # 敌机的起始Y坐标
        self.screen = screen_temp  # 窗口
        self.image = pygame.image.load("./enemy0.png")  # 创建一个敌机图片
        self.direction = "right"  # 用来存储飞机移动方向，默认向右移动
        self.bullet_to_remove = []
        # 爆炸效果用的属性
        self.hit = False  # 表示是否要爆炸
        self.bomb_lists = []  # 用来存储爆炸时需要的图片
        self.EnemyBullet_list = []  # 存储发射出去的敌机子弹对象引用
        self.EnemyBullet_interval = 0  # 发射子弹的时间间隔
        self.replenish_time = 5000  # 每5秒发射一次子弹
        self.__crate_images()  # 调用这个方法向bomb_lists中添加图片
        self.image_num = 0  # 用来记录while循环的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0  # 用来记录当前要显示的爆炸效果的图片的序号
        self.last_fire_time = 0

    def fire(self):
        if pygame.time.get_ticks() - self.EnemyBullet_interval > self.replenish_time:
            self.EnemyBullet_list.append(Bullet(self.screen, self.x, self.y))
            self.EnemyBullet_list.append(Bullet(self.screen, self.x + 24, self.y + 39))  # 根据敌机图片大小调整发射位置
            self.EnemyBullet_interval = pygame.time.get_ticks()  # 更新发射时间

    def __crate_images(self):  # 将爆炸需要的图片添加到self.bomb_lists中
        self.bomb_lists.append(pygame.image.load("./enemy0_down1.png"))
        self.bomb_lists.append(pygame.image.load("./enemy0_down2.png"))
        self.bomb_lists.append(pygame.image.load("./enemy0_down3.png"))
        self.bomb_lists.append(pygame.image.load("./enemy0_down4.png"))

    # 判断爆炸的方法,x1表示子弹最左侧的X坐标，x2表示子弹最右侧的X坐标，y表示子弹当前的Y坐标
    def blast(self, x1, x2, y):
        # 判断子弹能命中敌机的三种情况，满足任意一种即可让敌机爆炸，51是敌机图片的宽度，39是敌机图片的高度
        # 1.子弹横坐标在敌机横坐标的区域中，并且子弹Y坐标小于敌机图片的高度
        # 2.子弹最右侧坐标等于敌机最左侧坐标，并且子弹Y坐标小于敌机图片的高度
        # 3.子弹最左侧坐标等于敌机最右侧坐标，并且子弹Y坐标小于敌机图片的高度
        if ((x1 >= self.x and x2 <= self.x + 51) or
            x2 == self.x or
            x1 == self.x + 51) and y < 39:
            self.hit = True
            print("恭喜，你赢了")
            self.bullet_to_remove.append((x1, x2, y))
            pygame.event.post(pygame.event.Event(pygame.QUIT))  # 触发退出事件
            return  # 退出方法，防止执行后续代码

            # 收集需要删除的子弹

    def display(self):  # 显示敌机的方法
        # 显示敌机发射的子弹
        for bullet in self.EnemyBullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                self.EnemyBullet_list.remove(bullet)  # 从列表中删除子弹

        # 敌机发射子弹的时机（例如每5秒发射一次）

        if pygame.time.get_ticks() - self.last_fire_time > 5000:
            self.last_fire_time = pygame.time.get_ticks()
            self.fire()

        def fire(self):
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))  # 将发射的子弹对象存储到bullet_list中

        # 如果被击中,就显示爆炸效果,否则显示普通的飞机效果
        if self.hit == True:  # 如果满足爆炸条件，就显示爆炸的图片
            self.screen.blit(self.bomb_lists[self.image_index], (self.x, self.y))
            self.image_num += 1  # 这是统计循环次数，为了使玩家看清爆炸效果
            if self.image_num == 7:  # 如果循环次数达到7次
                self.image_num = 0  # 将循环次数改为0次
                self.image_index += 1  # 图片显示序号+1，换为另一张图
            if self.image_index > 3:  # 这里爆炸图片一共是四张，所以是图片序号大于三次
                time.sleep(1)  # 暂停一秒
                exit()  # 调用exit让游戏退出
        else:  # 否则显示正常的敌机图片
            self.screen.blit(self.image, (self.x, self.y))
            for bullet in self.bullet_to_remove:
                for b in Aircraft_obj.bullet_list:
                    if bullet[0] <= b.x + 22 and bullet[1] >= b.x and bullet[2] >= b.y - 10:
                        Aircraft_obj.bullet_list.remove(b)
                break

            self.bullet_to_remove.clear()  # 清空子弹列表

    def move(self):  # 敌机移动方法
        if self.hit == True:
            pass
        else:
            if self.direction == "right":  # 如果是向右移动
                self.x += 5  # X坐标自增加5
            elif self.direction == "left":  # 如果是向左移动
                self.x -= 5  # X坐标自减少5

            if self.x > 480 - 50:  # 如果X坐标大于窗口减去敌机宽度的值
                self.direction = "left"  # 移动方向改为左
            elif self.x < 0:  # 如果X坐标小于0
                self.direction = "right"  # 移动方向改为右


# 存储飞机的移动状态，添加上移和下移
aircraft_move_state = {
    'left': False,
    'right': False,
    'up': False,
    'down': False
}


# 处理鼠标和键盘事件的方法
def key_control(aircraft_temp):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            # 处理上移和下移按键
            if event.key == K_w or event.key == K_UP:
                aircraft_move_state['up'] = True
            elif event.key == K_s or event.key == K_DOWN:
                aircraft_move_state['down'] = True
            # 已有的左右移动和射击按键处理
            elif event.key == K_a or event.key == K_LEFT:
                aircraft_move_state['left'] = True
            elif event.key == K_d or event.key == K_RIGHT:
                aircraft_move_state['right'] = True
            elif event.key == K_SPACE:
                aircraft_temp.fire()
        elif event.type == KEYUP:
            # 处理上移和下移按键释放
            if event.key == K_w or event.key == K_UP:
                aircraft_move_state['up'] = False
            elif event.key == K_s or event.key == K_DOWN:
                aircraft_move_state['down'] = False
            # 已有的左右移动按键释放
            elif event.key == K_a or event.key == K_LEFT:
                aircraft_move_state['left'] = False
            elif event.key == K_d or event.key == K_RIGHT:
                aircraft_move_state['right'] = False


def gui(screen):
    running = True
    difficulty = None  # 用于存储选择的游戏难度
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 检查鼠标点击的位置是否在按钮区域内
                if easy_rect.collidepoint(event.pos):
                    difficulty = 'easy'
                    running = False
                elif medium_rect.collidepoint(event.pos):
                    difficulty = 'medium'
                    running = False
                elif hard_rect.collidepoint(event.pos):
                    difficulty = 'hard'
                    running = False

        screen.fill((0, 0, 0))  # 用黑色填充屏幕作为背景

        # 设置字体和大小
        font = pygame.font.Font(None, 36)
        # 显示选择难度的文本
        text = font.render('Select Difficulty', True, (255, 255, 255))
        screen.blit(text, (150, 100))

        # 创建难度选择按钮
        easy_rect = pygame.Rect(50, 200, 150, 50)  # 简单难度按钮位置和大小
        pygame.draw.rect(screen, (0, 255, 0), easy_rect)  # 绘制按钮
        easy_text = font.render('Easy', True, (255, 255, 255))
        screen.blit(easy_text, (easy_rect.x + 10, easy_rect.y + 10))  # 显示按钮文本

        medium_rect = pygame.Rect(220, 200, 150, 50)  # 中等难度按钮位置和大小
        pygame.draw.rect(screen, (255, 255, 0), medium_rect)  # 绘制按钮
        medium_text = font.render('Medium', True, (255, 255, 255))
        screen.blit(medium_text, (medium_rect.x + 10, medium_rect.y + 10))  # 显示按钮文本

        hard_rect = pygame.Rect(50, 270, 150, 50)  # 困难难度按钮位置和大小
        pygame.draw.rect(screen, (255, 0, 0), hard_rect)  # 绘制按钮
        hard_text = font.render('Hard', True, (255, 255, 255))
        screen.blit(hard_text, (hard_rect.x + 10, hard_rect.y + 10))  # 显示按钮文本

        pygame.display.update()  # 更新屏幕显示

    return difficulty  # 返回选择的难度


def draw_score(screen, score, font, x, y):
    """显示得分的函数"""
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (x, y))


def draw_best_score(screen, best_score, font, x, y):
    """显示历来最佳得分的函数"""
    best_score_text = font.render(f"Best Score: {best_score}", True, (255, 255, 255))
    screen.blit(best_score_text, (x, y))


def draw_timer(screen, start_time, font, x, y):
    """显示游戏时间的函数"""
    elapsed_time = pygame.time.get_ticks() - start_time
    minutes, seconds = divmod(elapsed_time / 1000, 60)
    timer_text = font.render(f"Time: {int(minutes):02d}:{int(seconds):02d}", True, (255, 255, 255))
    screen.blit(timer_text, (x, y))


def draw_best_time(screen, best_time, font, x, y):
    """显示历来最佳游戏时间的函数"""
    minutes, seconds = divmod(best_time / 1000, 60)
    best_time_text = font.render(f"Best Time: {int(minutes):02d}:{int(seconds):02d}", True, (255, 255, 255))
    screen.blit(best_time_text, (x, y))


def save_game_time_to_excel(game_time, filename='game_times.xlsx'):
    # 创建一个包含游戏时间的DataFrame
    game_times_df = pd.DataFrame({
        'Game Time (seconds)': [game_time]
    })

    # 检查文件是否存在，如果不存在，创建一个新的DataFrame；如果存在，加载现有的DataFrame
    try:
        # 使用现有的Excel文件，如果文件不存在则创建一个新的
        game_times_df.to_excel(filename, index=False, header=False, engine='openpyxl')
    except FileNotFoundError:
        # 文件不存在，添加表头并保存
        game_times_df.to_excel(filename, index=False, header=True, engine='openpyxl')


def main():
    # 1. 创建窗口

    global best_score, best_time
    pygame.init()
    screen = pygame.display.set_mode((480, 852), 0, 32)
    start_time = pygame.time.get_ticks()  # 游戏开始时间
    pygame.display.set_caption('Air Battle Game')
    # 显示GUI界面并获取选择的难度
    game_difficulty = gui(screen)
    if game_difficulty:
        print(f"Game will start in {game_difficulty} mode.")

        # 2. 创建一个背景图片
    background = pygame.image.load("./background.png")

    # 3. 创建一个飞机对象
    aircraft = Aircraft_obj(screen)

    # 4. 创建一个敌机对象
    enemy = EnemyPlane(screen)
    clock = pygame.time.Clock()  # 创建时钟对象
    last_replenish_time = pygame.time.get_ticks()  # 记录上次补给的时间
    start_time = pygame.time.get_ticks()  # 游戏开始时间
    score = 0  # 游戏得分

    aircraft.display()
    enemy.display()

    while True:
        screen.blit(background, (0, 0))  # 把背景复制到窗口的0,0处开始贴进去
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        aircraft.display()  # 执行飞机类中显示飞机的方法

        # 检查飞机发射的子弹是否击中敌机
        for bullet in aircraft.bullet_list:
            if bullet.y < 0:
                aircraft.bullet_list.remove(bullet)
            else:
                if enemy.blast(bullet.x, bullet.x, bullet.y):  # 这里blast方法需要返回一个布尔值表示是否击中
                    score += 100  # 击中敌机增加得分
                    break  # 假设每次只有一个子弹能击中敌机
                # 检查飞机发射的子弹是否击中敌机
        for bullet in aircraft.bullet_list:
            if bullet.y < 0:  # 如果子弹已经飞出屏幕，从列表中移除
                aircraft.bullet_list.remove(bullet)
            else:
                # 调用敌机的blast方法检查是否击中
                enemy.blast(bullet.x, bullet.x, bullet.y)
                # 更新得分和游戏时间

        # 检查是否更新最佳得分和最佳游戏时间
        if score > best_score:
            best_score = score
        if (pygame.time.get_ticks() - start_time) > best_time:
            best_time = pygame.time.get_ticks() - start_time

        # 根据按键状态更新飞机位置
        if aircraft_move_state['left']:
            aircraft.move_left()
        if aircraft_move_state['right']:
            aircraft.move_right()
        if aircraft_move_state['up']:
            aircraft.move_up()
        if aircraft_move_state['down']:
            aircraft.move_down()
            # 检查是否到了补给时间（每60秒）
        current_time = pygame.time.get_ticks()
        if current_time - last_replenish_time > 60000:  # 60000毫秒 = 1分钟
            aircraft.bullet_count = 0  # 重置子弹数量
            last_replenish_time = current_time  # 更新上次补给时间

        for bullet in aircraft.bullet_list:  # 循环飞机对象中存储的子弹信息
            x1 = bullet.x  # 子弹当前X坐标
            x2 = bullet.x + 22  # 子弹当前X坐标+子弹图片的宽
            y1 = bullet.y  # 子弹当前Y坐标
            enemy.blast(x1, x2, y1)  # 判断子弹的坐标区域有没有与敌机相交

        enemy.display()  # 执行敌机类中显示敌机的方法
        enemy.move()  # 调用敌机的移动方法

        if random.random() < 0.01:  # 每1%的概率发射子弹
            enemy.fire()

        # 检测飞机是否碰撞敌机或敌机子弹
        aircraft_rect = pygame.Rect(aircraft.x, aircraft.y, 100, 100)  # 根据飞机图片大小调整
        enemy_rect = pygame.Rect(enemy.x, enemy.y, 50, 39)  # 根据敌机图片大小调整

        if aircraft_rect.colliderect(enemy_rect) or any(
                pygame.Rect(bullet.x, bullet.y, 22, 10).colliderect(aircraft_rect) for bullet in
                enemy.EnemyBullet_list):
            print("很遗憾，你输了！")
            pygame.quit()
            sys.exit()
            # 游戏结束时，计算游戏时间
        game_time = (pygame.time.get_ticks() - start_time) / 1000  # 转换为秒
        # 保存游戏时间至Excel
        save_game_time_to_excel(game_time)

        pygame.display.update()  # 更新需要显示的内容到窗口
        key_control(aircraft)  # 处理飞机对象的相关事件
        clock.tick(60)
        time.sleep(0.01)  # 暂停0.01秒


if __name__ == '__main__':
    main()
