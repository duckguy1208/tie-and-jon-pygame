import pygame
import random
import os


class Object:
    vel = 100
    x_min = 0
    y_min = 0

    def __init__(self, surface, color = 'yellow', size = 5, sprite_size = 120):
        self.surface = surface
        self.color = color
        self.size = size
        self.sprite_size = sprite_size
        self.x_max = self.surface.get_width()
        self.y_max = self.surface.get_height()
        self.pos = self.random_position()
        # For quack text display
        self.quack_text = None
        self.quack_timer = 0
        # Load player image once (duck.png) from package assets
        assets_dir = os.path.join(os.path.dirname(__file__), 'image.assets')
        img_path = os.path.join(assets_dir, 'duck.png')
        try:
            self.player_img = pygame.image.load(img_path).convert_alpha()
            # Scale the image down to the configured sprite size
            self.player_img = pygame.transform.smoothscale(self.player_img, (self.sprite_size, self.sprite_size))
        except Exception:
            # Fallback: create a simple surface if image missing
            self.player_img = pygame.Surface((self.sprite_size, self.sprite_size), pygame.SRCALPHA)
            pygame.draw.circle(self.player_img, pygame.Color(self.color), (self.sprite_size//2, self.sprite_size//2), self.sprite_size//2)
        
        # Load quack image (duck_quack.png) if it exists
        quack_img_path = os.path.join(assets_dir, 'duck_quack.png')
        try:
            self.quack_img = pygame.image.load(quack_img_path).convert_alpha()
            self.quack_img = pygame.transform.smoothscale(self.quack_img, (self.sprite_size, self.sprite_size))
        except Exception:
            # If quack image doesn't exist, use the regular image
            self.quack_img = self.player_img

    def draw(self):
        # Use quack image if actively quacking, otherwise use regular image
        img = self.quack_img if (self.quack_timer > 0) else self.player_img
        offset = pygame.Vector2(img.get_width() / 2, img.get_height() / 2)
        dest = self.pos - offset
        self.surface.blit(img, (dest.x, dest.y))
        
        # Draw quack text if active
        if self.quack_text and self.quack_timer > 0:
            text_size = getattr(self, 'quack_text_size', 36)
            text_color = getattr(self, 'quack_color', (0, 0, 0))
            font = pygame.font.Font(None, text_size)
            text_surf = font.render(self.quack_text, True, text_color)
            text_pos = (self.pos.x - text_surf.get_width() / 2, self.pos.y - self.sprite_size / 2 - 10)
            self.surface.blit(text_surf, text_pos)
        
    def move(self, x, y, dt):
        # `dt` comes from clock.tick() in milliseconds — convert to seconds
        seconds = dt / 1000.0
        self.pos.x += x * self.vel * seconds
        self.pos.y += y * self.vel * seconds
        return self.adjust_pos()
    
    def applyGravity(self, dt):
        # apply negative y to obj 
        # position until 0
        # Gravity should only affect vertical axis (downwards)
        self.move(0, 0.2, dt)
    

    def random_position(self):
        return pygame.Vector2(self.random_x(), self.random_y())

    def random_left(self):
        return pygame.Vector2(self.random_x('left'), self.random_y())

    def random_right(self):
        return pygame.Vector2(self.random_x('right'), self.random_y())

    def random_x(self):
        return random.uniform(0 + (self.size / 2), self.surface.get_width() - (self.size / 2))

    def random_y(self):
        return random.uniform(0 + (self.size / 2), self.surface.get_height() - (self.size / 2))

    def adjust_pos(self):
        adjusted = False
        if self.pos.x < self.x_min + self.size:
            self.pos.x = self.x_min + self.size
            adjusted = True
        if self.pos.x > self.x_max - self.size:
            self.pos.x = self.x_max - self.size
            adjusted = True
        if self.pos.y < self.y_min + self.size:
            self.pos.y = self.y_min + self.size
            adjusted = True
        if self.pos.y > self.y_max - self.size:
            self.pos.y = self.y_max - self.size
            adjusted = True
        return adjusted
    
def objectFactory(x, y):
    return Object(pygame.Vector2(x, y))