import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主程序"""

    def __init__(self):
        print("游戏初始化")

        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create__sprites()
        pygame.time.set_timer(CREATE_ENMEY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)
    def __create__sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_grup = pygame.sprite.Group(bg1,bg2)

        self.enemy_grup = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_grup = pygame.sprite.Group(self.hero)



    def __event__handler(self):
        for event in pygame.event.get():
            #判断是否退出
            if event.type == pygame.QUIT:
                PlaneGame.__game__over()
            elif event.type == CREATE_ENMEY_EVENT:
                enemy = Enemy()
                self.enemy_grup.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        keys_prsesed = pygame.key.get_pressed()
        if keys_prsesed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_prsesed[pygame.K_LEFT]:
            self.hero.speed = -2

    def __check__collide(self):
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_grup,True,True)
        enemies=pygame.sprite.groupcollide(self.hero_grup,self.enemy_grup,False,True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game__over()

    def __update__sprites(self):
        self.back_grup.update()
        self.back_grup.draw(self.screen)

        self.enemy_grup.update()
        self.enemy_grup.draw(self.screen)

        self.hero_grup.update()
        self.hero_grup.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game__over():
        print("游戏结束")
        pygame.quit()
        exit()


    def star_game(self):
        print("游戏开始")
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event__handler()
            self.__check__collide()
            self.__update__sprites()
            pygame.display.update()


if __name__ == '__main__':

    #创建游戏对象
    game = PlaneGame()

    #启动游戏
    game.star_game()