# USB Game
#
# This is a simple game designed to demonstrate the functionality of a USB joystick
# Music: 03 Chibi Ninja.mp3 by Eric Skiff
# Code by Nicholas Farrell

import pygame
from pygame.locals import *
import sys
from settings import screen_width, screen_height
from gameboard import Gameboard
from sounds import sfx, background_music, chibiNinja, shoot

pygame.init()

# sound setup
pygame.mixer.init()
background_music.play(chibiNinja, loops=-1)

# screen setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('USB Controller Game')

# clock setup
clock = pygame.time.Clock()

# gameboard setup
gameboard = Gameboard(screen)

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == JOYBUTTONDOWN:
            if event.button == 0:
                sfx.play(shoot)
            print(event)
    gameboard.run()
    pygame.display.update()
    clock.tick(60)
