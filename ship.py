# coding=utf-8
"""Player ship module"""
import pygame

class Ship():
    """Player ship class"""
    def __init__(self, ai_settings, screen):
        """Init player ship and his position"""
        self.screen = screen

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.ai_settings = ai_settings
        self.moving_right = 0
        self.moving_left = 0

    def update(self):
        """Refresh ship position"""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)
