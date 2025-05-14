import pygame  # 导入pygame模块
from pygame.locals import *  # 导入pygame.locals模块
import time  # 导入time模块
import random
# 子弹类
class Bullet(object):
    # 构造方法，用于初始化子弹对象的属性
    def __init__(self, screen_temp, x, y):
        self.x = x + 40  # 子弹起始x坐标
        self.y = y - 20  # 子弹起始y坐标
        self.screen = screen_temp  # 窗口
        self.image = pygame.image.load("./bullet.png")  # 创建一个子弹图片

    # 显示子弹图片的方法
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))  # 显示子弹图片

    # 子弹移动
    def move(self):
        self.y -= 10  # 子弹y坐标自减10

    # 判断子弹是否越界的方法
    def judge(self):
        if self.y < 0:  # 如果子弹的y坐标小于0
            return True  # 返回true正确
        else:
            return False  # 返回false错误

class Bullet1(object):
    # 构造方法，用于初始化子弹对象的属性
    def __init__(self, screen_temp, x, y):
        self.x = x + 40  # 子弹起始x坐标
        self.y = y - 20  # 子弹起始y坐标
        self.screen = screen_temp  # 窗口
        self.image = pygame.image.load("./bullet.png")  # 创建一个子弹图片

    # 显示子弹图片的方法
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))  # 显示子弹图片

    # 子弹移动
    def move(self):
        self.y += 10  # 子弹y坐标自减10

    # 判断子弹是否越界的方法
    def judge(self):
        if self.y > 800:  # 如果子弹的y坐标小于0
            return True  # 返回true正确
        else:
            return False  # 返回false错误

# 玩家飞机类
class Aircraft_obj(object):
    # 构造方法，初始化飞机对象的属性
    def __init__(self, screen_temp):
        self.x = 190  # 飞起起始x坐标
        self.y = 708  # 飞机起始y坐标
        self.screen = screen_temp  # 窗口
        self.image = pygame.image.load("./hero1.png")  # 创建一个飞机图片
        self.bullet_list = []  # 存储发射出去的子弹对象
        self.bullet_count = 5  # 子弹数量
        self.hit = False  # 表示是否要爆炸
        self.bomb_lists = []  # 用来存储爆炸时需要的图片
        self.__crate_images()  # 调用这个方法向bomb_lists中添加图片
        self.image_num = 0  # 用来记录while循环的次数，当次数达到一定值时才显示一张爆炸的图，然后清空
        self.image_index = 0  # 用来记录当前要显示的爆炸效果的图片的序号
    # 显示飞机图片的方法（这里包括了显示子弹的图片）
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))  # 显示飞机图片
        # 显示飞机发射的所有子弹
        for bullet in self.bullet_list:
            bullet.display()  # 显示子弹
            bullet.move()  # 移动子弹
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)  # 删除子弹

    def __crate_images(self):
        self.bomb_lists.append(pygame.image.load("./enemy0_down1.png"))
        self.bomb_lists.append(pygame.image.load("./enemy0_down2.png"))
        self.bomb_lists.append(pygame.image.load("./enemy0_down3.png"))
        self.bomb_lists.append(pygame.image.load("./enemy0_down4.png"))
        # 判断爆炸的方法，x1为子弹最左侧的横坐标，x2为子弹最右侧的横坐标，y为子弹当前的纵坐标
    # 飞机左移方法
    def move_left(self):
        if self.x < 10:  # x坐标小于10（移动距离）
            pass  # 不做任何事
        else:
            self.x -= 10  # X坐标自减少10

    # 飞机右移方法
    def move_right(self):
        if self.x > 480 - 100 - 10:  # X坐标大于（窗口宽度-飞机宽度-移动距离）的值
            pass  # 不做任何事
        else:
            self.x += 10  # 坐标自增加10

    def move_up(self):
        if self.y < 426:
            pass
        else:
            self.y -= 10

    def move_down(self):
        if self.y > 852 - 150 - 10:
            pass
        else:
            self.y += 10

    def blast(self, x1, x2, y):
        # 判断子弹能命中敌机的三种情况（51是敌机图片的宽度，39是敌机图片的高度）
        if ((  x1 >= self.x and x2 <= self.x + 51) or x2 == self.x or x1 == self.x + 51) and y < self.y + 39 and y > self.y:
            self.hit = True
    # 存储发射子弹的方法
    def fire(self):
        if self.bullet_count > 0:
            self.bullet_list.append(Bullet(self.screen, self.x, self.y))  # 将发射的子弹对象存储到bullet_list中
            self.bullet_count -= 1


