import pygame
from fonction import*
from pygame.locals import *

pygame.init()
pygame.display.set_caption("jeux")
maison = pygame.image.load("Capture.PNG")
femme = pygame.image.load("main.PNG")




a = True
px = 90
py = 95
fenetre = pygame.display.set_mode((1240, 820))
fenetre.blit(maison,(0,0))
good = True
while good :
    for event in pygame.event.get():
        if a ==True:
            fenetre.blit(femme,(px,py))
            a= False
        if event.type == QUIT:
            good = False
        elif event.type == KEYDOWN:
            fenetre.blit(maison,(0,0))
            if event.key == K_RIGHT:
                px = px+83
                changement_de_sens("main.PNG",90,px,py,fenetre)
                direction="right"               
            if event.key == K_LEFT:
                px = px-83
                changement_de_sens("main.PNG",270,px,py,fenetre)
                direction="left"   
            if event.key == K_UP:
                py = py-83
                changement_de_sens("main.PNG",180,px,py,fenetre)
                direction="up"   
            if event.key == K_DOWN:
                py = py+83
                changement_de_sens("main.PNG",0,px,py,fenetre)
                direction="down"
				
            fenetre.blit(femme,(next_sens_case(px,py,direction)))
   
    pygame.display.update()

pygame.quit()




