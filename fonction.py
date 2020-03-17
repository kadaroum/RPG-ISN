import pygame
from pygame.locals import *

def changement_de_sens(sprit,sens,px,py,espace):
	personnage = pygame.image.load(sprit)
	personnage = pygame.transform.rotate(personnage,sens)
	espace.blit(personnage,(px,py))

def next_sens_case(px,py,direction):
	if direction == "right":
		next_case = (px+83,py)
	if direction == "left":
		next_case = (px-83,py)
	if direction == "up":
		next_case = (px,py-83)
	if direction == "down":
		next_case = (px,py+83)
	return next_case
