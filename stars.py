# coding=utf-8

import pygame

class Star():
    def __init__(self, coords, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        x, y  = coords
        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
