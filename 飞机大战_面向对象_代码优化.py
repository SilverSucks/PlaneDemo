import pygame
import random
import time
from pygame.locals import *

'''
飞机大战游戏，面向对象方式实现——代码优化
通过观察发现，我方飞机和敌方飞机有很多相似的功能
我方飞机子弹类和敌方飞机子弹类也有很多相似的地方
相似的地方可以抽象出来 作为一个类
'''


# 抽象一个飞机的基类
class BasePlane (object):
    def __init__(self, screen, imagePath):
        '''
        初始化基类函数
        :param screen: 主窗体对象
        :param imageName: 加载的图片
        '''
        self.screen = screen
        self.image = pygame.image.load (imagePath)
        self.bulletList = []  # 存储所有的子弹
        pass

    def display(self):
        '''
        飞机在主窗口的显示
        :return:
        '''
        self.screen.blit (self.image, (self.x, self.y))
        # 完善子弹的展示逻辑，声明一个新的列表对象，存放要显示的子弹，把越界的子弹删除掉
        needDellItemList = []  # 定义存放需要删除的子弹的列表,为了不修改原始数据

        for item in self.bulletList:
            if item.isOverBoundary ():  # 如果子弹越界，把即将消失的子弹从列表中删除
                needDellItemList.append (item)
                pass
            pass
        for i in needDellItemList:  # 遍历需要删除的子弹列表，进行删除
            self.bulletList.remove (i)
            pass
        # 更新有效的子弹
        for bullet in self.bulletList:
            bullet.display ()  # 显示子弹的位置
            bullet.move ()  # 让子弹进行移动
        pass

    pass

# 抽象出一个子弹类
class BaseBullet(object):
    '''
    公共的子弹类
    '''
    def __init__(self, x, y, screen, bulletType):
        '''
        :param x:
        :param y:
        :param screen:
        :param bulletType: 用来标识是我方子弹还是敌方子弹
        '''
        self.type = bulletType
        self.screen = screen
        if self.type == 'hero':
            self.x = x + 13
            self.y = y + 20
            self.imagePath = './feiji/bullet.png'
            pass
        elif self.type == 'enemy':
            self.x = x
            self.y = y + 10
            self.imagePath = './feiji/bullet1.png'
            pass
        self.image = pygame.image.load(self.imagePath)
        pass
    def move(self):
        '''
        子弹的移动
        :return:
        '''
        if self.type == 'hero':
            self.y -= 2
            pass
        elif self.type == 'enemy':
            self.y += 2
        pass
    def display(self):
        '''
        子弹的显示
        :return:
        '''
        self.screen.blit(self.image, (self.x, self.y))
        pass
    def isOverBoundary(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y > 500 or self.y < 0:
            return True
        else:
            return False
        pass
    pass

# 玩家飞机类
class HeroPlane (BasePlane):
    def __init__(self, screen, image):
        '''
        初始化函数
        :param screen: 主窗体对象
        :param image:  飞机的图片
        '''
        # 飞机的默认位置
        self.x = 150
        self.y = 450
        #调用父类的构造方法
        super().__init__(screen, './feiji/hero.png')
        pass

    def moveleft(self):
        '''
        左移动
        :return:
        '''
        if self.x > 0:  # 左移
            self.x -= 10
        pass

    def moveright(self):
        '''
        右移动
        :return:
        '''
        if self.x < 350 - 40:
            self.x += 10
        pass

    def shot(self):
        '''
        发射子弹的函数，不停地更改子弹的位置，来营造一个子弹移动的效果
        :return:
        '''
        # 创建一个子弹对象，当前飞机的位置(x, y) 以及屏幕参数
        newBullet = BaseBullet (self.x, self.y, self.screen, 'hero')
        self.bulletList.append (newBullet)  # 把子弹对象添加到子弹列表中
        pass
    pass


'''
创建敌机类,跟己方飞机功能类似。
同样继承BasePlane类
'''

class EnemyPlane(BasePlane):
    def __init__(self, screen):
        # 飞机的默认位置
        self.x = 150
        self.y = 0
        # 默认设置一个方向,默认向右走
        self.direction = 'right'

        # 继承父类的构造方法
        super().__init__(screen, './feiji/enemy0.png')


    def shotBullet(self):  # 表示敌方发射的子弹
        '''
        敌机发射，敌机发射子弹是随机的
        :return:
        '''
        num = random.randint (1, 30)
        if num == 3:
            newBullet = BaseBullet (self.x, self.y, self.screen, 'enemy')
            self.bulletList.append (newBullet)
        pass

    def move(self):
        '''
        敌机移动，随机进行
        :return:
        '''
        if self.direction == 'right':
            self.x += 0.5
            pass
        elif self.direction == 'left':
            self.x -= 0.5
            pass
        # 判断边界，飞机左右进行移动
        if self.x > 350 - 20:
            self.direction = 'left'
            pass
        elif self.x < 0:
            self.direction = 'right'
        pass

    pass


def key_control(HeroObj):
    '''
    定义普通的函数   用来实现键盘的检测
    :param HeroObj:   可控制检测的对象
    :return:
    '''
    # 获取键盘事件
    eventlist = pygame.event.get ()
    for event in eventlist:
        if event.type == QUIT:
            print ('退出')
            exit ()
            pass
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.type == K_a or event.key == K_LEFT:
                print ('left')
                HeroObj.moveleft ()  # 调用函数实现左移动
                pass
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print ('right')
                HeroObj.moveright ()  # 调用函数，实现右移动
                pass
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print ('space,发射子弹')
                HeroObj.shot()
                pass
            pass
        pass
    pass


def main():
    # 1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode ((350, 500), 0, 32)
    # 2. 加载一张和窗口大小一样的图片，用来充当背景
    background = pygame.image.load ('./feiji/background.png')
    # 设置一个title
    pygame.display.set_caption ('飞机大战游戏')

    # 添加背景音乐
    pygame.mixer.init ()
    pygame.mixer.music.load ('./feiji/background.mp3')
    pygame.mixer.music.set_volume (0.2)  # 设置背景音乐的音量
    pygame.mixer.music.play (-1)  # 设置音乐无限循环

    hero = HeroPlane (screen, background)  # 创建HeroPlane对象
    enemyPlane = EnemyPlane (screen)  # 创建敌机对象

    # 3. 把背景图片放到窗口中显示
    while True:
        # 设定需要显示的背景图
        screen.blit (background, (0, 0))
        hero.display ()
        enemyPlane.display ()  # 调用方法，显示敌机
        enemyPlane.move ()  # 敌机移动
        enemyPlane.shotBullet ()  # 敌机随机发射子弹
        key_control (hero)

        # 更新需要显示的内容
        pygame.display.update ()
        time.sleep (0.01)  # 休眠一秒钟
        # pygame.time.Clock().tick(25)  # 一秒钟执行5次
        pass
    pass


if __name__ == '__main__':
    main ()
