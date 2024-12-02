class Settings:
    # 存储游戏中所有设置类

    def __init__(self):
        # 初始化游戏的静态设置

        # 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed = 0.5
        self.alien_drop_speed = 5
        # fleet_direction为1表示右移，为0表示左移
        self.fleet_direction = 1

        # 加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 初始化游戏的动态设置

        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 0.5
        self.alien_points = 50

    def increase_speed(self):
        # 提高速度设置

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
