import pygame
from fonction import*
from pygame.locals import *
from pygame.draw import *



pygame.init()
music = pygame.mixer.music.load("animal(3).wav")
pygame.display.set_caption("jeux")
map_01 = pygame.image.load("01.png")
map_01bis = pygame.image.load("01bis.png")
map_02 = pygame.image.load("02.png")
map_03 = pygame.image.load("03.png")
map_04 = pygame.image.load("04.png")
map_05 = pygame.image.load("05.png")
map_06 = pygame.image.load("06.png")
map_07 = pygame.image.load("07.png")
map_08 = pygame.image.load("08.png")
map_09 = pygame.image.load("09.png")
map_10 = pygame.image.load("10.png")
map_11 = pygame.image.load("11.png")
map_12 = pygame.image.load("12.png")
femme = pygame.image.load("femme.PNG")
case_avant = [10,3]
pygame.mixer.music.play(-1)
a = True
px = 10
py = 3
sens = 270
fenetre = pygame.display.set_mode((960, 640))




good = True
while good :
	
	for event in pygame.event.get():
		if a ==True:
			current_map = map_01
			current_collision = collision_01
			fenetre.blit(current_map,(0,0))
			changement_de_sens("femme.PNG",femme,sens,px,py,fenetre,current_map)
			a= False
		if event.type == QUIT:
			good = False
		elif event.type == KEYDOWN:
			if event.key == K_RIGHT:
				px = px+1
				sens = 90
			if event.key == K_LEFT:
				px = px-1
				sens = 270
			if event.key == K_UP:
				py = py-1
				sens = 180   
			if event.key == K_DOWN:
				py = py+1
				sens = 0
			if current_collision(px,py) == True:
				px = case_avant[0]
				py = case_avant[1]
			fenetre.blit(current_map,(0,0))
			print(px,py)
			
			if current_map == map_01:
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map) == (0,7):
					current_map = map_02
					fenetre.blit(current_map,(0,0))
					px = 13
					py = 5
					current_collision = collision_02
					
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map) == (13,6):
					current_map = map_01bis
					fenetre.blit(current_map,(0,0))
					px = 5
					py = 5
					current_collision = collision_off
					
			if current_map == map_01bis:
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map) == (4,5):
					current_map = map_01
					fenetre.blit(current_map,(0,0))
					px = 12
					py = 6
					current_collision = collision_01
							
			if current_map == map_02:
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[1] == -1:
					current_map = map_03
					fenetre.blit(current_map,(0,0))
					py = 9
					current_collision = collision_03
					
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map) == (14,5):
					
					current_map = map_01
					fenetre.blit(current_map,(0,0))
					px = 1
					py = 7
					current_collision = collision_01
					
			if current_map == map_03:	
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[1] == -1:
					
					current_map = map_04
					fenetre.blit(current_map,(0,0))
					py = 9
					current_collision = collision_04
					
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[1] == 10:
					
					current_map = map_02
					fenetre.blit(current_map,(0,0))				
					py = 0
					current_collision = collision_02
					
			if current_map == map_04:
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[1] == 10:
					
					current_map = map_03
					fenetre.blit(current_map,(0,0))
					py = 0
					current_collision = collision_03
					
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == -1:
					
					current_map = map_05
					fenetre.blit(current_map,(0,0))
					px = 14
					current_collision = collision_05
					
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == 15:
					
					current_map = map_09
					fenetre.blit(current_map,(0,0))
					px = 0
					current_collision = collision_09
					
			if current_map == map_05:
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == -1:
					
					current_map = map_06
					fenetre.blit(current_map,(0,0))
					px = 14
					current_collision = collision_06
					
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == 15:
					
					current_map = map_04
					fenetre.blit(current_map,(0,0))
					px = 0
					current_collision = collision_04
					
			if current_map == map_06:
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == -1:
					current_map = map_07
					fenetre.blit(current_map,(0,0))
					px = 14
					current_collision = collision_07
					
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == 15:
					
					current_map = map_05
					fenetre.blit(current_map,(0,0))
					px = 0
					current_collision = collision_05
					
			if current_map == map_07:
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == 0:
					
					current_map = map_08
					fenetre.blit(current_map,(0,0))
					px = 13
					current_collision = collision_08
					
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == 15:
					
					current_map = map_06
					fenetre.blit(current_map,(0,0))
					px = 0
					current_collision = collision_06
					
			if current_map == map_08:
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == 14:
					
					current_map = map_07
					fenetre.blit(current_map,(0,0))
					px = 1
					current_collision = collision_07
					
			if current_map == map_09:
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == -1:
					
					current_map = map_04
					fenetre.blit(current_map,(0,0))
					px = 14
					current_collision = collision_04
					
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == 15:
					
					current_map = map_10
					fenetre.blit(current_map,(0,0))
					px = 0
					current_collision = collision_10
					
			if current_map == map_10:
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == -1:
					
					current_map = map_09
					fenetre.blit(current_map,(0,0))
					px = 14
					current_collision = collision_09
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == 15:
					
					current_map = map_11
					fenetre.blit(current_map,(0,0))
					px = 0
					current_collision = collision_11
					
			if current_map == map_11:
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == 15:
					
					current_map = map_12
					fenetre.blit(current_map,(0,0))
					px = 0
					current_collision = collision_12
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == -1:
					
					current_map = map_10
					fenetre.blit(current_map,(0,0))
					px = 14
					current_collision = collision_10
					
			if current_map == map_12:
				
				if event.key == K_KP0 and next_sens_case(px,py,sens,current_map)[0] == -1:
					
					current_map = map_11
					fenetre.blit(current_map,(0,0))
					px = 14
					current_collision = collision_11
					
				
			changement_de_sens("femme.PNG",femme,sens,px,py,fenetre,current_map)
			case_avant = [px,py]
			
	pygame.display.update()

pygame.quit()




