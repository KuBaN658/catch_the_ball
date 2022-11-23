from random import randint
from pygame.draw import circle
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
