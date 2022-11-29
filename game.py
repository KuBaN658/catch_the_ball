import pygame
import draws as ds
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








clock = pygame.time.Clock()
finished = ds.takes_the_name(screen, BLACK, WHITE, fnt, clock)

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
    ds.save_in_rating(NAME, hit, miss)

pygame.quit()
