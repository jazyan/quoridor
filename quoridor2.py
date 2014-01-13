import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode([480,480])
pygame.display.set_caption("Quoridor")

#create background and grid
back = pygame.Surface((480,480))
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

bars1 = []
bars2 = []
i = 0
j = 0
x = 60.
y = 60.

#add bars into bar list
while i < 9:
   (bar_x,bar_y) = (x,10)
   bars1.append((bar_x,bar_y))
   x+=45 
   i+=1
while j < 9:
   (bar_x,bar_y) = (10,y)
   bars2.append((bar_x,bar_y))
   y+=45
   j+=1

#loop through game
while 1:
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
   screen.blit(background,(0,0))
   pygame.draw.rect(screen,(0,0,0),Rect((10,10),(460,460)),5)
   k = 0
   while k < 9: 
      screen.blit(bar1,bars1[k])
      screen.blit(bar2,bars2[k])
      k+=1
   pygame.display.update()

# TODO
# create bars and store in arrays (bar1_x, bar2_x, bar1_y for locations)
# click a bar, then check bars around if legal
# make pieces
# check if legal move is actually illegal b/c blocks off all paths
