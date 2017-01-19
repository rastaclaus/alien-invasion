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
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = 1
    if event.key == pygame.K_LEFT:
        ship.moving_left = 1

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = 0
    if event.key == pygame.K_LEFT:
        ship.moving_left = 0

def update_screen(ai_settings, screen, ship):
    """Refresh and draw screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
    
