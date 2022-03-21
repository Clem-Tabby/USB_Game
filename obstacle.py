
import pygame
import random
from support import import_folder
from settings import obstacle_speed


# Obstacle objects are selected randomly
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.hit = False
        self.played_hit_sound = False
        self.speed = obstacle_speed
        self.obstacle_choices = ['rock', 'trashcan', 'cone']
        self.frames = import_folder('./graphics/obstacles/' + random.choice(self.obstacle_choices))
        self.frame_index = 0
        self.animation_speed = 0.2
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    def animate_hit(self):
        if self.frame_index <= len(self.frames) - 1:
            self.frame_index += self.animation_speed
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.rect.x -= self.speed
        if self.hit:
            self.animate_hit()
