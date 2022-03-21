import pygame
from settings import music_volume, sfx_volume

pygame.mixer.init()

background_music = pygame.mixer.Channel(0)
background_music.set_volume(music_volume)
chibiNinja = pygame.mixer.Sound('./sfx/03 Chibi Ninja.mp3')
shoot = pygame.mixer.Sound('./sfx/shoot.wav')
shoot.set_volume(sfx_volume)
bump = pygame.mixer.Sound('./sfx/bump.wav')
bump.set_volume(sfx_volume)
bling = pygame.mixer.Sound('./sfx/bling.wav')
bling.set_volume(sfx_volume)
hit = pygame.mixer.Sound('./sfx/hit.wav')
hit.set_volume(sfx_volume)
dead = pygame.mixer.Sound('./sfx/dead.wav')
dead.set_volume(sfx_volume)
