import pygame

pygame.init()
dark_blue = (44, 44, 127)

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

# loop 
# 1. Event Handling
# 2. Updating positions
# 3. Drawing objects

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #color
    screen.fill(dark_blue)
    pygame.display.update()
    clock.tick(60)
