from Maze import *
import pygame
import random
import time


x, y = 20, 20  # start point of maze on window/canvas
build_grid(0, 0, 20)

Make_Maze(x, y)
Solve_Maze(200, 200)

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
