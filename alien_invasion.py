#!/usr/bin/env python
# coding=utf-8

"""alien invasion main module"""
import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Initialise game,  create screen object, and start main loop"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_hight))
    bg_color = ai_settings.bg_color

    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
