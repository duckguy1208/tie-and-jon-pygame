import pygame
from duck import Duck


pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

duck = Duck(screen)


while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    dt = clock.tick(60)
    duck.applyGravity(dt)
    screen.fill("green")  # Fill the display with a solid color

    # Render the graphics here.
    duck.draw()


    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
