
import pygame
from coin import Coin
from obstacle import Obstacle
from player import Player
from settings import screen_height, screen_width, coin_spawn_percent, \
    background_color, obstacle_spawn_percent
import random
from sounds import bump, bling, hit, dead, background_music, chibiNinja
from life_gauge import LifeGauge


class Gameboard:

    def __init__(self, surface):
        background_music.play(chibiNinja, loops=-1)
        self.surface = surface
        self.score = 0
        self.obstacle_spawn_percent = obstacle_spawn_percent

        # Define sprite groups
        self.coins = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.player1 = Player((screen_width / 2, screen_height / 2))
        self.player.add(self.player1)

        # Life gauge setup
        self.life_gauge = LifeGauge((650, 10))

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
        surface.blit(score_text, (10, 10))

    # spawns coins randomly along right edge of board,
    # spawn_percent defines percentage chance that a coin spawns
    # per tick of the game clock
    def spawn_coins(self, coin_spawn_percent):
        if random.uniform(0, 100) <= coin_spawn_percent:
            coin = Coin((screen_width, int(random.uniform(40, screen_height - 16))))
            self.coins.add(coin)

    # functions similarly to spawn_coins method, but slowly increases spawn percentage
    def spawn_obstacles(self, obstacle_spawn_percent):
        if random.uniform(0, 100) <= obstacle_spawn_percent:
            obstacle = Obstacle((screen_width, int(random.uniform(40, screen_height - 16))))
            self.obstacles.add(obstacle)
        self.obstacle_spawn_percent += 0.001

    # handles coin collisions with the player and cleans up off-screen coins
    def check_coin_collision(self):
        for coin in self.coins.sprites():
            if pygame.sprite.collide_mask(self.player1, coin) and self.player1.alive:
                coin.kill()
                bling.play()
                self.score += 100
            elif coin.rect.x < -coin.rect.width:
                coin.kill()

    # handles obstacle collisions with the player and cleans up off-screen obstacles
    def check_obstacle_collision(self):
        for obstacle in self.obstacles.sprites():
            if pygame.sprite.collide_mask(self.player1, obstacle) and not obstacle.hit and self.player1.alive:
                obstacle.hit = True
                hit.play()
                self.life_gauge.damage()
            elif obstacle.rect.x < -obstacle.rect.width:
                obstacle.kill()

    # handles events when player dies
    def check_death(self):
        if self.life_gauge.lives <= 0 and self.player1.alive:
            self.player1.alive = False
            background_music.pause()
            dead.play()
        if not self.player1.alive:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.reset()

    def reset(self):
        for coin in self.coins:
            coin.kill()
        for obstacle in self.obstacles:
            obstacle.kill()
        self.player1.rect.x = screen_width / 2
        self.player1.rect.y = screen_height / 2
        self.score = 0
        self.life_gauge.reset()
        self.player1.alive = True
        self.obstacle_spawn_percent = obstacle_spawn_percent
        background_music.unpause()

    def run(self):
        if self.joystick_count != 0:
            horiz_axis_pos = self.my_joystick.get_axis(0)
            vert_axis_pos = self.my_joystick.get_axis(1)
            self.player1.update((horiz_axis_pos, vert_axis_pos))
        self.spawn_coins(coin_spawn_percent)
        self.spawn_obstacles(self.obstacle_spawn_percent)
        self.check_coin_collision()
        self.check_obstacle_collision()
        self.life_gauge.update()
        if self.player1.alive:
            self.coins.update()
            self.obstacles.update()
        self.surface.fill(background_color)
        self.draw_score(self.surface)
        self.life_gauge.draw(self.surface)
        self.player.draw(self.surface)
        self.obstacles.draw(self.surface)
        self.coins.draw(self.surface)
        if self.player1.check_bump(screen_width, screen_height):
            bump.play()
        self.check_death()
        print(self.obstacle_spawn_percent)


