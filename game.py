import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
difficulty = 1
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
    global X, Y, R, DX, DY, color
    X = randint(200, 1000)
    Y = randint(200, 800)
    R = randint(11, 100)
    DX = randint(-10, 10)
    DY = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (X, Y), R)


def move_ball():
    """
    смещает круг
    :return: None
    """
    global X, Y, DX, DY
    X = X + DX
    Y = Y + DY
    if X - R <= 0:
        DX = -DX
    elif X + R >= 1200:
        DX = -DX
    elif Y - R <= 0:
        DY = -DY
    elif Y + R >= 900:
        DY = -DY
    circle(screen, color, (X, Y), R)


def is_hit_the_mark(event):
    """
    подсчитывает количество попаданий и промахов
    :param event: обьект события
    :return: возвращает True если есть попадание и False если промах
    """
    x, y = event.pos
    diff_x = abs(X - x)
    diff_y = abs(Y - y)
    if (diff_x**2 + diff_y**2)**0.5 <= R:
        global hit
        hit += 1
        draw_hits()
        return True
    else:
        global miss
        miss += 1
        draw_miss()
        return False


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
    clock.tick(difficulty)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    new_ball()
    pygame.display.update()
    draw_interface()
    is_hit = False

    while not is_hit:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_hit = True
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                is_hit = is_hit_the_mark(event)

        screen.fill(BLACK)
        move_ball()
        draw_interface()
        pygame.display.update()


pygame.quit()
