import pygame as pg
import copy as c
import names as n
import pycountry as pc
import random as r
import noise as pn
import numpy as np
import scipy
from PIL import Image
from matplotlib import cm

win = pg.display.set_mode((800, 600))

pg.display.set_caption("First Game")

offset = 20
size = 130

WorldWidth = 13
WorldHeigth = 8
String = ''

#WorldGrid
WG = []
ListColumn = []

for i in range(WorldWidth):
    for i2 in range(WorldHeigth):
        ListColumn.append(0)
    WG.append(c.deepcopy(ListColumn))

Terain = [['Sea', (0, 0, 255)],['Grassland', (0, 255, 0)]]
Resourse = ['Fish','Wheat']

class Grid:
    Name = ''
    GTerain = ''
    GResourse = ''
    population = 0
    Growth = 0

def GenerateWorld():
    ix = 0
    iy = 0
    v = Grid()
    ListColumn = []

    for i in range(WorldHeigth):
        ListColumn.append(0)

    #WG[ix] = ListColumn

    for x in range(WorldWidth):
        

        for y in range(WorldHeigth):
            v.Name = list(pc.countries)[r.randint(0,len(pc.countries) - 1)].name
            v.GResourse = Resourse[r.randint(0,1)]
            v.GTerain = Terain[r.randint(0,1)]
            v.population = 0
            v.Growth = 0.1
            
            ListColumn[y] = c.deepcopy(v)
            iy += 1
        
        iy = 0
        ix += 1        
        WG[ix - 1] = (c.deepcopy(ListColumn))
        for i in range(len(ListColumn)):
            ListColumn[i] = 0

    #PrintArray()
    print('1 =' + str(len(WG)))

def PrintArray():
    WG[0][2].GTerain[0] = 'Hello'

    for x2 in WG:
        for y2 in x2:
            print(y2.GTerain)
    
def drawGrid():
    x = 0
    y = 0
    color = (0, 0, 0)
    for row in WG:
        for column in row:
            if column.GTerain[0] == 'Sea':
                color = Terain[0][1]
            else:
                color = Terain[1][1]
            pg.draw.rect(win, color, (50 + 20 * x, 50 + 20 * y, size, size))
            y += 1
        x += 1
        y = 0
    
    #pg.draw.rect(win, (255, 255, 255), (2, 2, 5, 5))
    #print(x,y)

run = False
while run:
    pg.time.delay(1000)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            quit()
        if pygame.mouse.get_pressed()[0]:
            coords = pygame.mouse.get_pos()
            print(coords)

    GenerateWorld()    
    print('2 =' + str(len(WG)))
    drawGrid()
    pg.display.update()
