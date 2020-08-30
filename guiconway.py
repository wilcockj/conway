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

pygame.init()
playing = False
window_size = [1920,1080]
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
lightblue = (51,255,255)
lightbluegreen = (51,255,153)
red = (255,0,0)
blue = (0,0,255)
grid = []
myblank = []
start = (0,0)
end = (9,9)
#want to have height always go down to 1000 and if square leave space on sides
gridheight = 100
gridwidth = 100
height = int((800/gridheight))
if height == 0:
    height = 1
width = height
margin = 0
smallfont = pygame.font.SysFont('Corbel',35)
#must make faster to make buttons more responsive also currently buttons are triggered only by position not mouse click
text = smallfont.render('ToggleSim',True,(255,255,255))
quit = smallfont.render('Quit',True,(255,255,255))
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
        if 0 <= x < gridheight and 0 <= y < gridwidth:
            result += grid[x][y]
    return result
def nextboard(myblank,array,myheight,mywidth):
    heightrange = range(myheight)
    widthrange = range(mywidth)
    num = 0 
    b = []
    for x in range(myheight):
        b.append([])
        for y in range(mywidth):
            b[x].append(0)
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
def addgun(grid,x,y):
    print(x,y)
    grid[5+x][1+y] = 1
    grid[5+x][2+y] = 1
    grid[6+x][1+y] = 1
    grid[6+x][2+y] = 1
    grid[1+x][25+y] = 1
    grid[2+x][23+y] = 1
    grid[2+x][25+y] = 1
    grid[3+x][13+y] = 1
    grid[3+x][14+y] = 1
    grid[3+x][21+y] = 1
    grid[3+x][22+y] = 1
    grid[4+x][12+y] = 1
    grid[4+x][16+y] = 1
    grid[4+x][21+y] = 1
    grid[4+x][22+y] = 1
    grid[5+x][11+y] = 1
    grid[5+x][17+y] = 1
    grid[5+x][21+y] = 1
    grid[5+x][22+y] = 1
    grid[6+x][11+y] = 1
    grid[6+x][15+y] = 1
    grid[6+x][17+y] = 1
    grid[6+x][18+y] = 1
    grid[6+x][23+y] = 1
    grid[6+x][25+y] = 1
    grid[7+x][11+y] = 1
    grid[7+x][17+y] = 1
    grid[7+x][25+y] = 1
    grid[8+x][12+y] = 1
    grid[8+x][16+y] = 1
    grid[9+x][13+y] = 1
    grid[9+x][14+y] = 1
    grid[3+x][35+y] = 1
    grid[3+x][36+y] = 1
    grid[4+x][35+y] = 1
    grid[4+x][36+y] = 1
    return grid
print("Initializing Game Board")
for row in range(gridheight):   
    grid.append([])
    myblank.append([])
    for column in range(gridwidth):
        grid[row].append(0)
        myblank[row].append(0)

screen = pygame.display.set_mode(window_size,pygame.FULLSCREEN)
done = False
clock = pygame.time.Clock()
print("Starting Game")
drawcount = 0
while not done:
    if playing:
        print("doing things")
        #time.sleep(1)
        start_time = time.time()
        grid = nextboard(myblank,grid,gridheight,gridwidth)
        print("--- %s seconds to do conway sim ---" % (time.time() - start_time))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            print(drawcount)
            done = True
        elif pygame.mouse.get_pressed()[0]:
            if 40 <= pos[0] <= 200 and 1005 <= pos[1] <= 1055:
                print("button pressed")
                playing = not playing
            if 300 <= pos[0] <= 380 and 1005 <= pos[1] <= 1055:
                pygame.quit()
            pos = pygame.mouse.get_pos()
            column = pos[0] // (width+margin)
            row = pos[1] // (height+margin)
            if row < gridheight and column < gridwidth:
                if not (row == start[0] and column == start[1]):
                    grid[row][column] = 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = not playing
            if event.key == pygame.K_r:
                for row in range(gridheight):
                    for column in range(gridwidth):
                        if random() > .5:
                            grid[row][column] = 1
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == pygame.K_p:
                for x in range(gridheight):
                    for y in range(gridwidth):
                        grid[x][y] = 0
            if event.key == pygame.K_g:
                for x in range(int(gridheight/30)):
                    grid = addgun(grid,30*x,0)
                for y in range(int(gridwidth/50)):
                    grid = addgun(grid,0,50*y)
        '''
        elif pygame.mouse.get_pressed()[2]:
            column = pos[0] // (width+margin)
            row = pos[1] // (height+margin)
            if row < gridheight and column < gridwidth:
                if not (row == start[0] and column == start[1]):
                    grid[row][column] = 0
        '''

        '''
            if event.key == pygame.K_SPACE:
                playing = not playing
                if not playing:
                    print("stopped")
                if playing:
                    print("doing things")
                grid = nextboard(grid,gridheight,gridwidth)
        '''
    screen.fill(black)

    if playing:
        pygame.draw.rect(screen,green,[40,1005,160,50])
    elif not playing:
        pygame.draw.rect(screen,red,[40,1005,160,50])
    pygame.draw.rect(screen,blue,[300,1005,80,50])
    start_time = time.time() 
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
    print("--- %s seconds to draw rects ---" % (time.time() - start_time))
    screen.blit(text,(50,1010))
    screen.blit(quit,(310,1010))
    clock.tick(60)
    pygame.display.update()
pygame.quit()
