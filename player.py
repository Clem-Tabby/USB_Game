
import pygame
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = import_folder('./graphics/player')
        image = self.frames[self.frame_index]
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.hit = False
        self.alive = True

    def animate(self):
        if self.alive:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.frames):
                self.frame_index = 0
            self.image = self.frames[int(self.frame_index)]
        else:
            pass

    # updates player position based on incoming joystick tuple
    def update(self, new_pos):
        self.animate()
        if self.alive:
            scaled_pos = [int(i * 4) for i in new_pos]
            self.rect.x += -0.6 * scaled_pos[0]
            self.rect.y += scaled_pos[1]

    def check_bump(self, screen_width, screen_height):
        if self.rect.x < 0:
            self.rect.x = 0
            self.hit = True
        elif self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width
            self.hit = True
        elif self.rect.y < 40:
            self.rect.y = 40
            self.hit = True
        elif self.rect.y > screen_height - self.rect.height:
            self.rect.y = screen_height - self.rect.height
            self.hit = True
        else:
            self.hit = False
        return self.hit
