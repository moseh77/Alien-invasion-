

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    # Make a ship.
    ship = Ship(ai_settings, screen)

    # make a group to store bullets and a group of aliens
    bullets = Group()
    aliens  = Group()

    # Make an alien
    alien = Alien(ai_settings, screen)
    # create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    pygame.display.set_caption("Alien Invasion")

    # Make the play buttom
    play_button = Button(ai_settings, screen, "play")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)



    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
             ship.update()

        
             gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
             #bullets.update()

             # Get rid of bullets that have disappeared.
             for bullet in bullets.copy():
                     if bullet.rect.bottom <= 0:
                          bullets.remove(bullet)
             #print(len(bullets))

             gf.update_aliens(ai_settings, stats,screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

        

        
run_game()


