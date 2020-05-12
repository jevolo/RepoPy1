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

shape = (1024,1024)
scale = 500.0
octaves = 6
persistence = 0.25
lacunarity = 2.0

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = pn.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=0)

im = Image.fromarray(np.uint8(cm.gist_earth(world)*255))


blue = [65,105,225]
green = [34,139,34]
beach = [238, 214, 175]

def add_color(world):
    color_world = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.05:
                color_world[i][j] = blue
            elif world[i][j] < 0:
                color_world[i][j] = beach
            elif world[i][j] < 1.0:
                color_world[i][j] = green

    return color_world

color_world = add_color(world)
color_world = Image.fromarray(np.uint8(cm.gist_earth(world)*255))

im.save(r"C:\Users\Jordy\Desktop\Image.png")