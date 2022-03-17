
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
        self.rect.inflate(-4, -8)
        self.hit = False

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    # updates player position based on incoming joystick tuple
    def update(self, new_pos):
        self.animate()
        scaled_pos = [int(i * 10) for i in new_pos]
        self.rect.x += -1 * scaled_pos[0]
        self.rect.y += scaled_pos[1]

    def check_bump(self, screen_width, screen_height):
        if self.rect.x < 0:
            self.rect.x = 0
            self.hit = True
        elif self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width
            self.hit = True
        elif self.rect.y < 35:
            self.rect.y = 35
            self.hit = True
        elif self.rect.y > screen_height - self.rect.height:
            self.rect.y = screen_height - self.rect.height
            self.hit = True
        else:
            self.hit = False
        return self.hit
