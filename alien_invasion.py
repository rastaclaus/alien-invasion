#!/usr/bin/env python
# coding=utf-8

"""alien invasion main module"""
import pygame
from pygame.sprite import Group

import game_functions as gf
from game_stats import GameStats
from settings import Settings
from ship import Ship
from button import Button
from scoreboard import Scoreboard


def run_game():
    """Initialise game,  create screen object, and start main loop"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "СТАРТ")

    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    sb = Scoreboard(ai_settings, screen, stats)
    gf.create_fleet(ai_settings, screen, aliens)
    while True:
        gf.check_events(ai_settings, aliens,
                        screen, stats, ship, bullets, play_button, sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,
                              aliens, bullets, stats, sb)
            gf.update_aliens(ai_settings, stats, screen,
                             ship, aliens, bullets, sb)
        gf.update_screen(ai_settings,
                         screen,
                         stats,
                         sb,
                         ship,
                         aliens,
                         bullets,
                         play_button)


run_game()
