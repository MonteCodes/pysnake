import random
import pygame
from pygame.locals import *

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

GREEN       = (  0, 255,   0)
DARK_GREEN  = (  0, 155,   0)

HEAD = 0


class Snake:

    def __init__(self, cell_width, cell_height):
        self.cell_width = cell_width
        self.cell_height = cell_height

        self.starting_x = random.randint(5, self.cell_width - 6)
        self.starting_y = random.randint(5, self.cell_height - 6)

        self.coords = [{'x': self.starting_x, 'y': self.starting_y},
                       {'x': self.starting_x - 1, 'y': self.starting_y},
                       {'x': self.starting_x - 2, 'y': self.starting_y}]

        self.direction = RIGHT

    def change_directions(self):
        if self.direction == UP:
            new_head = {'x': self.coords[HEAD]['x'], 'y': self.coords[HEAD]['y'] - 1}
        elif self.direction == DOWN:
            new_head = {'x': self.coords[HEAD]['x'], 'y': self.coords[HEAD]['y'] + 1}
        elif self.direction == LEFT:
            new_head = {'x': self.coords[HEAD]['x'] - 1, 'y': self.coords[HEAD]['y']}
        elif self.direction == RIGHT:
            new_head = {'x': self.coords[HEAD]['x'] + 1, 'y': self.coords[HEAD]['y']}
        self.coords.insert(0, new_head)

    def check_collisions(self):
        if self.coords[HEAD]['x'] == -1 or self.coords[HEAD]['x'] == self.cell_width:
            return True

        if self.coords[HEAD]['y'] == -1 or self.coords[HEAD]['y'] == self.cell_height:
            return True

        for snake_body in self.coords[1:]:
            if snake_body['x'] == self.coords[HEAD]['x'] and snake_body['y'] == self.coords[HEAD]['y']:
                return True

        return False

    def check_apple_collision(self, apple):
        return self.coords[HEAD]['x'] == apple.coords['x'] and self.coords[HEAD]['y'] == apple.coords['y']

    def draw(self, surface, cell_size):
        for coord in self.coords:
            x = coord['x'] * cell_size
            y = coord['y'] * cell_size

            snake_segment_rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(surface, DARK_GREEN, snake_segment_rect)

            snake_inner_segment_rect = pygame.Rect(x + 4, y + 4, cell_size - 8, cell_size - 8)
            pygame.draw.rect(surface, GREEN, snake_inner_segment_rect)