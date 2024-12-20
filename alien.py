import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # 外星人类
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        # 检测外星人超出屏幕
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True

    def update(self):
        # 更新外星人
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
