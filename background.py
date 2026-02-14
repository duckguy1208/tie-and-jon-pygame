import pygame

class ParallaxBackground:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.layers = []
        
        # Define layers: (image_path, scroll_speed)
        # scroll_speed 0.0 means static relative to screen, 1.0 means moves with world.
        layer_configs = [
            ("assets/images/background_sky1.png", 0.05),
            ("assets/images/background_sky2.png", 0.1),
            ("assets/images/background_sky3.png", 0.2),
            ("assets/images/background_sky4.png", 0.3),
            ("assets/images/background_sky5.png", 0.4),
        ]
        
        for path, speed in layer_configs:
            try:
                img = pygame.image.load(path).convert_alpha()
                img = pygame.transform.scale(img, (screen_width, screen_height))
                self.layers.append({'image': img, 'speed': speed})
            except pygame.error:
                # Fallback: create a transparent surface if image missing
                img = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
                self.layers.append({'image': img, 'speed': speed})

    def draw(self, surface, camera_y):
        # Draw layers from furthest to closest
        for layer in self.layers:
            img = layer['image']
            speed = layer['speed']
            
            # Calculate the vertical offset for this layer
            # Using % to tile the background vertically
            y_offset = -(camera_y * speed) % self.screen_height
            
            # Draw the image and one above/below to ensure continuous coverage
            surface.blit(img, (0, y_offset))
            surface.blit(img, (0, y_offset - self.screen_height))
