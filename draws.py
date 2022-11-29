from random import randint
from pygame.draw import circle
import pickle
import pygame

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


def draw_hits(surface, font, hit):
    """
    рисует количество попаданий
    :param surface: поверхность для отображения
    :param font: шрифт
    :param hit: количество попаданий
    :return: None
    """
    sc_text_number_hits = font.render(str(hit), True, GREEN, BLUE)
    surface.blit(sc_text_number_hits, (50, 50))


def draw_miss(surface, font, miss):
    """
    рисует количество попаданий
    :param surface: поверхность для отображения
    :param font: шрифт
    :param miss: количество промахов
    :return: None
    """
    sc_text_number_hits = font.render(str(miss), True, RED, YELLOW)
    surface.blit(sc_text_number_hits, (1130, 50))


def draw_interface(surface, font, miss, hit, color_font_hit=GREEN,
                   color_background_hit=BLUE, color_font_miss=RED, color_background_miss=YELLOW):
    """
    рисует промахи и попадания в игре
    :param surface: поверхность для отображения
    :param font: шрифт
    :param miss: количество промахов
    :param hit: количество попаданий
    :param color_font_hit: цвет шрифта попаданий
    :param color_background_hit: цвет фона попаданий
    :param color_font_miss: цвет шрифта промахов
    :param color_background_miss: цвет фона промахов
    :return: None
    """
    sc_text_hit = font.render("Попадания", True, GREEN, BLUE)
    sc_text_miss = font.render("Промахи", True, RED, YELLOW)
    surface.blit(sc_text_hit, (0, 0))
    surface.blit(sc_text_miss, (1010, 0))
    draw_miss(surface, font, miss)
    draw_hits(surface, font, hit)


def new_ball(index, COLORS, surface, X, Y, R, VX, VY, COLOR):
    """
    создает новый круг
    :param index: индекс в массивах для хранения данных о круге
    :param COLORS: массив цветов
    :param surface: поверхность для рисования
    :param X: Координата х центра шарика
    :param Y: координата y центра шарика
    :param R: радиус шарика
    :param VX: скорость по абциссе
    :param VY: скорость по ординате
    :param COLOR: цвет шарика
    :return: X, Y, R, VX, VY, COLOR
    """
    X[index] = randint(200, 1000)
    Y[index] = randint(200, 800)
    R[index] = randint(40, 80)
    VX[index] = randint(-10, 10)
    VY[index] = randint(-10, 10)
    COLOR[index] = COLORS[randint(0, 5)]
    circle(surface, COLOR[index], (X[index], Y[index]), R[index])
    return X, Y, R, VX, VY, COLOR


def new_colorful_ball(index, COLORS, surface, X, Y, R, VX, VY, COLOR, SECOND_COLOR, THIRD_COLOR):
    """
    создает новый цветной круг
    :param index: индекс в массивах для хранения данных о круге
    :param COLORS: массив цветов
    :param surface: поверхность для рисования
    :param X: координата х центра круга
    :param Y: координата у центра круга
    :param R: радиус круга
    :param VX: скорость по абциссе
    :param VY: скорость по ординате
    :param COLOR: цвет наружней части
    :param SECOND_COLOR: цвет средней части
    :param THIRD_COLOR: цвет центральной части
    :return: X, Y, R, VX, VY, COLOR, SECOND_COLOR, THIRD_COLOR
    """
    X[index] = randint(200, 1000)
    Y[index] = randint(200, 800)
    R[index] = randint(40, 80)
    VX[index] = randint(-10, 10)
    VY[index] = randint(-10, 10)
    COLOR[index] = COLORS[randint(0, 1)]
    SECOND_COLOR[index] = COLORS[randint(2, 3)]
    THIRD_COLOR[index] = COLORS[randint(4, 5)]
    circle(surface, COLOR[index], (X[index], Y[index]), R[index])
    circle(surface, SECOND_COLOR[index], (X[index], Y[index]), R[index]*0.66)
    circle(surface, THIRD_COLOR[index], (X[index], Y[index]), R[index]*0.33)
    return X, Y, R, VX, VY, COLOR, SECOND_COLOR, THIRD_COLOR


def move_ball(surface, X, Y, R, VX, VY, AX, AY, COLOR, SECOND_COLOR, THIRD_COLOR, ball_number, ball_colorful_number):
    """
    отрисовывает движение шариков
    :param surface: поверхность для рисования
    :param X: х центра круга
    :param Y: у центра круга
    :param R: радиус круга
    :param VX: скорость по х
    :param VY: скорость по у
    :param AX: ускорение по х
    :param AY: ускорение по у
    :param COLOR: цвет круга
    :param SECOND_COLOR: второй цвет круга
    :param THIRD_COLOR: третий цвет круга
    :param ball_number: количество обычных кругов
    :param ball_colorful_number: количество цветных кругов
    :return: None
    """
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
            circle(surface, COLOR[i], (X[i], Y[i]), R[i])
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
            circle(surface, COLOR[i], (X[i], Y[i]), R[i])
            circle(surface, SECOND_COLOR[i], (X[i], Y[i]), R[i]*0.66)
            circle(surface, THIRD_COLOR[i], (X[i], Y[i]), R[i]*0.33)
    return X, Y, VX, VY


