import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ship Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ship
ship = pygame.Rect(WIDTH//2 - 25, HEIGHT - 60, 50, 50)
ship_speed = 5

# Bullets
bullets = []
bullet_speed = 7

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire bullet
                bullets.append(pygame.Rect(ship.centerx-5, ship.top-10, 10, 20))

    # Keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship.left > 0:
        ship.x -= ship_speed
    if keys[pygame.K_RIGHT] and ship.right < WIDTH:
        ship.x += ship_speed

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, ship)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    pygame.display.flip()
    clock.tick(60)