# 敌机类
class EnemyPlane(object):
    # 构造方法，初始化敌机对象的属性
    def __init__(self, screen_temp):
        self.x = 0  # 敌机的起始x坐标
        self.y = 0  # 敌机的起始y坐标
        self.screen = screen_temp  # 窗口
        self.image = pygame.image.load("./enemy0.png")  # 创建一个敌机图片
        self.direction = "right"  # 用来存储飞机移动方向，默认向右移动

        self.direction_y = "down"
        self.bullet_list = []  # 存储发射出去的子弹对象
        # 爆炸效果用的属性
        self.hit = False  # 表示是否要爆炸
        self.bomb_lists = []  # 用来存储爆炸时需要的图片
        self.__crate_images()  # 调用这个方法向bomb_lists中添加图片
        self.image_num = 0  # 用来记录while循环的次数，当次数达到一定值时才显示一张爆炸的图，然后清空
        self.image_index = 0  # 用来记录当前要显示的爆炸效果的图片的序号

    # 敌机移动方法
    # 敌机移动方法
    def move(self):
        if self.hit == True:  # 如被击中，敌机不移动
            pass
        else:
            if self.direction == "right":
                self.x += 5
                if self.x > 480 - 50:  # 当敌机走到屏幕最右侧时
                    self.x = 480 - 50  # 重置为最右侧位置
                    self.direction = "left"  # 改变 X 轴移动方向为向左


            elif self.direction == "left":
                self.x -= 5
                if self.x < 0:  # 当敌机走到屏幕最左侧时
                    self.x = 0  # 重置为最左侧位置
                    self.direction = "right"  # 改变 X 轴移动方向为向右

    # 判断是否与飞机碰撞
    def is_hit_aircraft(self, aircraft):
        aircraft_rect = pygame.Rect(aircraft.x, aircraft.y, 100, 124)
        enemy_rect = pygame.Rect(self.x, self.y, 51, 39)
        return aircraft_rect.colliderect(enemy_rect)

    # 将爆炸需要的图片添加到self.bomb_lists中
    def __crate_images(self):
        self.bomb_lists.append(pygame.image.load("./enemy0_down1.png"))
        self.bomb_lists.append(pygame.image.load("./enemy0_down2.png"))
        self.bomb_lists.append(pygame.image.load("./enemy0_down3.png"))
        self.bomb_lists.append(pygame.image.load("./enemy0_down4.png"))
        # 判断爆炸的方法，x1为子弹最左侧的横坐标，x2为子弹最右侧的横坐标，y为子弹当前的纵坐标

    def blast(self, x1, x2, y):
        # 判断子弹能命中敌机的三种情况（51是敌机图片的宽度，39是敌机图片的高度）
        if ((  x1 >= self.x and x2 <= self.x + 51) or x2 == self.x or x1 == self.x + 51) and y < self.y + 39 and y > self.y:
            self.hit = True

    def fire(self):
            self.bullet_list.append(Bullet1(self.screen, self.x, self.y))  # 将发射的子弹对象存储到bullet_list中
    def display(self):  # 显示敌机的方法
        # 如果被击中，就显示爆炸效果，否则显示普通的飞机效果
        if self.hit == True:  # 如果满足爆炸条件，就显示爆炸的图片
            self.screen.blit(self.bomb_lists[self.image_index], (self.x, self.y))

            self.image_num += 1  # 统计循环次数，为了使玩家看清爆炸效果
        if self.image_num == 7:  # 如果循环次数达到7次
            self.image_num = 0  # 将循环次数改为0次
            self.image_index += 1  # 图片显示序号加1，换为另一张图
        if self.image_index > 3:  # 如果图片序号大于3（一共4张图片）
                time.sleep(1)  # 暂停一秒
                exit()  # 调用exit退出游戏
        else:  # 否则显示正常的敌机图片
            self.screen.blit(self.image, (self.x, self.y))
        for bullet1 in self.bullet_list:
            bullet1.display()  # 显示子弹
            bullet1.move()  # 移动子弹
            if bullet1.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet1)  # 删除子弹
    # 处理鼠标和键盘事件的方法


