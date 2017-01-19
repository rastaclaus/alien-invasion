# coding=utf-8
"""Player ship module"""
import pygame

class Ship():
    """Player ship class"""
    def __init__(self, screen):
        """Init player ship and his position"""
        self.screen = screen

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = 0
        self.moving_left = 0

    def update(self):
        """Refresh ship position"""
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)
