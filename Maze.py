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
# x = 0  # the top left corner of the screen is (0,0)
# y = 0
w = 20  # width of cell
grid = []
visited = []
stack = []
solution = {}  # holds the pairs of new and current cells


# build grid
def build_grid(x, y, w):
    for row in range(0, 10):
        x = 20  # grid is 20 by 20 and we are building it from 20px inside the screen,every row will be 20px below
        y = y+20
        for col in range(0, 10):
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


# these cut_ functions are used to remove the lines from the grid to make it look like a maze
# since removing a line is very difficult in ptgame so we are actually overwriting on 2 cells with different color
# so that it may looks like that a line has been removed


def cut_up(x, y):
    pygame.draw.rect(screen, BLUE, (x+1, y-w+1, w-1, (w+w)-1))
    pygame.display.update()


def cut_down(x, y):
    pygame.draw.rect(screen, BLUE, (x+1, y+1, w-1, (w+w)-1))
    pygame.display.update()


def cut_left(x, y):
    pygame.draw.rect(screen, BLUE, (x-w+1, y+1, (w+w)-1, w-1))
    pygame.display.update()


def cut_right(x, y):
    pygame.draw.rect(screen, BLUE, (x+1, y+1, (w+w)-1, w-1))
    pygame.display.update()


# draw staring point

def single_cell(x, y):
    pygame.draw.rect(screen, GREEN, (x+1, y+1, 18, 18))
    pygame.display.update()


def backtracking_cell(x, y):
    # used to re-colour the path after single_cell has visited
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, 18, 18), 0)
    pygame.display.update()


def solution_cell(x, y):
    # used to show the solution
    pygame.draw.rect(screen, YELLOW, (x+8, y+8, 5, 5), 0)
    pygame.display.update()


def Make_Maze(x, y):
    single_cell(x, y)
    stack.append((x, y))
    visited.append((x, y))
    while len(stack) > 0:  # loop till stack is empty
        time.sleep(0.07)  # add delay
        pos = []
        # check if any of the neighbouring cell is not visited
        if (x+w, y) not in visited and (x+w, y) in grid:  # if the cell to the right is not visited
            pos.append('right')  # then add a position in pos list

        if (x-w, y) not in visited and (x-w, y) in grid:
            pos.append('left')

        if (x, y+w) not in visited and (x, y+w) in grid:
            pos.append('down')

        if (x, y-w) not in visited and (x, y-w) in grid:
            pos.append('up')

        # when unvisited neighbours are selected, move to any of these neighbours at random
        if len(pos) > 0:
            chosen_cell = random.choice(pos)

            if chosen_cell == 'right':
                cut_right(x, y)
                # add curr cell to solution dict
                solution[(x+w, y)] = x, y
                # make this cell curr cell
                x = x+w
                # add curr cell to visited and stack
                visited.append((x, y))
                stack.append((x, y))

            if chosen_cell == 'left':
                cut_left(x, y)
                # add curr cell to solution dict
                solution[(x-w, y)] = x, y
                # make this cell curr cell
                x = x-w
                # add curr cell to visited and stack
                visited.append((x, y))
                stack.append((x, y))

            if chosen_cell == 'down':
                cut_down(x, y)
                # add curr cell to solution dict
                solution[(x, y+w)] = x, y
                # make this cell curr cell
                y = y+w
                # add curr cell to visited and stack
                visited.append((x, y))
                stack.append((x, y))

            if chosen_cell == 'up':
                cut_up(x, y)
                # add curr cell to solution dict
                solution[(x, y-w)] = x, y
                # make this cell curr cell
                y = y-w
                # add curr cell to visited and stack
                visited.append((x, y))
                stack.append((x, y))

        # if there are no unvisited neighbours
        else:
            # pop from stack
            x, y = stack.pop()
            # Display poping
            single_cell(x, y)
            time.sleep(0.05)
            backtracking_cell(x, y)


# this function will get to the start of the maze from the position provided from main
def Solve_Maze(x, y):
    # solution list contains all the coordinates to route back to start
    solution_cell(x, y)
    # loop until cell position == start position
    while (x, y) != (20, 20):
        # "key value" now becomes the new key
        x, y = solution[x, y]
        # animate route back
        solution_cell(x, y)
        time.sleep(.1)
