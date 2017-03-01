#!/usr/bin/env python
# coding=utf-8

"""alien invasion main module"""
import sys
from time import sleep
import pygame
from pygame.sprite import Group

import game_functions as gf
from game_stats import GameStats
from settings import Settings
from ship import Ship
from button import Button
from scoreboard import Scoreboard
from bullet import Bullet
from alien import Alien


class Game():
    def __init__(self):
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width,
                                               self.ai_settings.screen_height))
        self.play_button = Button(self.ai_settings, self.screen, "СТАРТ")
        self.stats = GameStats(self.ai_settings)
        self.ship = Ship(self.ai_settings, self.screen)
        self.bullets = Group()
        self.aliens = Group()
        self.sb = Scoreboard(self.ai_settings, self.screen, self.stats)
        self.gf.create_fleet(self.ai_settings, self.screen, self.aliens)

    def run(self):
        """Initialise game,  create screen object, and start main loop"""
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        while True:
            self.check_events()
            if self.stats.game_active:
                self.ship.update()
                self.update_bullets()
                self.update_aliens()
                self.update_screen()

    def check_events(self):
        """Key press and mouse events processing"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_play_button(mouse_x, mouse_y)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = 1
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = 1
        if event.key == pygame.K_SPACE:
            self.fire_bullet()
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_p and not self.stat.game_active:
            self.game_start()

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = 0
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = 0

    def check_play_button(self, mouse_x, mouse_y):
        button_clicked = self.play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not self.stat.game_active:
            self.game_start()

    def game_start(self):
            self.ai_settings.initialise_dynamic_settings()
            pygame.mouse.set_visible(False)
            self.stat.reset_stat()
            self.stat.game_active = True
            self.aliens.empty()
            self.bullets.empty()
            self.create_fleet()
            self.ship.center_ship()
            self.sb.prep_score()
            self.sync_high_scores()
            self.sb.prep_ships()

    def sync_high_scores(self):
        if self.stat.scores >= self.stat.high_scores:
            self.stat.high_scores = self.stat.scores
            self.sb.prep_high_score()

    def update_screen(self):
        """Refresh and draw screen"""
        self.screen.fill(self.ai_settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.stat.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.check_bullet_alien_collisions()

    def check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                True, True)
        if collisions:
            self.stat.scores +=\
                self.ai_settings.alien_points * len(collisions.values())
            self.sb.prep_score()
            self.sync_high_scores()

        if len(self.aliens) == 0:
            self.ai_settings.increase_speed()
            self.create_fleet()
            self.stat.level += 1

    def fire_bullet(self):
        if len(self.bullets) < self.ai_settings.bullets_allowed:
            new_bullet = Bullet(self.ai_settings, self.screen, self.ship)
            bullets.add(new_bullet)
                self.sb.prep_score()
