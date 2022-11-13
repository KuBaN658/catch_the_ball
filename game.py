import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))
fnt = pygame.font.Font(None, 64)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
hit = 0
miss = 0
def draw_interface():
    """
    рисует интерфейс игры
    :return: none
    """
    sc_text_hit = fnt.render("Hit", 1, GREEN, BLUE)
    sc_text_miss = fnt.render("Miss", 1, RED, YELLOW)
    screen.blit(sc_text_hit, (0, 0))
    screen.blit(sc_text_miss, (1100, 0))
    draw_miss()
    draw_hits()


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
        global hit
        hit += 1
        draw_hits()
    else:
        global miss
        miss += 1
        draw_miss()


def draw_hits():
    """
    Рисует количество попаданий
    :return:
    """
    sc_text_number_hits = fnt.render(str(hit), 1, GREEN, BLUE)
    screen.blit(sc_text_number_hits, (10, 50))


def draw_miss():
    """
    Рисует количество попаданий
    :return:
    """
    sc_text_number_hits = fnt.render(str(miss), 1, RED, YELLOW)
    screen.blit(sc_text_number_hits, (1130, 50))


draw_interface()
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
    draw_interface()

pygame.quit()