def key_control(aircraft_temp):
    # 获取当前等待处理的事件，使用for循环遍历里面的事件
    for event in pygame.event.get():
        # 判断是否点击了退出按钮
        if event.type == QUIT:
            print("exit")  # 输出“exit”
            exit()  # 退出窗口
        # 判断是不是键盘按下事件
        elif event.type == KEYDOWN:

            if event.key == K_SPACE:
                print('space')  # 输出“space”
                aircraft_temp.fire()  # 执行飞机类中存储子弹的方法


def main():
    # 创建窗口
    pygame.init()  # 初始化pygame
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 创建一个背景图片
    background = pygame.image.load("./background.png")
    # 创建一个玩家飞机对象
    aircraft = Aircraft_obj(screen)
    # 创建一个敌机对象
    enemy = EnemyPlane(screen)
    last_bullet_supply_time = 0
    bullet_supply_interval = 10
    while True:
        screen.blit(background, (0, 0))  # 显示背景图片
        aircraft.display()  # 执行飞机类中显示飞机的方法
        current_time = time.time()


        if enemy.hit:
            # 定义颜色
            print("命中")
            WHITE = (255, 255, 255)
            RED = (255, 0, 0)
            GREEN = (0, 255, 0)
            # 通过字体文件获得字体对象
            fontObj = pygame.font.Font('ziti/FZQTFW.TTF', 50)
            # 配置要显示的文字
            textSurfaceObj1 = fontObj.render('恭喜你，你赢了！', True, GREEN, RED)
            # 获得要显示的对象的rect
            textRectObj1 = textSurfaceObj1.get_rect()
            # 设置显示对象的坐标
            textRectObj1.center = (250, 400)
            # 设置背景
            screen.fill(WHITE)
            screen.blit(textSurfaceObj1, textRectObj1)
            pygame.display.update()  # 强制更新显示
            pygame.time.wait(1000)  # 暂停1秒
            exit()

        if aircraft.hit:
            print("碰撞")
            screen = pygame.display.set_mode((480, 852))
            pygame.display.set_caption('Font')
            WHITE = (255, 255, 255)
            RED = (255, 0, 0)
            GREEN = (0, 255, 0)
            fontObj = pygame.font.Font('ziti/FZQTFW.TTF', 50)
            textSurfaceObj2 = fontObj.render('很遗憾，你输了！', True, GREEN, RED)
            textRectObj2 = textSurfaceObj2.get_rect()
            textRectObj2.center = (250, 400)
            screen.fill(WHITE)
            screen.blit(textSurfaceObj2, textRectObj2)
            pygame.display.update()  # 强制更新显示
            pygame.time.wait(1000)  # 暂停1秒
            exit()
        if random.random() < 0.01:  # 每1%的概率发射子弹
            enemy.fire()
        for bullet in aircraft.bullet_list:  # 遍历飞机对象中存储的子弹信息
            x1 = bullet.x  # 子弹当前横坐标
            x2 = bullet.x + 22  # 子弹当前横坐标加子弹图片的宽
            y1 = bullet.y  # 子弹当前纵坐标
            enemy.blast(x1, x2, y1)  # 判断子弹的坐标区域有没有与敌机相交
        for bullet1 in enemy.bullet_list:  # 遍历飞机对象中存储的子弹信息
            x1 = bullet1.x  # 子弹当前横坐标
            x2 = bullet1.x - 22  # 子弹当前横坐标加子弹图片的宽
            y1 = bullet1.y  # 子弹当前纵坐标
            aircraft.blast(x1, x2, y1)  # 判断子弹的坐标区域有没有与敌机相交
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            aircraft.move_left()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            aircraft.move_right()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            aircraft.move_up()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            aircraft.move_down()
        if current_time - last_bullet_supply_time > bullet_supply_interval:
            # 补充子弹
            aircraft.bullet_count = 5  # 清空当前的子弹列表

            # 更新时间变量
            last_bullet_supply_time = current_time
        enemy.display()  # 执行敌机类中显示敌机的方法
        enemy.move()  # 调用敌机的移动方法
        pygame.display.update()  # 更新需要显示的内容到窗口
        key_control(aircraft)  # 处理飞机对象的相关事件
        time.sleep(0.01)  # 暂停0.01秒


main()