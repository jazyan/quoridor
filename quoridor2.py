import pygame
from pygame.locals import *
from sys import exit
import numpy
import random

pygame.init()
screen = pygame.display.set_mode([470,470])
pygame.display.set_caption("Quoridor")

#create background and grid
back = pygame.Surface((470,470))
background = back.convert()
background.fill((255,255,255))

circ_sur = pygame.Surface((30,30))
circ = pygame.draw.circle(circ_sur,(0,255,0),(15,15),15)
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

bar_x = pygame.Surface((1,50))
bar1 = bar_x.convert()
bar1.fill((0,0,255))

bar_y = pygame.Surface((50,1))
bar2 = bar_y.convert()
bar2.fill((0,0,255))

bar_vert_x = [60,110,160,210,260,310,360,410]
bar_vert_y = [10]*8
bar_hor = [zip(bar_vert_y, bar_vert_x)]
bar_vert = [zip(bar_vert_x, bar_vert_y)]
j = 60
for i in range(0,8):
   bar_vert_y = [j]*8
   zipper_vert = zip(bar_vert_x,bar_vert_y)
   zipper_hor = zip(bar_vert_y,bar_vert_x)
   bar_vert.append(zipper_vert)
   bar_hor.append(zipper_hor)
   j += 50

#loop through game
while 1:
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
   screen.blit(background,(0,0))
   pygame.draw.rect(screen,(0,0,0),Rect((10,10),(450,450)),5)
   for j in range(0,9):
      for k in range(0,8): 
         screen.blit(bar1,bar_vert[j][k])
         screen.blit(bar2,bar_hor[j][k])
   pygame.display.update()

# TODO
# create bars and store in arrays (bar1_x, bar2_x, bar1_y for locations)
# click a bar, then check bars around if legal
# make pieces
# check if legal move is actually illegal b/c blocks off all paths
