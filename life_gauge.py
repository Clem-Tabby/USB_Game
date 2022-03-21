
import pygame
from heart import Heart


class LifeGauge(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.lives = 3
        self.pos = pos
        self.heart3 = Heart(self.pos)
        self.heart2 = Heart((self.heart3.rect.topright[0] + 5, self.pos[1]))
        self.heart1 = Heart((self.heart2.rect.topright[0] + 5, self.pos[1]))
        self.hearts = pygame.sprite.Group()
        self.hearts.add(self.heart1, self.heart2, self.heart3)

    def draw(self, surface):
        self.hearts.draw(surface)

    # reduce lives by 1 and animate heart breaking
    def damage(self):
        self.lives -= 1
        if self.lives == 2:
            self.heart1.broken = True
        elif self.lives == 1:
            self.heart2.broken = True
        elif self.lives == 0:
            self.heart3.broken = True

    # reset hearts
    def reset(self):
        self.lives = 3
        for heart in self.hearts:
            heart.reset()

    def update(self):
        self.heart1.update()
        self.heart2.update()
        self.heart3.update()
