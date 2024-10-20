import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
WHITE = (255, 255, 255)


# Sprite class with mask support
class MaskedSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, pos):
        super().__init__()
        self.image = pygame.image.load(
            image_path
        ).convert_alpha()  # Load image with transparency
        self.rect = self.image.get_rect(topleft=pos)
        self.mask = pygame.mask.from_surface(self.image)  # Create a mask from the image

    def update(self, dx, dy):
        # Move sprite by updating its rect
        self.rect.x += dx
        self.rect.y += dy


# Load two sprites
sprite1 = MaskedSprite("sprite1.png", (100, 100))  # Example path to image
sprite2 = MaskedSprite("sprite2.png", (300, 200))  # Example path to image

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement example (move sprite1 with arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1.update(-5, 0)
    if keys[pygame.K_RIGHT]:
        sprite1.update(5, 0)
    if keys[pygame.K_UP]:
        sprite1.update(0, -5)
    if keys[pygame.K_DOWN]:
        sprite1.update(0, 5)

    # Check for collision using masks
    if pygame.sprite.collide_mask(sprite1, sprite2):
        print("Collision detected!")

    # Clear the screen
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
