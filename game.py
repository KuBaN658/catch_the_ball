import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 75
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
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
hit = 0
miss = 0
ball_number = 7
ball_colorful_number = 3
X = [0]*(ball_number + ball_colorful_number)
Y = [0]*(ball_number + ball_colorful_number)
R = [0]*(ball_number + ball_colorful_number)
VX = [0]*(ball_number + ball_colorful_number)
VY = [0]*(ball_number + ball_colorful_number)
COLOR = [0]*(ball_number + ball_colorful_number)
SECOND_COLOR = [0]*(ball_number + ball_colorful_number)
THIRD_COLOR = [0]*(ball_number + ball_colorful_number)
count_number_ball = 0
AX = 0.5
AY = -0.5
NAME = ""


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
    добавляет очередной одноцветный шарик
    :param index: индекск шарика в массивах данных
    :return: None
    """
    global X, Y, R, VX, VY, COLOR
    X[index] = randint(200, 1000)
    Y[index] = randint(200, 800)
    R[index] = randint(40, 80)
    VX[index] = randint(-10, 10)
    VY[index] = randint(-10, 10)
    COLOR[index] = COLORS[randint(0, 5)]
    circle(screen, COLOR[index], (X[index], Y[index]), R[index])


def new_colorful_ball(index):
    """
    Рисует трехцветный круг
    :param index: индекск шарика в массивах данных
    :return: None
    """
    X, Y, R, VX, VY, COLOR, SECOND_COLOR, THIRD_COLOR
    X[index] = randint(200, 1000)
    Y[index] = randint(200, 800)
    R[index] = randint(40, 80)
    VX[index] = randint(-10, 10)
    VY[index] = randint(-10, 10)
    COLOR[index] = COLORS[randint(0, 1)]
    SECOND_COLOR[index] = COLORS[randint(2, 3)]
    THIRD_COLOR[index] = COLORS[randint(4, 5)]
    circle(screen, COLOR[index], (X[index], Y[index]), R[index])
    circle(screen, SECOND_COLOR[index], (X[index], Y[index]), R[index]*0.66)
    circle(screen, THIRD_COLOR[index], (X[index], Y[index]), R[index]*0.33)


def move_ball():
    """
    смещает круги на экране
    :return: None
    """
    global X, Y, VX, VY

    for i in range(ball_number + ball_colorful_number):
        if i < 7:
            if X[i] - R[i] <= 0:
                VX[i] = -VX[i]
            elif X[i] + R[i] >= 1200:
                VX[i] = -VX[i]
            elif Y[i] - R[i] <= 0:
                VY[i] = -VY[i]
            elif Y[i] + R[i] >= 900:
                VY[i] = -VY[i]
            X[i] = X[i] + VX[i]
            Y[i] = Y[i] + VY[i]
            circle(screen, COLOR[i], (X[i], Y[i]), R[i])
        else:
            VX[i] += AX
            VY[i] += AY
            X[i] = X[i] + VX[i]
            Y[i] = Y[i] + VY[i]
            if X[i] - R[i] <= 0:
                VX[i] = randint(1, 10)
                VY[i] = randint(1, 10)
            elif X[i] + R[i] >= 1200:
                VX[i] = -randint(1, 10)
                VY[i] = -randint(1, 10)
            elif Y[i] - R[i] <= 0:
                VX[i] = randint(1, 10)
                VY[i] = randint(1, 10)
            elif Y[i] + R[i] >= 900:
                VX[i] = -randint(1, 10)
                VY[i] = -randint(1, 10)
            circle(screen, COLOR[i], (X[i], Y[i]), R[i])
            circle(screen, SECOND_COLOR[i], (X[i], Y[i]), R[i]*0.66)
            circle(screen, THIRD_COLOR[i], (X[i], Y[i]), R[i]*0.33)


def is_hit_the_mark(even):
    """
    подсчитывает количество попаданий и промахов.
    Начисляет очки за поадания
    :param even: обьект события
    :return: возвращает True если есть попадание и False если промах
    """
    global miss, hit
    x, y = even.pos
    for i in range(ball_number + ball_colorful_number):
        diff_x = abs(X[i] - x)
        diff_y = abs(Y[i] - y)
        if i >= 7 and (diff_x**2 + diff_y**2)**0.5 <= R[i]*0.33:
            hit += 3
            draw_hits()
            R[i] = 0
            return True
        elif i >= 7 and (diff_x**2 + diff_y**2)**0.5 <= R[i]*0.66:
            hit += 2
            draw_hits()
            R[i] = 0
        elif (diff_x**2 + diff_y**2)**0.5 <= R[i]:
            hit += 1
            draw_hits()
            R[i] = 0
            return True
        elif i == 9:
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


def draw_prompt():
    """
    Рисует подсказку о том, что нужно ввести имя
    :return: None
    """
    surf_text = fnt.render("Введите свое имя:", True, WHITE)
    screen.blit(surf_text, (400, 350))


def draw_results():
    """
    рисует рэйтинг игроков
    :return: None
    """
    with open("rating.txt") as file:
        y = 50
        for line in file:
            line = line[:-1]
            surf_text = fnt.render(line, True, WHITE)
            screen.blit(surf_text, (100, y))
            y += 50


def takes_the_name():
    """
    Принимает имя игрока и сохраняет его в глобальную переменную
    :return: None
    """
    global NAME
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(450, 400, 300, 32)
    color_inactive = pygame.Color(GREEN)
    color_active = pygame.Color(RED)
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    tab = True
                    while tab:
                        screen.fill(BLACK)
                        draw_results()
                        pygame.display.update()
                        for events in pygame.event.get():
                            if events.type == pygame.KEYUP:
                                if events.key == pygame.K_TAB:
                                    tab = False
                if active:
                    if event.key == pygame.K_RETURN:
                        NAME = text
                        return False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(BLACK)
        draw_prompt()
        txt_surface = font.render(text, True, BLUE)
        width = max(300, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 1)

        pygame.display.update()
        clock.tick(FPS)



def save_in_rating():
    """
    сохраняет результат игрока в рейтинг
    :return: None
    """
    with open("rating.txt", 'a') as file:
        print(NAME, "-", hit - miss, file=file)


clock = pygame.time.Clock()
finished = takes_the_name()

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
            if count_number_ball % 10 < 7:
                new_ball(count_number_ball % 10)
            else:
                new_colorful_ball(count_number_ball % 10)
        if count % 20 == 0:
            AX = -AX
            AY = -AY

        move_ball()
        draw_interface()
        pygame.display.update()
        count += 1

if NAME != "":
    save_in_rating()

pygame.quit()
