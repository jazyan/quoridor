import pygame
from pygame.locals import *
from sys import exit
import random

class Bar(pygame.sprite.Sprite):
   def __init__(self, width, height):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface((width,height)).convert()
      self.image.fill((0,0,0))
      self.rect = self.image.get_rect()
   def update(self,mouse,width,height):
      if check == 0:
         if self.rect.collidepoint(mouse):
            self.image.fill((255,0,0))
            if width > height:
               hor_redbar_list.add(self)
            elif height > width:
               vert_redbar_list.add(self)
      elif check == 1:
         if self.rect.collidepoint(mouse) and width > height:
            for bar in hor_redbar_list:
               if bar.rect.x<=self.rect.x+50 and bar.rect.x>=self.rect.x-50:
                  if bar.rect.y == self.rect.y:
                     self.image.fill((255,0,0))
         elif self.rect.collidepoint(mouse) and width < height:
            for bar in vert_redbar_list:
               if bar.rect.y<=self.rect.y+50 and bar.rect.y>=self.rect.y-50:
                  if bar.rect.x == self.rect.x:
                     self.image.fill((255,0,0))

class Player(pygame.sprite.Sprite):
   def __init__(self,image):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(image)
      self.rect = self.image.get_rect()
   def update(self,mouse):
      test = 0
      if self.rect.collidepoint(mouse):
         if event.key == K_RIGHT:
            for bar in vert_redbar_list:
               if bar.rect.x<=self.rect.x+50 and bar.rect.x>=self.rect.x:
                  if bar.rect.y<=self.rect.y+10 and bar.rect.y>=self.rect.y-10:
                     self.rect.x = self.rect.x
                     test = 1
            if test == 0: self.rect.x += 50
            if self.rect.x >= 423: self.rect.x = 423
         elif event.key == K_UP:
            for bar in hor_redbar_list:
               if bar.rect.y>=self.rect.y-50 and bar.rect.y<=self.rect.y:
                  if bar.rect.x<=self.rect.x+10 and bar.rect.x>=self.rect.x-10:
                     self.rect.y = self.rect.y
                     test = 1
            if test == 0: self.rect.y -= 50.
            if self.rect.y <= 20: self.rect.y = 20
         elif event.key == K_DOWN:
            for bar in hor_redbar_list:
               if bar.rect.y<=self.rect.y+50 and bar.rect.y>=self.rect.y:
                  if bar.rect.x<=self.rect.x+10 and bar.rect.x>=self.rect.y-10:
                     self.rect.y = self.rect.y
                     test = 1
            if test == 0: self.rect.y += 50.
            if self.rect.y >= 420: self.rect.y = 420
         elif event.key == K_LEFT:
            for bar in vert_redbar_list:
               if bar.rect.x>=self.rect.x-50 and bar.rect.x<=self.rect.x:
                  if bar.rect.y<=self.rect.y+10 and bar.rect.y>=self.rect.y-10:
                     self.rect.x = self.rect.x
                     test = 1
            if test == 0: self.rect.x -= 50.
            if self.rect.x<=23: self.rect.x = 23

pygame.init()
screen = pygame.display.set_mode([470,470])
pygame.display.set_caption("Quoridor")

#create background
back = pygame.Surface((470,470))
background = back.convert()
background.fill((255,255,255))

bar_list = pygame.sprite.Group()
hor_bar_list = pygame.sprite.Group()
vert_bar_list = pygame.sprite.Group()
hor_redbar_list = pygame.sprite.Group()
vert_redbar_list = pygame.sprite.Group()
player1_group = pygame.sprite.Group()
player2_group = pygame.sprite.Group()
player_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

bar_coord_x = [60,110,160,210,260,310,360,410]
bar_coord = bar_coord_x
bar_coord_y = [10,60,110,160,210,260,310,360,410]

#create grid of bars
for i in range(0,8):
   for j in range(0,9):
      bar_vert = Bar(5,50)
      bar_vert.rect.x = bar_coord_x[i]
      bar_vert.rect.y = bar_coord_y[j]
      vert_bar_list.add(bar_vert)
      bar_list.add(bar_vert)
      all_sprites_list.add(bar_vert)

for i in range(0,8):
   for j in range(0,9):
      bar_hor = Bar(50,5)
      bar_hor.rect.x = bar_coord_y[j]
      bar_hor.rect.y = bar_coord_x[i]
      hor_bar_list.add(bar_hor)
      bar_list.add(bar_hor)
      all_sprites_list.add(bar_hor)

#create players
player1 = Player('piece1.png')
player1.rect.x = 223
player1.rect.y = 20
player1_group.add(player1)
player_list.add(player1)
all_sprites_list.add(player1)

player2 = Player('piece2.png')
player2.rect.x = 222
player2.rect.y = 420
player2_group.add(player2)
player_list.add(player2)
all_sprites_list.add(player2)
check = 0
p1_turn = 1
num_moves = 0

#loop through game
while 1:
   mouse = pygame.mouse.get_pos()
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         bar_list.update(mouse,50,5)
         bar_list.update(mouse,5,50) 
         if check == 0: 
            num_moves +=1
            check = 1
         else: check = 0
      if event.type == pygame.KEYDOWN:
         if p1_turn == 1:
            player1_group.update(mouse)
            p1_turn = 0
            num_moves += 1 
         elif p1_turn == 0:
            player2_group.update(mouse)
            p1_turn = 1
            num_moves += 1
   screen.blit(background,(0,0))
   pygame.draw.rect(screen,(0,0,0),Rect((10,10),(450,450)),5)
   all_sprites_list.draw(screen)
   pygame.display.update()

# TODO
# double click bar = black
# piece cannot move through red walls (up not working?)
# more contraints than double clicking
# limit blocks/player (list of each player's block)
# check if legal move is actually illegal b/c blocks off all paths
