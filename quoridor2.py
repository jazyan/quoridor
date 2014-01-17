import pygame
from pygame.locals import *
from sys import exit
import random

class Bar(pygame.sprite.Sprite):
   def __init__(self, width, height,row,column):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.Surface((width,height)).convert()
      self.image.fill((0,0,0))
      self.rect = self.image.get_rect()
      self.column = column
      self.row = row
   def update(self,mouse):
      if num_bar_clicked == 0:
         if self.rect.collidepoint(mouse):
            self.image.fill((255,0,0))
            if self.rect.width > self.rect.height:
               hor_redbar_list.add(self)
            elif self.rect.height > self.rect.width:
               vert_redbar_list.add(self)
      elif num_bar_clicked == 1:
         if self.rect.collidepoint(mouse) and self.rect.width > self.rect.height:
            for bar in hor_redbar_list:
               if bar.row == self.row and abs(bar.column - self.column) == 1:
                  self.image.fill((255,0,0))
         elif self.rect.collidepoint(mouse) and self.rect.width < self.rect.height:
            for bar in vert_redbar_list:
               if bar.column == self.column and abs(bar.row - self.column) == 1:
                  self.image.fill((255,0,0))

class Player(pygame.sprite.Sprite):
   def __init__(self,image,row,column):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(image)
      self.rect = self.image.get_rect()
      self.column = column
      self.row = row
      self.update_position()
   def update_position(self):
      self.rect.y = self.row*50 + 20
      self.rect.x = self.column*50 + 23
 
   def update(self,mouse):
      move_blocked = 0
      if self.rect.collidepoint(mouse):
         if event.key == K_RIGHT:
            for bar in vert_redbar_list:
               if bar.row == self.row and bar.column == self.column:
                  move_blocked = 1
            if move_blocked == 0: self.column += 1
            if self.column >= 8: self.column = 8
         elif event.key == K_UP:
            for bar in hor_redbar_list:
               if bar.row == self.row - 1 and bar.column == self.column:
                  move_blocked = 1
            if move_blocked == 0: self.row -= 1
            if self.row < 0: self.row = 0
         elif event.key == K_DOWN:
            for bar in hor_redbar_list:
               if bar.row == self.row and bar.column == self.column:
                  move_blocked = 1
            if move_blocked == 0: self.row += 1
            if self.row >= 8: self.row = 8
         elif event.key == K_LEFT:
            for bar in vert_redbar_list:
               if bar.row == self.row and bar.column == self.column - 1:
                  move_blocked = 1
            if move_blocked == 0: self.column -= 1
            if self.column <= 0: self.rect.x = 0
      self.update_position()

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
for row in range(0,9):
   for column in range(0,8):
      bar_vert = Bar(5, 50, row, column)
      bar_vert.rect.x = bar_coord_x[column]
      bar_vert.rect.y = bar_coord_y[row]
      vert_bar_list.add(bar_vert)
      bar_list.add(bar_vert)
      all_sprites_list.add(bar_vert)

for row in range(0,8):
   for column in range(0,9):
      bar_hor = Bar(50,5, row, column)
      bar_hor.rect.x = bar_coord_y[column]
      bar_hor.rect.y = bar_coord_x[row]
      hor_bar_list.add(bar_hor)
      bar_list.add(bar_hor)
      all_sprites_list.add(bar_hor)

#create players
player1 = Player('piece1.png',0,4)
player1_group.add(player1)
player_list.add(player1)
all_sprites_list.add(player1)

player2 = Player('piece2.png',8,4)
player2_group.add(player2)
player_list.add(player2)
all_sprites_list.add(player2) 
num_bar_clicked= 0
p1_turn = 1
num_moves = 0

#loop through game
while 1:
   mouse = pygame.mouse.get_pos()
   for event in pygame.event.get():
      if event.type == QUIT:
         exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         bar_list.update(mouse)
         if num_bar_clicked == 0: 
            num_moves +=1
            num_bar_clicked = 1
         else: num_bar_clicked = 0
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
