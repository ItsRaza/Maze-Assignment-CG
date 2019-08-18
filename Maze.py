import pygame
import time
import random

# setitng pygame window
WIDTH = 600
HEIGHT = 500
FPS = 25  # framerate

# Defining names to RGB colours

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MAZE')
clock = pygame.time.Clock()


# Maze Variables
x = 0  # the top left corner of the screen is (0,0)
y = 0
w = 20  # width of cell
grid = []
visited = []
stack = []
solution = {}  # holds the pairs of new and current cells


# build grid
def build_grid(x, y, w):
    for row in range(0, 20):
        x = 20  # grid is 20 by 20 and we are building it from 20px inside the screen,every row will be 20px below
        y = y+20
        for col in range(0, 20):
            # top of cell,drawing line form curr x,y till the width of cell
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])
            # right of cell
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])
            # bottom of cell
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])
            # left of cell
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])
            # add cell to grid list
            grid.append((x, y))
            # move cell to new position
            x = x + 20
