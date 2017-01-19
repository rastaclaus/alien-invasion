# coding=utf-8
"""settings module"""

class Settings:
    """Settings storage class"""

    def __init__(self):
        """Init game settings"""
        self.screen_width = 1000
        self.screen_hight = 720
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
