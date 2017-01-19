"""Модуль для общих функций игры"""

import sys
import pygame

def check_events():
    """Функция обработки нажатий клавиш и событий мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
