import pygame
from pygame.locals import *
from pygame.draw import *
global current_map,current_collision,px,py

def changement_de_sens(png,sprit,sens,x,y,fenetre,sprit_fond):
	personnage = pygame.image.load(png)
	personnage = pygame.transform.rotate(personnage,sens)
	deplacement_position (x,y,sprit_fond,personnage,fenetre)

def next_sens_case(x,y,direction,sprit_fond):
	if direction == 90:
		next_case = (x+1,y)
	if direction == 270:
		next_case = (x-1,y)
	if direction == 180:
		next_case = (x,y-1)
	if direction == 0:
		next_case = (x,y+1)
	return next_case
	
def deplacement_position (x,y,sprit_fond,sprit,fenetre):
	dim_sprit_fond = sprit_fond.get_rect().size
	case_x  = dim_sprit_fond[0]/15
	case_y  = dim_sprit_fond[1]/10
	fenetre.blit(sprit,(x*case_x,y*case_y))
	
def collision_off(px,py):
	collision = False
	collision = px == -1 or px == 15 or py == -1 or py == 10
	return collision
	
def collision_01 (px,py):
	collision = False
	collision = px == 0 or px == 14 or py == 0 or py == 9 or (px,py) == (10,1)or (px,py) == (11,3)or (px,py) == (11,2)or (px,py) == (11,1)or (px,py) == (12,1)or (px,py) == (12,2)or (px,py) == (12,3)or (px,py) == (13,1)or (px,py) == (13,6)or (px,py) == (12,8)or (px,py) == (13,8)or (px,py) == (13,7)or (px,py) == (5,6)or (px,py) == (5,4)or (px,py) == (5,5)or (px,py) == (6,5)or (px,py) == (2,2)or (px,py) == (2,1)or (px,py) == (4,5)or (px,py) == (1,1)or (px,py) == (6,6)or (px,py) == (6,4)
	return collision
	
def collision_02 (px,py):
	collision = False
	collision = px == 0 or px == 1 or px == 2 or py == 8 or py == 9 or px == 14 or (px,py) == (3,0) or (px,py) == (3,1) or (px,py) == (3,2) or (px,py) == (3,7) or (px,py) == (3,6) or (px,py) == (4,7) or (px,py) == (5,7) or (px,py) == (13,2) or (px,py) == (12,2) or (px,py) == (13,1) or (px,py) == (12,1) or (px,py) == (13,0)or (px,py) == (12,0)or (px,py) == (10,7)or py == -1
	return collision

def collision_03 (px,py):
	collision = False
	collision = px == 3 or px == 12 or py == -1 or py == 10 or (px,py) == (4,5)or (px,py) == (8,4)or (px,py) == (9,4)or (px,py) == (10,4)or (px,py) == (11,4)or (px,py) == (8,3)or (px,py) == (9,3)or (px,py) == (10,3)or (px,py) == (11,3)or (px,py) == (5,4)or (px,py) == (5,3)or (px,py) == (8,3)or (px,py) == (8,4)or (px,py) == (11,0)or (px,py) == (11,1)or (px,py) == (11,2)or (px,py) == (4,3)or (px,py) == (4,0)or (px,py) == (4,1)or (px,py) == (4,2)or (px,py) == (5,5)or (px,py) == (5,2)or (px,py) == (10,0)or (px,py) == (10,1)or (px,py) == (10,2)or (px,py) == (5,6)or (px,py) == (8,6)or (px,py) == (8,5)or (px,py) == (8,1)or (px,py) == (8,2)or (px,py) == (5,1)
	return collision
	
def collision_04 (px,py):
	collision = False
	collision = px == -1 or px == 15 or py == 0 or py == 10 or (px,py) == (4,9)or (px,py) == (3,8)or (px,py) == (2,7)or (px,py) == (0,6)or (px,py) == (1,7)or (px,py) == (7,5)or (px,py) == (8,5)or (px,py) == (8,4)or (px,py) == (9,3)or (px,py) == (10,3)or (px,py) == (11,3)or (px,py) == (12,2)or (px,py) == (13,1)or (px,py) == (14,1)or (px,py) == (10,9)or (px,py) == (11,8)or (px,py) == (12,7)or (px,py) == (13,6)or (px,py) == (14,5)or (px,py) == (6,4)or (px,py) == (5,3)or (px,py) == (4,2)or (px,py) == (3,2)or (px,py) == (2,1)or (px,py) == (1,0)or (px,py) == (0,0)
	return collision

