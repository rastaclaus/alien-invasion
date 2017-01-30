#!/usr/bin/env python
# coding=utf-8

"""alien invasion main module"""
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from stars import Star
import game_functions as gf

def run_game():
    """Initialise game,  create screen object, and start main loop"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    stars = []
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)
    gf.create_stars(ai_settings, screen, stars)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.update_screen(ai_settings,
                         screen,
                         ship,
                         aliens,
                         bullets,
                         stars)

run_game()
