# coding=utf-8
"""alien ship module"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class represent alien ship instance"""
    def __init__(self, ai_settings, screen):
        """Init alien and set his start position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width / 2

    def blitme(self):
        """Draw alien on his current position"""
        self.screen.blit(self.image, self.rect)
