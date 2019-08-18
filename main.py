from Maze import *
import pygame
import random
import time


# 1st argument = x value, 2nd argument = y value, 3rd argument = width of cell
build_grid(40, 0, 20)


# pygame running loop

running = True
while running:
    # keep running at the at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
