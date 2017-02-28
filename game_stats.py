# -*- coding=UTF-8 -*-


class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stat()
        self.game_active = False

    def reset_stat(self):
        self.ships_remain = self.ai_settings.ship_limit
        self.scores = 0
