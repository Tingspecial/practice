import pygame
import random
import os

WIDTH = 360
HEIGHT = 480
FPS = 30

#define colors
WHITE = (255,255,255)
BLUE = (0,0,225)
BLACK = (0,0,0)

# mac: "/User/"
game_folder = os.path.dirname(__file__)
img_folder = "img/view.png"

class Player(pygame.sprite.Sprite):
    #sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/view.png").convert()
        #self.imge.fill(WHITE)
        self.image.set_colorkey(BLACK)
        self.rect= self.image.get_react()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

#game loop

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#game loop
running = True

while running:
    #processing input(event)
    clock.tick(FPS)
    for event in pygame.event.get():
        #CHECK FOR CLOSING WINDOW
        if event.type == pygame.QUIT:
            running = False
    #update
    all_sprites.update()

    #draw/ render
    # red + green = yellow; red + blue =magenta ; green + blue = cyan;
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
