import pygame

#this is a comment,just for practice
def test():
    print("just a test")
pygame.init()
display_width = 600
display_height = 400

black =(0,0,0)
white = (255,255,255)
red = (255,0,0)
blue =(0,0,255)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width, display_width))
pygame.display.set_caption('A game')
clock = pygame.time.Clock()

carImg = pygame.image.load('img/car.jpg')
carImg = pygame.transform.scale(carImg,(50,50))


def car(x,y):
    gameDisplay.blit(carImg,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        #print(event)

    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
