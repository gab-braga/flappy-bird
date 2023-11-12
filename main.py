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
FONT_POINTS = pygame.font.SysFont("arial", 50)

