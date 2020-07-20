import pygame
from pygame.locals import *
'''
1. 搭建界面，主要完成窗口和背景图的显示
2. 添加背景音乐
3. 添加飞机图片
4. 实现飞机的键盘控制
以上功能都是基于面向过程实现的，可扩展性不好
'''
def main():
    #1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((350, 500), 0, 32)
    #2. 加载一张和窗口大小一样的图片，用来充当背景
    background = pygame.image.load('./feiji/background.png')
    # 设置一个title
    pygame.display.set_caption('飞机大战游戏')

    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./feiji/background.mp3')
    pygame.mixer.music.set_volume(0.2)   # 设置背景音乐的音量
    pygame.mixer.music.play(-1)  # 设置音乐无限循环

    # 载入玩家的飞机图片
    hero = pygame.image.load('./feiji/hero.png')
    # 初始化玩家的位置
    x,y = 160, 450
    #3. 把背景图片放到窗口中显示
    while True:
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))  # 玩家飞机图片

        # 获取键盘事件
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == QUIT:
                print('退出')
                exit()
                pass
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if event.type == K_a or event.key == K_LEFT:
                    print('left')
                    if x > 0:   # 向左一次移动五个像素
                        x -= 5
                        pass
                    pass
                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    if x < 310:   # 向右一次移动5个像素
                        x += 5
                        pass
                    pass
                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')
        # 更新需要显示的内容
        pygame.display.update()
        pass
    pass

if __name__ == '__main__':
    main()