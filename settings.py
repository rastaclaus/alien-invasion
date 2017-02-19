# coding=utf-8
"""settings module"""


class Settings:
    """Settings storage class"""

    def __init__(self):
        """Init game settings"""
        self.screen_width = 1000
        self.screen_height = 720
        self.bg_color = (20, 20, 100)
        self.ship_speed_factor = 1.5
        # Settings for bullet
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 130, 190, 190
        self.bullets_allowed = 3
        # Settings for aliens
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 30
        # fleet_direction = 1 - move right, -1 move left
        self.fleet_direction = 1
        # game_stats
        self.ship_limit = 3
