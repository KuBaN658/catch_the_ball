import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """
    рисует новый шарик
    :return: None
    """
    global X, Y, R
    X = randint(100, 1100)
    Y = randint(100, 900)
    R = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (X, Y), R)


def click():
    """
    печатает координаты и радиус круга
    :return: None
    """
    print(X, Y, R)


def is_hit_the_mark(event):
    """
    печатает ок если есть попадание в круг
    :param event: обьект события
    :return: None
    """
    x, y = event.pos
    diff_x = abs(X - x)
    diff_y = abs(Y - y)
    if (diff_x**2 + diff_y**2)**0.5 <= R:
        print("ок")


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            is_hit_the_mark(event)

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
