class GameStats:
    # 游戏统计信息类

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        file = open("high_score.txt",'r')
        high_score_str = file.read().strip()
        self.high_score = int(high_score_str)
        file.close()

    def reset_stats(self):
        # 重置游戏统计信息
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1