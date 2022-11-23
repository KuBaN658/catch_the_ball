import pygame
import pickle
import draws as ds
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






def draw_prompt():
    """
    Рисует подсказку о том, что нужно ввести имя
    :return: None
    """
    surf_text = fnt.render("Введите свое имя:", True, WHITE)
    screen.blit(surf_text, (400, 350))


def draw_results():
    """
    рисует рэйтинг Топ-3 игроков
    :return: None
    """
    with open("rating.bin", "rb") as file:
        rating = pickle.load(file)

    y = 50
    first = 0
    second = 0
    third = 0
    first_name = ""
    second_name = ""
    third_name = ""
    for name in rating:
        if first < rating[name]:
            third_name = second_name
            second_name = first_name
            first = rating[name]
            first_name = name
        elif second < rating[name]:
            third_name = second_name
            second = rating[name]
            second_name = name
        elif third < rating[name]:
            third = rating[name]
            third_name = name

    array_names = [first_name, second_name, third_name]

    for i in array_names:
        surf_text = fnt.render(i + " " + str(rating[i]), True, WHITE)
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
                elif active:
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
    with open("rating.bin", "rb") as file:
        rating = pickle.load(file)
        rating[NAME] = hit - miss
    with open("rating.bin", 'wb') as file:
        pickle.dump(rating, file)


clock = pygame.time.Clock()
finished = takes_the_name()

while not finished:
    clock.tick(difficulty)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    ds.draw_interface(screen, fnt, miss, hit)
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
                is_hit, hit, miss = ds.is_hit_the_mark(event, screen, fnt, X, Y, R, ball_number, ball_colorful_number, hit, miss)

        screen.fill(BLACK)
        if count % 100 == 0 and count > 0:
            count_number_ball += 1
            if count_number_ball % 10 < 7:
                X, Y, R, VX, VY, COLOR = ds.new_ball(count_number_ball % 10,
                                                     COLORS, screen, X, Y, R, VX, VY, COLOR)
            else:
                X, Y, R, VX, VY, COLOR, SECOND_COLOR, THIRD_COLOR = \
                    ds.new_colorful_ball(count_number_ball % 10, COLORS, screen,
                                         X, Y, R, VX, VY, COLOR, SECOND_COLOR, THIRD_COLOR)
        if count % 20 == 0:
            AX = -AX
            AY = -AY

        X, Y, VX, VY = ds.move_ball(screen, X, Y, R, VX, VY, AX, AY, COLOR,
                                    SECOND_COLOR, THIRD_COLOR, ball_number, ball_colorful_number)
        ds.draw_interface(screen, fnt, miss, hit)
        pygame.display.update()
        count += 1

if NAME != "":
    save_in_rating()

pygame.quit()
