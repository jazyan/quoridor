import pygame
from pygame.locals import *
from sys import exit
import numpy
import random

class Bar(pygame.sprite.Sprite):
   def __init__(self, color, width, height):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface((width,height))
      self.image = self.image.convert()
      self.image.fill(color)
      self.rect = self.image.get_rect()
   #def update(self):

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

bar_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

bar_coord = [60,110,160,210,260,310,360,410]

for i in range(0,8):
   for j in range(10,410):
      bar_vert = Bar((0,0,255),1,50)
      bar_vert.rect.x = bar_coord[i]
      bar_vert.rect.y = j
      bar_list.add(bar_vert)
      all_sprites_list.add(bar_vert)
      j += 50

for i in range(0,8):
   for j in range(10,410):
      bar_hor = Bar((0,0,255),50,1)
      bar_hor.rect.x = j
      bar_hor.rect.y = bar_coord[i]
      bar_list.add(bar_hor)
      all_sprites_list.add(bar_hor)
      j += 50

#loop through game
while 1:
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         pos = pygame.mouse.get_pos()
   screen.blit(background,(0,0))
   pygame.draw.rect(screen,(0,0,0),Rect((10,10),(450,450)),5)
   all_sprites_list.draw(screen)
   pygame.display.update()

# TODO
# click a bar, then check bars around if legal (SPRITES)
# make pieces
# check if legal move is actually illegal b/c blocks off all paths
