
import pygame
from support import import_folder


class Heart(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.broken = False
        self.frames = import_folder('./graphics/heart')
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    def animate(self):
        if self.frame_index <= len(self.frames) - 1:
            self.frame_index += self.animation_speed
        self.image = self.frames[int(self.frame_index)]

    def reset(self):
        self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        if self.broken:
            self.animate()
