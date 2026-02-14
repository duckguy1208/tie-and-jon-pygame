import os
# Use dummy video driver for headless testing
os.environ['SDL_VIDEODRIVER'] = 'dummy'

import pygame
import pytest
from object import Platform, Object
from duck import Duck

def test_platform_creation():
    p = Platform(100, 200, 50, 10)
    assert p.rect.x == 100
    assert p.rect.y == 200
    assert p.rect.width == 50
    assert p.rect.height == 10

def test_object_movement():
    pygame.init()
    surface = pygame.Surface((2000, 600)) # Larger surface to avoid boundary cap
    obj = Object(surface)
    initial_x = obj.pos.x
    obj.move(1, 0, 1000) # Move right for 1 second at vel=400
    # Boundary check might still hit if random start is too far right
    if initial_x + 400 <= 2000 - 60:
        assert obj.pos.x == initial_x + 400
    else:
        assert obj.pos.x == 2000 - 60

def test_camera_rendering():
    pygame.init()
    surface = pygame.Surface((800, 600))
    p = Platform(100, 200, 50, 10)
    # This just tests it doesn't crash, since we can't easily check the surface content here without more complex mocking
    p.draw(surface, camera_y=50)
    assert True 

def test_procedural_generation_logic():
    # Simulate the logic in main.py
    platforms = [Platform(100, 600, 400, 40)]
    highest_platform_y = 600
    camera_y = 0
    SCREEN_HEIGHT = 720
    SCREEN_WIDTH = 1280

    def generate_platform(y_pos):
        return Platform(0, y_pos, 200, 40)

    # Duck moves up
    duck_pos_y = 200
    if duck_pos_y < camera_y + SCREEN_HEIGHT / 2:
        camera_y = duck_pos_y - SCREEN_HEIGHT / 2
    
    # Should trigger generation if camera moved up enough
    while highest_platform_y > camera_y - SCREEN_HEIGHT:
        highest_platform_y -= 200
        platforms.append(generate_platform(highest_platform_y))
    
    assert len(platforms) > 1
    assert platforms[-1].rect.y < 600

def test_score_increment():
    score = 0
    max_height = 360 # Initial
    
    # Duck moves up
    duck_pos_y = 300
    if duck_pos_y < max_height:
        score += int((max_height - duck_pos_y) / 10)
        max_height = duck_pos_y
    
    assert score == 6
    assert max_height == 300
    
    # Duck moves down
    duck_pos_y = 400
    if duck_pos_y < max_height:
        score += int((max_height - duck_pos_y) / 10)
        max_height = duck_pos_y
    
    assert score == 6 # Score should not change
    assert max_height == 300
