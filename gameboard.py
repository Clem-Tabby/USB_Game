
import pygame
from coin import Coin
from obstacle import Obstacle
from player import Player
from settings import screen_height, screen_width, coin_spawn_percent, \
    background_color, obstacle_spawn_percent
import random
from sounds import bump, bling, hit

class Gameboard:

    def __init__(self, surface):
        self.surface = surface
        self.score = 0

        # Define sprite groups
        self.coins = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.player1 = Player((screen_width / 2, screen_height / 2))
        self.player.add(self.player1)

        # joystick setup
        self.joystick_count = pygame.joystick.get_count()
        if self.joystick_count == 0:
            print("Error: no joystick connected")
        else:
            self.my_joystick = pygame.joystick.Joystick(0)
            self.my_joystick.init()

    def draw_score(self, surface):
        score_string = 'SCORE: ' + str(self.score)
        score_font = pygame.font.Font('freesansbold.ttf', 25)
        score_text = score_font.render(score_string, True, (0, 0, 0))
        surface.blit(score_text, (10,10))

    # spawns coins randomly along right edge of board,
    # spawn_percent defines percentage chance that a coin spawns
    # per tick of the game clock
    def spawn_coins(self, coin_spawn_percent):
        if random.uniform(0, 100) <= coin_spawn_percent:
            coin = Coin((screen_width, int(random.uniform(35, screen_height - 16))))
            self.coins.add(coin)

    # functions similarly to spawn_coins method
    def spawn_obstacles(self, obstacle_spawn_percent):
        if random.uniform(0, 100) <= obstacle_spawn_percent:
            obstacle = Obstacle((screen_width, int(random.uniform(35, screen_height - 16))))
            self.obstacles.add(obstacle)

    def check_coin_collision(self):
        for coin in self.coins.sprites():
            if self.player1.rect.colliderect(coin.rect):
                coin.kill()
                bling.play()
                self.score += 100
            elif coin.rect.x < -coin.rect.width:
                coin.kill()

    def check_obstacle_collision(self):
        for obstacle in self.obstacles.sprites():
            if self.player1.rect.colliderect(obstacle.rect) and not obstacle.hit:
                obstacle.hit = True
                hit.play()
            elif obstacle.rect.x < -obstacle.rect.width:
                obstacle.kill()

    def run(self):
        if self.joystick_count != 0:
            horiz_axis_pos = self.my_joystick.get_axis(0)
            vert_axis_pos = self.my_joystick.get_axis(1)
            self.player1.update((horiz_axis_pos, vert_axis_pos))
        self.spawn_coins(coin_spawn_percent)
        self.spawn_obstacles(obstacle_spawn_percent)
        self.check_coin_collision()
        self.check_obstacle_collision()
        self.coins.update()
        self.obstacles.update()
        self.surface.fill(background_color)
        self.draw_score(self.surface)
        self.player.draw(self.surface)
        self.obstacles.draw(self.surface)
        self.coins.draw(self.surface)
        if self.player1.check_bump(screen_width, screen_height):
            bump.play()
