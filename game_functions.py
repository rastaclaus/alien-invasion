"""Модуль для общих функций игры"""

import sys
import pygame

def check_events():
    """Функция обработки нажатий клавиш и событий мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Обновляет изображения на экране и отображает новый экран"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip()
