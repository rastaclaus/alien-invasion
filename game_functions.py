
import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


""""""
def check_events(ai_settings, aliens,
                 screen, stat, ship, bullets, play_button, sb):
    """Key press and mouse events processing"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,
                                 screen, ship, bullets, stat, aliens, sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stat, play_button, ship,
                              aliens, bullets, mouse_x, mouse_y, sb)


""""""
def sync_high_scores(stat, sb):
    if stat.scores >= stat.high_scores:
        stat.high_scores = stat.scores
        sb.prep_high_score()

""""""
def game_start(stat, aliens, bullets, ai_settings, screen, ship, sb):
        ai_settings.initialise_dynamic_settings()
        pygame.mouse.set_visible(False)
        stat.reset_stat()
        stat.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, aliens)
        ship.center_ship()
        sb.prep_score()
        sync_high_scores(stat, sb)
        sb.prep_ships()


""""""
def check_play_button(ai_settings, screen, stat, play_button, ship,
                      aliens, bullets, mouse_x, mouse_y, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stat.game_active:
        game_start(stat, aliens, bullets, ai_settings, screen, ship, sb)

""""""
def check_keydown_events(event, ai_settings,
                         screen, ship, bullets, stat, aliens, sb):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = 1
    if event.key == pygame.K_LEFT:
        ship.moving_left = 1
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_p and not stat.game_active:
        game_start(stat, aliens, bullets, ai_settings, screen, ship, sb)

""""""
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = 0
    if event.key == pygame.K_LEFT:
        ship.moving_left = 0


""""""
def update_screen(ai_settings,
                  screen,
                  stat,
                  sb,
                  ship,
                  aliens,
                  bullets,
                  play_button):
    """Refresh and draw screen"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stat.game_active:
        play_button.draw_button()
    pygame.display.flip()


""""""
def update_bullets(ai_settings, screen, aliens, bullets, stat, sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen,
                                  aliens, bullets, stat, sb)


""""""
def check_bullet_alien_collisions(ai_settings, screen,
                                  aliens, bullets, stat, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stat.scores += ai_settings.alien_points * len(collisions.values())
        sb.prep_score()
        sync_high_scores(stat, sb)

    if len(aliens) == 0:
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, aliens)
        stat.level += 1
        sb.prep_score()


""""""
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
    alien.y = 60 + row_number * alien_height * 2
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


def check_aliens_bottom(ai_settings, stat, screen, ship, aliens, bullets, sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stat, screen, ship, aliens, bullets, sb)
            break


def update_aliens(ai_settings, stat, screen, ship, aliens, bullets, sb):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stat, screen, ship, aliens, bullets, sb)
    check_aliens_bottom(ai_settings, stat, screen, ship, aliens, bullets, sb)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.y_dropcount = ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stat, screen, ship, aliens, bullets, sb):
    stat.ships_remain -= 1
    sb.prep_ships()
    if stat.ships_remain > 0:
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, aliens)
        ship.center_ship()
        sleep(1)
    else:
        stat.game_active = False
        pygame.mouse.set_visible(True)