def collision_05 (px,py):
	collision = False
	collision =  px == -1 or px == 15 or py == 0 or py == 1 or py == 9  or (px,py) == (1,5) or (px,py) == (2,5) or (px,py) == (3,5) or (px,py) == (4,5) or (px,py) == (5,5) or (px,py) == (6,5) or (px,py) == (5,6) or (px,py) == (4,6) or (px,py) == (1,6) or (px,py) == (2,6) or (px,py) == (6,8) or (px,py) == (7,8) or (px,py) == (8,8) or (px,py) == (9,8) or (px,py) == (10,8) or (px,py) == (11,8) or (px,py) == (12,8) or (px,py) == (13,8) or (px,py) == (14,8) or (px,py) == (0,2) or (px,py) == (1,2) or (px,py) == (0,4) or (px,py) == (1,4) or (px,py) == (2,4) or (px,py) == (3,4) or (px,py) == (4,4) or (px,py) == (5,4) or (px,py) == (6,4) or (px,py) == (1,6) or (px,py) == (2,6) or (px,py) == (3,6) or (px,py) == (4,6) or (px,py) == (5,6) or (px,py) == (6,6) or (px,py) == (0,6) or (px,py) == (14,6) or (px,py) == (12,6) or (px,py) == (13,6) or (px,py) == (8,7) or (px,py) == (9,7) or (px,py) == (10,7) or (px,py) == (11,7) or (px,py) == (12,7) or (px,py) == (13,7) or (px,py) == (14,7)
	return collision
	
def collision_06 (px,py):
	collision = False
	collision = px == -1 or px == 15 or py == 0 or py == 1 or py == 9 or (px,py) == (14,2) or (px,py) == (14,4) or (px,py) == (0,0) or (px,py) == (14,5) or (px,py) == (14,6) or (px,py) == (14,7) or (px,py) == (14,8) or (px,py) == (11,2) or (px,py) == (10,3) or (px,py) == (10,4) or (px,py) == (10,5) or (px,py) == (10,6) or (px,py) == (9,6) or (px,py) == (8,6) or (px,py) == (7,6) or (px,py) == (7,5) or (px,py) == (7,4) or (px,py) == (7,3) or (px,py) == (6,2) or (px,py) == (5,1) or (px,py) == (4,1) or (px,py) == (3,1) or (px,py) == (2,2) or (px,py) == (2,3) or (px,py) == (1,3) or (px,py) == (4,4) or (px,py) == (4,5) or (px,py) == (4,6) or (px,py) == (4,7) or (px,py) == (5,8) or (px,py) == (6,8) or (px,py) == (3,7) or (px,py) == (2,7) or (px,py) == (1,7) or (px,py) == (13,5) or (px,py) == (13,6) or (px,py) == (13,7) or (px,py) == (13,8) or (px,py) == (0,8) or (px,py) == (0,2)
	return collision
	

def collision_07 (px,py):
	collision = False
	collision = py == 0 or px == 15 or px == 0 or py == 8 or py == 9 or py == 7 or (px,py) == (3,1) or (px,py) == (4,1) or (px,py) == (5,2) or (px,py) == (6,2) or (px,py) == (7,2) or (px,py) == (8,2) or (px,py) == (9,2) or (px,py) == (10,2) or (px,py) == (11,1) or (px,py) == (12,1) or (px,py) == (13,1) or (px,py) == (14,1) or (px,py) == (0,0) or (px,py) == (0,0) or (px,py) == (0,0) or (px,py) == (0,0) or (px,py) == (0,0)
	return collision

def collision_08 (px,py):
	collision = False
	collision = px == 0 or px == 14 or py == 0 or py == 9
	return collision
	
def collision_09 (px,py):
	collision = False
	collision = px == -1 or px == 15 or py == -1 or (px,py) == (0,2)or (px,py) == (1,2)or (px,py) == (2,1)or (px,py) == (3,1)or (px,py) == (4,1)or (px,py) == (5,1)or (px,py) == (5,0)or (px,py) == (9,0)or (px,py) == (9,1)or (px,py) == (10,1)or (px,py) == (11,1)or (px,py) == (12,2)or (px,py) == (13,2)or (px,py) == (14,2)or (px,py) == (14,7)or (px,py) == (13,8)or (px,py) == (12,8)or (px,py) == (11,8)or (px,py) == (10,8)or (px,py) == (9,8)or (px,py) == (8,7)or (px,py) == (7,6)or (px,py) == (6,6)or (px,py) == (0,5)or (px,py) == (1,5)or (px,py) == (2,5)or (px,py) == (3,5)or (px,py) == (4,5)or (px,py) == (5,5)
	return collision 

def collision_10 (px,py):
	collision = False
	collision = px == -1 or px == 15 or py == 2 or py == 7
	return collision 
	
def collision_11(px,py):
	collision = False
	collision = px == -1 or px == 15 or py == 8 or py == 1  or (px,py) == (3,2) or (px,py) == (8,7) or (px,py) == (9,7) or (px,py) == (10,7) or (px,py) == (10,2) or (px,py) == (14,2) or (px,py) == (13,2) or (px,py) == (13,7) or (px,py) == (14,7)
	return collision 

def collision_12(px,py):
	collision = False
	collision = px == -1 or py == 7 or py == 2 or (px,py) == (5,3) or (px,py) == (6,3) or (px,py) == (7,3) or (px,py) == (6,6) or (px,py) == (7,6) or px == 12
	return collision 



