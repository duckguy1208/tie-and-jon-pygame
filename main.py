import pygame
from duck import Duck



pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

duck = Duck(screen)
# Start the player vertically centered (keep x from object's random position)
duck.pos.y = screen.get_height() / 2

DARK_GREEN = (0, 100, 0)

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

<<<<<<< HEAD
    screen.fill("yellow")  # Fill the display with a solid color
    player_img = pygame.image.load('image.assets/duck.png').convert_alpha()
=======
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
    screen.fill(DARK_GREEN)  # Fill the display with a solid color
>>>>>>> 7f37da2fd09b5cc5b1a1c381c56819f970afd5b8

    # Render the graphics here.
    duck.draw()

    pygame.display.flip()  # Refresh on-screen display

    