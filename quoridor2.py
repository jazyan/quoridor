import pygame
from pygame.locals import *
from sys import exit
import random

class Bar(pygame.sprite.Sprite):
   def __init__(self, color, width, height):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface((width,height)).convert()
      self.image.fill(color)
      self.rect = self.image.get_rect()
   def update(self,mouse):
      if check == 0:
         if self.rect.collidepoint(mouse):
            self.image.fill((255,0,0))
            red_bar_list.add(self)
      elif check == 1:
         if self.rect.collidepoint(mouse):
            for bar in red_bar_list:
              if bar.rect.x<=self.rect.x+50 and bar.rect.x>=self.rect.x-50:
                 if bar.rect.y == self.rect.y:
                    self.image.fill((255,0,0))
         #if event.key == K_LEFT:
            #mouse[0] = x-50
         
class Player(pygame.sprite.Sprite):
   def __init__(self,image):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(image)
      self.rect = self.image.get_rect()
   def update(self,mouse):
      if self.rect.collidepoint(mouse):
         if event.key == K_RIGHT:
            self.rect.x += 50.
         elif event.key == K_UP:
            self.rect.y -= 50.
         elif event.key == K_DOWN:
            self.rect.y += 50.
         elif event.key == K_LEFT:
            self.rect.x -= 50.

pygame.init()
screen = pygame.display.set_mode([470,470])
pygame.display.set_caption("Quoridor")

#create background
back = pygame.Surface((470,470))
background = back.convert()
background.fill((255,255,255))

bar_list = pygame.sprite.Group()
red_bar_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

bar_coord_x = [60,110,160,210,260,310,360,410]
bar_coord = bar_coord_x
bar_coord_y = [10,60,110,160,210,260,310,360,410]

#create grid of bars
for i in range(0,8):
   for j in range(0,9):
      bar_vert = Bar((0,0,0),5,50)
      bar_vert.rect.x = bar_coord_x[i]
      bar_vert.rect.y = bar_coord_y[j]
      bar_list.add(bar_vert)
      all_sprites_list.add(bar_vert)

for i in range(0,8):
   for j in range(0,9):
      bar_hor = Bar((0,0,0),50,5)
      bar_hor.rect.x = bar_coord_y[j]
      bar_hor.rect.y = bar_coord_x[i]
      bar_list.add(bar_hor)
      all_sprites_list.add(bar_hor)

#create players
player1 = Player('piece1.png')
player1.rect.x = 223
player1.rect.y = 70
player_list.add(player1)
all_sprites_list.add(player1)

player2 = Player('piece2.png')
player2.rect.x = 222
player2.rect.y = 370
player_list.add(player2)
all_sprites_list.add(player2)
check = 0

#loop through game
while 1:
   mouse = pygame.mouse.get_pos()
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         if check == 0: check = 1
         else: check = 0
         bar_list.update(mouse)
      if event.type == pygame.KEYDOWN:
         player_list.update(mouse)
   screen.blit(background,(0,0))
   pygame.draw.rect(screen,(0,0,0),Rect((10,10),(450,450)),5)
   all_sprites_list.draw(screen)
   pygame.display.update()

# TODO
# click a bar, then check bars around if legal (SPRITES)
# check if legal move is actually illegal b/c blocks off all paths
