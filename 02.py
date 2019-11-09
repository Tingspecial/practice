#crash boundary
import pygame
import time

pygame.init()
display_width = 600
display_height = 600

black =(0,0,0)
white = (255,255,255)
red = (255,0,0)
blue =(0,0,255)
green = (0,255,0)
car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_width))
pygame.display.set_caption('A small game')
clock = pygame.time.Clock()

carImg = pygame.image.load('img/car.jpg')
carImg = pygame.transform.scale(carImg,(73,73))


def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text,True,blue)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 80)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(2)
    #game_loop()

def crash():
    message_display("Good Luck!")

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    crashed = False
    x_change = 0

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            #print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 5
                elif event.key == pygame.K_RIGHT:
                    x_change += 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)
        car(x,y)

        if x > display_width - car_width or x < 0:
            #crashed = True
            crash()

        clock.tick(30)
        pygame.display.update()

game_loop()
pygame.quit()
quit()
