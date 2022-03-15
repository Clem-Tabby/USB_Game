
import pygame
from heart import Heart


class LifeGuage(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.lives = 3
        self.rect = self.image.get_rect(topleft=pos)

    # reduce lives by 1
    def damage(self):
        self.lives -= 1

    def reset(self):
        self.lives = 3

    def update(self):
        self.animate()
