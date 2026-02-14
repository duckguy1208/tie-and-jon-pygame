import pygame
from duck import Duck


pygame.init()

DARK_GREEN = (0, 100, 0)

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

duck = Duck(screen)
# Start the player vertically centered (keep x from object's random position)
duck.pos.y = screen.get_height() / 2

# Load background image
background = screen.fill(DARK_GREEN)

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    dt = clock.tick(60)
    
    # Decrement quack timer
    duck.quack_timer -= dt
    if duck.quack_timer < 0:
        duck.quack_timer = 0

    # Handle continuous arrow-key movement
    keys = pygame.key.get_pressed()
    dx = 0
    dy = 0
    if keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_UP]:
        dy = -1
    if keys[pygame.K_DOWN]:
        dy = 1
    if dx != 0 or dy != 0:
        duck.move(dx, dy, dt)
    #quack button
    if keys[pygame.K_SPACE]:
        duck.quack()

    duck.applyGravity(dt)
    screen.blit(background, (0, 0))  # Draw the background image

    # Render the graphics here.
    duck.draw()

    pygame.display.flip()  # Refresh on-screen display

    