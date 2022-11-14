import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 120
difficulty = 2
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
ball_number = 10
X = [0]*ball_number
Y = [0]*ball_number
R = [0]*ball_number
VX = [0]*ball_number
VY = [0]*ball_number
COLOR = [0]*ball_number
count_number_ball = 0


def draw_interface():
    """
    рисует интерфейс игры
    :return: none
    """
    sc_text_hit = fnt.render("Попадания", True, GREEN, BLUE)
    sc_text_miss = fnt.render("Промахи", True, RED, YELLOW)
    screen.blit(sc_text_hit, (0, 0))
    screen.blit(sc_text_miss, (1010, 0))
    draw_miss()
    draw_hits()


def new_ball(index):
    """
    добавляет очередной шарик
    :return: None
    """
    global X, Y, R, VX, VY, COLOR
    X[index] = randint(200, 1000)
    Y[index] = randint(200, 800)
    R[index] = randint(11, 100)
    VX[index] = randint(-10, 10)
    VY[index] = randint(-10, 10)
    COLOR[index] = COLORS[randint(0, 5)]
    circle(screen, COLOR[index], (X[index], Y[index]), R[index])


def move_ball():
    """
    смещает круги на экране
    :return: None
    """
    global X, Y, VX, VY
    for i in range(ball_number):
        X[i] = X[i] + VX[i]
        Y[i] = Y[i] + VY[i]
        if X[i] - R[i] <= 0:
            VX[i] = -VX[i]
        elif X[i] + R[i] >= 1200:
            VX[i] = -VX[i]
        elif Y[i] - R[i] <= 0:
            VY[i] = -VY[i]
        elif Y[i] + R[i] >= 900:
            VY[i] = -VY[i]
        circle(screen, COLOR[i], (X[i], Y[i]), R[i])


def is_hit_the_mark(even):
    """
    подсчитывает количество попаданий и промахов
    :param even: обьект события
    :return: возвращает True если есть попадание и False если промах
    """
    x, y = even.pos
    for i in range(ball_number):
        print(i)
        diff_x = abs(X[i] - x)
        diff_y = abs(Y[i] - y)
        print(diff_x, diff_y)
        if (diff_x**2 + diff_y**2)**0.5 <= R[i]:
            global hit
            hit += 1
            draw_hits()
            R[i] = 0
            return True
        elif i == 9:
            global miss
            miss += 1
            draw_miss()
            return False


def draw_hits():
    """
    Рисует количество попаданий
    :return:
    """
    sc_text_number_hits = fnt.render(str(hit), True, GREEN, BLUE)
    screen.blit(sc_text_number_hits, (50, 50))


def draw_miss():
    """
    Рисует количество попаданий
    :return: None
    """
    sc_text_number_hits = fnt.render(str(miss), True, RED, YELLOW)
    screen.blit(sc_text_number_hits, (1130, 50))


draw_interface()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(difficulty)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    draw_interface()
    pygame.display.update()
    is_hit = False
    count = 0
    while not is_hit:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_hit = True
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                is_hit = is_hit_the_mark(event)

        screen.fill(BLACK)
        if count % 100 == 0 and count > 0:
            count_number_ball += 1
            new_ball(count_number_ball % 10)
        move_ball()
        draw_interface()
        pygame.display.update()
        count += 1


pygame.quit()
