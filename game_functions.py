# coding=utf-8
"""Game common functions"""

import sys
import pygame

def check_events(ship):
    """Key press and mouse events processing"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1
            elif event.key == pygame.K_LEFT:
                ship.rect.centerx -= 1

def update_screen(ai_settings, screen, ship):
    """Refresh and draw screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()
