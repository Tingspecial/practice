import pygame
import os

pygame.init()
display_width = 800
display_height = 600

black =(0,0,0)
white = (255,255,255)
red = (255,0,0)
green =(0,0,255)
blue = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width, display_width))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('./img/veiw.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)
crashed = False

while not crashed:
    for event in pygame.event.get():
        #if event.type == pygame.QUIT:
         #   crashed = True
        print(event)


    gameDisplay.fill(white)
    car()
    pygame.display.update()
    clock.tick(100)

pygame.quit()
quit()
