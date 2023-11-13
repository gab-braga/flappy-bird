import pygame
import os
import random

WIDTH_SCREEN = 500
HEIGHT_SCREEN = 800


def scale(img):
    return pygame.transform.scale2x(img)


IMG_OBSTACLE = scale(pygame.image.load(os.path.join("imgs", "pipe.png")))
IMG_BASE = scale(pygame.image.load(os.path.join("imgs", "base.png")))
IMG_BACKGROUND = scale(pygame.image.load(os.path.join("imgs", "bg.png")))
IMG_BIRD = [
    scale(pygame.image.load(os.path.join("imgs", "bird1.png"))),
    scale(pygame.image.load(os.path.join("imgs", "bird2.png"))),
    scale(pygame.image.load(os.path.join("imgs", "bird3.png")))
]

pygame.font.init()
FONT_POINTS = pygame.font.SysFont("arial", 25)

class Bird:
    SPRITES = IMG_BIRD
    MAX_ROTATE = 25
    SPEED_ROTATE = 20
    TIME_ANIMATION = 5

    def __init__(self, x, y):
        self.x = y
        self.y = y
        self.ang = 0
        self.speed = 0
        self.height = self.y
        self.time = 0
        self.count_mode = 0
        self.sprite = self.SPRITES[0]

    def jump(self):
        self.speed = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
        # calcular deslocamento
        self.time += 1
        displacement = 1.5 * self.time ** 2 + self.speed * self.time

        # restringir deslocamento
        if displacement > 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 2
        self.y += displacement

        # calcular angulo
        if displacement < 0 or self.y < (self.height + 50):
            if self.ang < self.MAX_ROTATE:
                self.ang = self.MAX_ROTATE
        else:
            if self.ang > -90:
                self.ang -= self.SPEED_ROTATE

    def draw(self, screen):
        # definir a imagem a desenhar
        self.count_mode += 1
        if self.count_mode < self.TIME_ANIMATION:
            self.sprite = self.SPRITES[0]
        elif self.count_mode < self.TIME_ANIMATION * 2:
            self.sprite = self.SPRITES[1]
        elif self.count_mode < self.TIME_ANIMATION * 3:
            self.sprite = self.SPRITES[2]
        elif self.count_mode < self.TIME_ANIMATION * 4:
            self.sprite = self.SPRITES[1]
        elif self.count_mode < self.TIME_ANIMATION * 4 + 1:
            self.sprite = self.SPRITES[0]
            self.count_mode = 0

        # verificar se o passaro cai
        if self.ang <= -80:
            self.sprite = self.SPRITES[1]
            self.count_mode = self.TIME_ANIMATION * 2

        # desenhar o passaro
        sprite_rotate = pygame.transform.rotate(self.sprite, self.ang)
        pos_center = self.sprite.get_rect(topleft=(self.x, self.y)).center
        node = sprite_rotate.get_rect(center=pos_center)
        screen.blit(sprite_rotate, node.topleft)

    def get_mask(self):
        pygame.mask.from_surface(self.sprite)

class Obstacle:
    DISTANCE = 200
    SPEED = 5
    SPRITE_TOP = pygame.transform.flip(IMG_OBSTACLE, False, True)
    SPRITE_BASE = IMG_OBSTACLE

    def __int__(self, x):
        self.x = x
        self.height = 0
        self.pos_top = 0
        self.pos_base = 0
        self.surpassed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.pos_top = self.height - self.SPRITE_TOP.get_height()
        self.pos_base = self.height + self.DISTANCE

    def move(self):
        self.x -= self.SPEED

    def draw(self, screen):
        screen.blit(self.SPRITE_TOP, (self.x, self.pos_top))
        screen.blit(self.SPRITE_BASE, (self.x, self.pos_base))

    def get_mask(self):
        pygame.mask.from_surface(self.sprite)

    def check_collision(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.SPRITE_TOP)
        base_mask = pygame.mask.from_surface(self.SPRITE_BASE)

        distance_top = (self.x - bird.x, self.pos_top - round(bird.y))
        distance_base = (self.x - bird.x, self.pos_base - round(bird.y))

        top_collision = bird_mask.overlap(top_mask, distance_top)
        base_collision = bird_mask.overlap(base_mask, distance_base)

        return top_collision or base_collision


class Base:
    pass