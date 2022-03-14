
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        image = pygame.image.load('graphics/player/Bucket Truck.png').convert_alpha()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.hit = False
        self.old_x = 0
        self.old_y = 0

# updates player position based on incoming joystick tuple
    def update(self, new_pos):
        self.old_x = self.rect.x
        self.old_y = self.rect.y
        scaled_pos = [int(i * 10) for i in new_pos]
        self.rect.x += -1 * scaled_pos[0]
        self.rect.y += scaled_pos[1]

    def check_bump(self, screen_width, screen_height):
        if self.rect.x < 0:
            self.rect.x = 0
            if self.old_x != 0:
                self.hit = True
        elif self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width
            self.hit = True
        elif self.rect.y < 0:
            self.rect.y = 0
            self.hit = True
        elif self.rect.y > screen_height - self.rect.height:
            self.rect.y = screen_height - self.rect.height
            self.hit = True
        else:
            self.hit = False
        return self.hit
