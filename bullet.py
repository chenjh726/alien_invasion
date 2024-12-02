import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # 子弹类

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midbottom = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        # 更新子弹
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        # 显示子弹
        pygame.draw.rect(self.screen, self.color, self.rect)