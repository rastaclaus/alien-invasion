"""alien invasion main module"""
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """ Инициализирует игру и создаёт объект экрана"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_hight))
    bg_color = ai_settings.bg_color

    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)
    while True:
        gf.check_events()
        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()


run_game()
