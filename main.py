import pygame
import random
from duck import Duck
from object import Platform

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

duck = Duck(screen)
# Start the player vertically centered
duck.pos.y = SCREEN_HEIGHT / 2

# Camera position
camera_y = 0

# Define some platforms
platforms = [
    Platform(100, 600, 400, 40),
    Platform(600, 450, 400, 40),
    Platform(200, 300, 300, 40)
]

def generate_platform(y_pos):
    width = random.randint(200, 400)
    x_pos = random.randint(0, SCREEN_WIDTH - width)
    return Platform(x_pos, y_pos, width, 40)

# Track the highest platform to know when to generate more
highest_platform_y = 300

# Score tracking
score = 0
max_height = SCREEN_HEIGHT / 2 # Initial duck height

# Load background image
background_image = pygame.image.load("image.assets/game_background.png")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

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

    # quack button
    if keys[pygame.K_SPACE]:
        duck.quack()

    duck.applyGravity(dt, platforms)

    # Update score based on height reached
    if duck.pos.y < max_height:
        score += int((max_height - duck.pos.y) / 10)
        max_height = duck.pos.y

    # Camera follow logic: if duck is in the upper half of the screen, scroll up
    if duck.pos.y < camera_y + SCREEN_HEIGHT / 2:
        camera_y = duck.pos.y - SCREEN_HEIGHT / 2

    # Procedural platform generation
    while highest_platform_y > camera_y - SCREEN_HEIGHT:
        highest_platform_y -= random.randint(150, 250)
        platforms.append(generate_platform(highest_platform_y))

    # Clean up old platforms
    platforms = [p for p in platforms if p.rect.y < camera_y + SCREEN_HEIGHT + 100]

    screen.blit(background_image, (0, 0))  # Draw the background image

    # Render platforms
    for p in platforms:
        p.draw(screen, camera_y)

    # Render the graphics here.
    duck.draw(camera_y)

    # Draw score
    font = pygame.font.Font(None, 74)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()  # Refresh on-screen display
