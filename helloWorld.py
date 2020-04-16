import pygame, sys
from pygame.locals import *

#set up pygame
pygame.init()

#Set up the window
windowSurface = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Hello Pygame World!')

# Draw the background
bg = pygame.image.load("mountain.png").convert()
windowSurface.fill((0, 0, 0))
windowSurface.blit(bg, (0, 0))

# Set up the colors.
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Set up the font
simpleFont = pygame.font.SysFont(None, 48)

 # Set up the text
text = simpleFont.render('MountainGame!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery
    
# Draw the text onto the surface.
windowSurface.blit(text, textRect)
pygame.display.flip()

while True: # main game loop
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    