# USB Game
#
# This is a simple game designed to demonstrate the functionality of a USB joystick
# Music: 03 Chibi Ninja.mp3 by Eric Skiff
# Code by Nicholas Farrell

import pygame
from pygame.locals import *
import sys
from player import Player
from coin import Coin
from settings import screen_width, screen_height, background_color
from sounds import sfx, background_music, chibiNinja, shoot, bump

pygame.init()

# sound setup
pygame.mixer.init()
background_music.play(chibiNinja, loops=-1)

# screen setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('USB Controller Game')

# clock setup
clock = pygame.time.Clock()

# sprite setup
all_sprites = pygame.sprite.Group()
player = Player((screen_width/2, screen_height/2))
coin = Coin((screen_width/2 + 100, screen_height/2))
all_sprites.add(player)
all_sprites.add(coin)

# joystick setup
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("Error: no joystick connected")
else:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

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
        if event.type == JOYBUTTONUP:
            print(event)

    if joystick_count != 0:
        horiz_axis_pos = my_joystick.get_axis(0)
        vert_axis_pos = my_joystick.get_axis(1)
    screen.fill(background_color)
    player.update((horiz_axis_pos, vert_axis_pos))
    hit = player.check_bump(screen_width, screen_height)
    if hit:
        sfx.play(bump)
    for sprite in all_sprites:
        try:
            sprite.animate()
        except AttributeError:
            pass
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)

# TODO: Create Gameboard class with method run(self) which will be called in main game loop
