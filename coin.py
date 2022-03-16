
import pygame
import random
from support import import_folder
from settings import coin_speed


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.speed_choice = [-2, -1, 0, 0, 1, 2]
        self.speed = coin_speed + random.choice(self.speed_choice)
        self.frames = import_folder('./graphics/coin')
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.height = self.rect.height

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.rect.x -= self.speed
        self.animate()
