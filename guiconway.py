import pygame
import sys
import time
from tkinter import *
from tkinter import messagebox
#import math
Tk().wm_withdraw() #to hide the main window
#before rendering go through the next board list and old list and find differences to make rendering faster
#messagebox.showinfo()
#todo fix prioritizing moving diagonal when should move in cardinal directions
#believe it is seeing moving diagonal as 1 space moved
#fix catching for no solution error
playing = False
window_size = [1920,1000]
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
lightblue = (51,255,255)
lightbluegreen = (51,255,153)
red = (255,0,0)
blue = (0,0,255)
width = 2
height = 2
margin = 1
grid = []
start = (0,0)
end = (9,9)
gridheight = 330
gridwidth = 750
from random import seed
from random import random
# seed random number generator
seed(1)
def renderboard(grid):
    screen.fill(black)
    for row in range(gridheight):
        for column in range(gridwidth):
                color = white
                if grid[row][column] == 1:
                        color = black
                pygame.draw.rect(screen, 
                                color,
                                [(margin+width)*column+margin,
                                (margin+height)*row+margin,
                                width,
                                height])
    clock.tick(60)
    pygame.display.flip()
def numneighbors(grid,x_coord,y_coord):
    result = 0
    for x,y in [(x_coord+i,y_coord+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            if grid[x][y] == 1:
                result += 1
    return result
def nextboard(array,myheight,mywidth):
    b = []
    for x in range(myheight):
        b.append([])
        for y in range(mywidth):
            b[x].append(0)
    num = 0 
    for x in range(myheight):
        for y in range(mywidth):
            num = numneighbors(array,x,y)
            if array[x][y] == 1:	
                if num == 2 or num == 3:
                    #print("It lives")
                    b[x][y] = 1
                else:
                    b[x][y] = 0
            else:	
                if num == 3:
#print("It lives")
                    b[x][y] = 1
        #print("dies")
    
    return b


print("Initializing Game Board")
for row in range(gridheight):   
    grid.append([])
    for column in range(gridwidth):
        grid[row].append(0)

pygame.init()
screen = pygame.display.set_mode(window_size)
done = False
clock = pygame.time.Clock()
print("Starting Game")
drawcount = 0
while not done:
    if playing:
        print("doing things")
        #time.sleep(1)
        grid = nextboard(grid,gridheight,gridwidth)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(drawcount)
            done = True
        elif pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width+margin)
            row = pos[1] // (height+margin)
            if row < gridheight and column < gridwidth:
                if not (row == start[0] and column == start[1]):
                    grid[row][column] = 1
        elif pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width+margin)
            row = pos[1] // (height+margin)
            if row < gridheight and column < gridwidth:
                if not (row == start[0] and column == start[1]):
                    grid[row][column] = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = not playing
                if not playing:
                    print("stopped")
                if playing:
                    print("doing things")
                #time.sleep(1)
                grid = nextboard(grid,gridheight,gridwidth)
                    #renderboard(grid)
            if event.key == pygame.K_g:
                for row in range(gridheight):
                    for column in range(gridwidth):
                        if random() > .5:
                            grid[row][column] = 1
    screen.fill(black)

    
    for row in range(gridheight):
        for column in range(gridwidth):
            color = white
            if grid[row][column] == 1:
                color = black
            #if row == start[0] and column == start[1]:
            #    color = blue
            #if row==end[0] and column == end[1]:
            #    color = red
            pygame.draw.rect(screen, 
                            color,
                            [(margin+width)*column+margin,
                            (margin+height)*row+margin,
                            width,
                            height])
            drawcount+=1
    clock.tick(60)
    pygame.display.flip()
