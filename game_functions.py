# coding=utf-8
"""Game common functions"""

import sys
import pygame
from bullet import Bullet
from alien import Alien
from stars import Star

def check_events(ai_settings, screen, ship, bullets):
    """Key press and mouse events processing"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = 1
    if event.key == pygame.K_LEFT:
        ship.moving_left = 1
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = 0
    if event.key == pygame.K_LEFT:
        ship.moving_left = 0

def update_screen(ai_settings, screen, ship, aliens, bullets, stars):
    """Refresh and draw screen"""
    screen.fill(ai_settings.bg_color)
    for star in stars:
        star.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """compute aliens number in a one row"""
    available_space_x = ai_settings.screen_width - alien_width
    number_aliens_x = int(available_space_x / (1.5 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - 
            3 * alien_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, row_number, alien_number):
    """create alien and place him in a row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = 0.5 * alien_width + 1.5 * alien_width * alien_number
    alien.y = row_number * alien_height * 2
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, alien.rect.height,
            alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, row_number, alien_number)

STAR_COUNT = 50

from random import randint

def create_stars(ai_settings, screen, stars):
    for i in range(STAR_COUNT):
        coords = (randint(0, ai_settings.screen_width),
                randint(0, ai_settings.screen_height))
        star = Star(coords, screen)
        stars.append(star)

def update_aliens(aliens):
    aliens.update()
