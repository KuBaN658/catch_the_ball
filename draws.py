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


def draw_interface(surface, font, miss, hit, color_font_hit=GREEN, color_background_hit=BLUE, color_font_miss=RED, color_background_miss=YELLOW):
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
