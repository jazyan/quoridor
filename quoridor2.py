import pygame
from pygame.locals import *
from sys import exit
import random

class Bar(pygame.sprite.Sprite):
   def __init__(self, color, width, height):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface((width,height))
      self.image = self.image.convert()
      self.image.fill(color)
      self.rect = self.image.get_rect()
   def update(self,mouse):
      if self.rect.collidepoint(mouse):
         self.image.fill((255,0,0))

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

bar_coord_x = [60,110,160,210,260,310,360,410]
bar_coord = bar_coord_x
bar_coord_y = [10,60,110,160,210,260,310,360,410]

for i in range(0,8):
   for j in range(0,9):
      bar_vert = Bar((0,0,0),3,50)
      bar_vert.rect.x = bar_coord_x[i]
      bar_vert.rect.y = bar_coord_y[j]
      bar_list.add(bar_vert)
      all_sprites_list.add(bar_vert)

for i in range(0,8):
   for j in range(0,9):
      bar_hor = Bar((0,0,0),50,3)
      bar_hor.rect.x = bar_coord_y[j]
      bar_hor.rect.y = bar_coord_x[i]
      bar_list.add(bar_hor)
      all_sprites_list.add(bar_hor)

#loop through game
while 1:
   mouse = pygame.mouse.get_pos()
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         all_sprites_list.update(mouse)
      if event.type == pygame.MOUSEBUTTONUP:
         all_sprites_list.update(mouse)
   screen.blit(background,(0,0))
   pygame.draw.rect(screen,(0,0,0),Rect((10,10),(450,450)),5)
   all_sprites_list.draw(screen)
   pygame.display.update()

# TODO
# click a bar, then check bars around if legal (SPRITES)
# make pieces
# check if legal move is actually illegal b/c blocks off all paths
