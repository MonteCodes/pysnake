import random
import pygame


RED         = (255,   0,   0)


class Apple:

    def __init__(self, cell_width, cell_height):
        self.cell_width = cell_width
        self.cell_height = cell_height

        self.x = random.randint(0, self.cell_width - 1)
        self.y = random.randint(0, self.cell_height - 1)

        self.coords = {'x': self.x, 'y': self.y}

    def move(self):
        self.x = random.randint(0, self.cell_width - 1)
        self.y = random.randint(0, self.cell_height - 1)

        self.coords = {'x': self.x, 'y': self.y}

    def draw(self, surface, cell_size):
        x = self.coords['x'] * cell_size
        y = self.coords['y'] * cell_size
        apple_rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(surface, RED, apple_rect)
