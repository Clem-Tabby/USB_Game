
import pygame
from support import import_folder


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.frames = import_folder('./graphics/coin')
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.image = self.frames[int(self.frame_index)]
