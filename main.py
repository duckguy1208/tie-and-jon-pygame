import pygame
from duck import Duck



pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

duck = Duck(screen)
# Start the player vertically centered (keep x from object's random position)
duck.pos.y = screen.get_height() / 2

class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (139, 69, 19) # Brown color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Define some platforms
platforms = [
    Platform(100, 600, 400, 40),
    Platform(600, 450, 400, 40),
    Platform(200, 300, 300, 40)
]

# Load background image
background_image = pygame.image.load("image.assets/game_background.png")
background_image = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

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
    if keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_RIGHT]:
        dx = 1
    
    if dx != 0:
        duck.move(dx, 0, dt)
    
    if keys[pygame.K_UP]:
        duck.jump()

    #quack button
    if keys[pygame.K_SPACE]:
        duck.quack()

    duck.applyGravity(dt, platforms)
    screen.blit(background_image, (0, 0))  # Draw the background image

    # Render platforms
    for p in platforms:
        p.draw(screen)

    # Render the graphics here.
    duck.draw()

    pygame.display.flip()  # Refresh on-screen display

    