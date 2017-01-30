# coding=utf-8
"""settings module"""

class Settings:
    """Settings storage class"""

    def __init__(self):
        """Init game settings"""
        self.screen_width = 1000
        self.screen_height = 720
        self.bg_color = (130, 130, 255)
        self.ship_speed_factor = 1.5
        # Settings for bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
