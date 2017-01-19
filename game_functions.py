# coding=utf-8
"""Game common functions"""

import sys
import pygame

def check_events():
    """Key press and mouse events processing"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Refresh and draw screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()
