"""alien invasion main module"""
import sys
import pygame

def run_game():
    """ Инициализирует игру и создаёт объект экрана"""
    pygame.init()
    screen = pygame.display.set_mode((1000, 720))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


run_game()
