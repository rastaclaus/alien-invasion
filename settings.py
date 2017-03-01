# coding=utf-8
"""settings module"""


class Settings:
    """Settings storage class"""

    def __init__(self):
        """Init game settings"""
        self.screen_width = 1000
        self.screen_height = 720
        self.bg_color = (20, 20, 100)
        # Settings for bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 130, 190, 190
        self.bullets_allowed = 3
        # Settings for aliens
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        # fleet_direction = 1 - move right, -1 move left
        # game_stats
        self.ship_limit = 3
        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        self.alien_speed_factor = .5
        self.bullet_speed_factor = 3
        self.ship_speed_factor = 1.5
        self.fleet_drop_speed = 10
        self.alien_points = 50

        self.fleet_direction = 1

    def increase_speed(self):
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