def is_hit_the_mark(even, surface, font, X, Y, R, ball_number, ball_colorful_number, hit, miss):
    """
    подсчитывает количество попаданий и промахов.
    Начисляет очки за поадания
    :param even: обьект события
    :return: возвращает True если есть попадание и False если промах
    """
    x, y = even.pos
    for i in range(ball_number + ball_colorful_number):
        diff_x = abs(X[i] - x)
        diff_y = abs(Y[i] - y)
        if i >= 7 and (diff_x**2 + diff_y**2)**0.5 <= R[i]*0.33:
            hit += 3
            draw_hits(surface, font, hit)
            R[i] = 0
            return True, hit, miss
        elif i >= 7 and (diff_x**2 + diff_y**2)**0.5 <= R[i]*0.66:
            hit += 2
            draw_hits(surface, font, hit)
            R[i] = 0
            return True, hit, miss
        elif (diff_x**2 + diff_y**2)**0.5 <= R[i]:
            hit += 1
            draw_hits(surface, font, hit)
            R[i] = 0
            return True, hit, miss
        elif i == 9:
            miss += 1
            draw_miss(surface, font, hit)
            return False, hit, miss


def draw_prompt(surface, font, color, coords):
    """
    рисует подсказку что надо ввести имя
    :param surface: поверохность для рисования
    :param font: шрифт написания подсказки
    :param color: цвет шрифта
    :return: None
    """
    surf_text = font.render("Введите свое имя:", True, color)
    surface.blit(surf_text, coords)


def draw_results(surface, font, color):
    """
    Рисует рейтинг игроков
    :param surface: поверхность для рисования
    :param font: шрифт написания рейтинга
    :param color: цвет шрифта
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
            first_name = name
            third = second
            second = first
            first = rating[name]
        elif second < rating[name]:
            third_name = second_name
            second_name = name
            third = second
            second = rating[name]
        elif third < rating[name]:
            third = rating[name]
            third_name = name

    array_names = [first_name, second_name, third_name]
    for i in array_names:
        surf_text = font.render(i + " " + str(rating[i]), True, color)
        surface.blit(surf_text, (100, y))
        y += 50


def draws_start_game(surface, background, font, color_prompt, color_rect, text, input_box, clock):
    """
    рисует интерфейс ввода имени игрока
    :param surface: поверхность для рисования
    :param background: цвет заднего фона
    :param font: шрифт
    :param color: цвет шрифта
    :param text: текст
    :param input_box: прямоугольник ввода имени
    :param clock: количество обновлений монитора
    :return: None
    """
    surface.fill(background)
    draw_prompt(surface, font, color_prompt, (450, 350))
    txt_surface = font.render(text, True, BLUE)
    width = max(300, txt_surface.get_width() + 10)
    input_box.w = width
    surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(surface, color_rect, input_box, 1)

    pygame.display.update()
    clock.tick(1)


def save_in_rating(NAME, hit, miss):
    """
    Если результат игрока улучшен или это новый игрок данные добавляются в словарь
    :param NAME: Имя игрока
    :param hit: количество попаданий
    :param miss: количество промахов
    :return: None
    """
    with open("rating.bin", "rb") as file:
        rating = pickle.load(file)
        if rating[NAME] < hit - miss:
            rating[NAME] = hit - miss
    with open("rating.bin", 'wb') as file:
        pickle.dump(rating, file)


def takes_the_name(surface, color_background, color_text, font, FPS, clock):
    """
    получает имя игрока и выводит общий рейтинг
    :param surface: поверхность для рисования
    :param color_background: цвет фона
    :param color_text: цвет текста
    :param font: шрифт
    :param clock: частота обновления экрана
    :return: None
    """
    global NAME
    font_prompt = pygame.font.Font(None, 48)
    input_box = pygame.Rect(450, 400, 300, 40)
    color_inactive = pygame.Color(GREEN)
    color_active = pygame.Color(RED)
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        clock.tick(FPS)
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
                        surface.fill(color_background)
                        draw_results(surface, font, color_text)
                        pygame.display.update()
                        for events in pygame.event.get():
                            if events.type == pygame.KEYUP:
                                if events.key == pygame.K_TAB:
                                    draws_start_game(surface, color_background, font_prompt,
                                                     color_text, color, text, input_box, clock)
                                    tab = False
                elif active:
                    if event.key == pygame.K_RETURN:
                        NAME = text
                        return False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        draws_start_game(surface, color_background, font_prompt, color_text, color, text,
                         input_box, clock)
