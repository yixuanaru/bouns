import pygame
import random

pygame.init()

width,height=400,400
grid_size=8
cell_size=width//grid_size

white=(255,255,255)

screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("candycrash")

grid=[[random.randint(1,3) for _ in range(grid_size)] for _ in range(grid_size)]

select= None

def click(row,col):
    global select
    if select is None:
        select=(row,col)
    else:
        row1,col1=select
        grid[row][col],grid[row1][col1]=grid[row1][col1],grid[row][col]
        select=None

def match():
    matches=set()
    for row in range(grid_size):
        for col in range(grid_size-2):
            if grid[row][col]==grid[row][col+1]==grid[row][col+2]:
                matches.add((row,col))
                matches.add((row,col+1))
                matches.add((row,col+2))
    for col in range(grid_size):
        for row in range(grid_size-2):
            if grid[row][col]==grid[row+1][col]==grid[row+2][col]:
                matches.add((row,col))
                matches.add((row+1,col))
                matches.add((row+2,col))
    return matches


def fill_empty():
    for col in range(grid_size):
        empty_count=sum(1 for row in range(grid_size) if grid[row][col]==0)
        for _ in range(empty_count):
            grid[grid_size-1][_]=random.randint(1,3)

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            col=event.pos[0]//cell_size
            row=event.pos[1]//cell_size
            if 0<=row<grid_size and 0<=col<grid_size:
                click(row,col)
    
    screen.fill(white)

    for row in range(grid_size):
        for col in range(grid_size):
            candy_type=grid[row][col]
            candy_color=(255,0,0) if candy_type==1 else(0,255,0) if candy_type==2 else (0,0,255)
            pygame.draw.rect(screen,candy_color,(col*cell_size ,row*cell_size,cell_size,cell_size))
        
    matches=match()
    if matches:
        for row,col in matches:
            grid[row][col]=0
    pygame.display.flip()

pygame.quit()