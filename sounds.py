import pygame
from settings import music_volume, sfx_volume

pygame.mixer.init()

background_music = pygame.mixer.Channel(0)
sfx = pygame.mixer.Channel(1)
background_music.set_volume(music_volume)
sfx.set_volume(sfx_volume)
chibiNinja = pygame.mixer.Sound('./sfx/03 Chibi Ninja.mp3')
shoot = pygame.mixer.Sound('./sfx/shoot.wav')
bump = pygame.mixer.Sound('./sfx/bump.wav')
bling = pygame.mixer.Sound('./sfx/bling.wav')
hit = pygame.mixer.Sound('./sfx/hit.wav')
