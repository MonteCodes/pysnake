import random
import pygame
import sys

from pygame.locals import *

from snake import Snake
from apple import Apple

FRAMES_PER_SECOND = 20
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
CELL_SIZE = 20
CELL_WIDTH = int(WINDOW_WIDTH / CELL_SIZE)
CELL_HEIGHT = int(WINDOW_HEIGHT / CELL_SIZE)

#               R    G    B
WHITE       = (255, 255, 255)
BLACK       = (  0,   0,   0)
RED         = (255,   0,   0)
GREEN       = (  0, 255,   0)
DARK_GREEN  = (  0, 155,   0)
DARK_GRAY   = ( 40,  40,  40)

BACKGROUND_COLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0


def main():
    global FPS_CLOCK, DISPLAY_SURFACE, BASIC_FONT

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BASIC_FONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake')

    show_start_screen()
    while True:
        run_game()
        show_game_over_screen()


def run_game():
    snake = Snake(CELL_WIDTH, CELL_HEIGHT)
    apple = Apple(CELL_WIDTH, CELL_HEIGHT)

    while True:
        check_for_movement(snake)

        if snake.check_collisions():
            return

        if snake.check_apple_collision(apple):
            apple.move()
        else:
            del snake.coords[-1]

        snake.change_directions()

        DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
        draw_grid()
        snake.draw(DISPLAY_SURFACE, CELL_SIZE)
        apple.draw(DISPLAY_SURFACE, CELL_SIZE)
        draw_score(len(snake.coords) - 3)
        pygame.display.update()
        FPS_CLOCK.tick(FRAMES_PER_SECOND)


def check_for_key_press():
    key_up_events = pygame.event.get()
    if len(key_up_events) == 0:
        return None
    if key_up_events[0] == K_ESCAPE:
        terminate()
    return key_up_events[0]


def check_for_movement(snake):
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYDOWN:
            if (event.key == K_LEFT or event.key == K_a) and snake.direction != RIGHT:
                snake.direction = LEFT
            elif (event.key == K_RIGHT or event.key == K_d) and snake.direction != LEFT:
                snake.direction = RIGHT
            elif (event.key == K_UP or event.key == K_w) and snake.direction != DOWN:
                snake.direction = UP
            elif (event.key == K_DOWN or event.key == K_s) and snake.direction != UP:
                snake.direction = DOWN


def show_start_screen():
    title_font = pygame.font.Font('freesansbold.ttf', 100)
    title_surface_one = title_font.render('Snake!', True, WHITE, DARK_GREEN)
    title_surface_two = title_font.render('Snake!', True, GREEN)

    degrees_one = 0
    degrees_two = 0

    while True:
        DISPLAY_SURFACE.fill(BACKGROUND_COLOR)

        rotated_surface_one = pygame.transform.rotate(title_surface_one, degrees_one)
        rotated_rect_one = rotated_surface_one.get_rect()
        rotated_rect_one.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        DISPLAY_SURFACE.blit(rotated_surface_one, rotated_rect_one)

        rotated_surface_two = pygame.transform.rotate(title_surface_two, degrees_two)
        rotated_rect_two = rotated_surface_two.get_rect()
        rotated_rect_two.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        DISPLAY_SURFACE.blit(rotated_surface_two, rotated_rect_two)

        draw_press_key_message()

        if check_for_key_press():
            pygame.event.get()
            return
        pygame.display.update()
        FPS_CLOCK.tick(FRAMES_PER_SECOND)
        degrees_one += 3
        degrees_two += 7


def show_game_over_screen():
    game_over_font = pygame.font.Font('freesansbold.ttf', 150)

    game_surface = game_over_font.render('GAME', True, WHITE)
    game_rect = game_surface.get_rect()
    game_rect.midtop = (WINDOW_WIDTH / 2, 10)

    over_surface = game_over_font.render('OVER', True, WHITE)
    over_rect = over_surface.get_rect()
    over_rect.midtop = (WINDOW_WIDTH / 2, game_rect.height + 35)

    DISPLAY_SURFACE.blit(game_surface, game_rect)
    DISPLAY_SURFACE.blit(over_surface, over_rect)
    draw_press_key_message()
    pygame.display.update()
    pygame.time.wait(500)
    check_for_key_press()

    while True:
        if check_for_key_press():
            pygame.event.get()
            return


def draw_press_key_message():
    press_key_surface = BASIC_FONT.render('Press a key to play.', True, WHITE)
    press_key_rect = press_key_surface.get_rect()
    press_key_rect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
    DISPLAY_SURFACE.blit(press_key_surface, press_key_rect)


def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(DISPLAY_SURFACE, DARK_GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(DISPLAY_SURFACE, DARK_GRAY, (0, y), (WINDOW_WIDTH, y))


def draw_score(score):
    score_surface = BASIC_FONT.render('Score: %s' % score, True, WHITE)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (WINDOW_WIDTH - 120, 10)
    DISPLAY_SURFACE.blit(score_surface, score_rect)


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()