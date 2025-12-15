import pygame
import random
import sys
import numpy as np
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Circle Catch Game')
parser.add_argument('-nosound', action='store_true', help='Disable sound effects')
args = parser.parse_args()

# Initialize Pygame
pygame.init()
if not args.nosound:
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# Constants
CIRCLE_RADIUS = 100
INITIAL_WIDTH = 800
INITIAL_HEIGHT = 600
CIRCLE_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (255, 255, 255)  # White

# Create the display window (resizable)
screen = pygame.display.set_mode((INITIAL_WIDTH, INITIAL_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Circle Catch Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

def get_random_position(screen_width, screen_height):
    """Generate a random position for the circle that fits within the screen."""
    x = random.randint(CIRCLE_RADIUS, screen_width - CIRCLE_RADIUS)
    y = random.randint(CIRCLE_RADIUS, screen_height - CIRCLE_RADIUS)
    return x, y

def get_random_color():
    """Generate a random RGB color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def generate_sound(frequency, duration=0.1):
    """Generate a simple beep sound at the given frequency."""
    sample_rate = 22050
    samples = int(sample_rate * duration)
    wave = np.sin(2 * np.pi * frequency * np.linspace(0, duration, samples))
    # Apply fade out to avoid clicking
    fade_samples = int(sample_rate * 0.01)
    wave[-fade_samples:] *= np.linspace(1, 0, fade_samples)
    # Convert to 16-bit integers
    wave = (wave * 32767).astype(np.int16)
    # Create stereo sound
    stereo_wave = np.zeros((samples, 2), dtype=np.int16)
    stereo_wave[:, 0] = wave
    stereo_wave[:, 1] = wave
    sound = pygame.sndarray.make_sound(stereo_wave)
    return sound

def play_random_sound():
    """Play a random beep sound."""
    if args.nosound:
        return
    # Random frequency between 300 and 1000 Hz
    frequency = random.randint(300, 1000)
    sound = generate_sound(frequency, duration=0.15)
    sound.play()

def is_mouse_over_circle(mouse_pos, circle_pos, radius):
    """Check if the mouse is over the circle."""
    mx, my = mouse_pos
    cx, cy = circle_pos
    distance = ((mx - cx) ** 2 + (my - cy) ** 2) ** 0.5
    return distance <= radius

# Get initial screen size
screen_width, screen_height = screen.get_size()

# Initial circle position and color
circle_pos = get_random_position(screen_width, screen_height)
circle_color = get_random_color()

# Counter for touches
touch_count = 0

# Font for displaying the counter
font = pygame.font.Font(None, 48)  # None uses default font, 48 is the size

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Update screen size when window is resized
            screen_width, screen_height = event.w, event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            # Reposition circle if it's now outside the new window bounds
            cx, cy = circle_pos
            if (cx - CIRCLE_RADIUS < 0 or cx + CIRCLE_RADIUS > screen_width or
                cy - CIRCLE_RADIUS < 0 or cy + CIRCLE_RADIUS > screen_height):
                circle_pos = get_random_position(screen_width, screen_height)
                circle_color = get_random_color()
                play_random_sound()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if mouse is over the circle
    if is_mouse_over_circle(mouse_pos, circle_pos, CIRCLE_RADIUS):
        # Generate new random position and color
        circle_pos = get_random_position(screen_width, screen_height)
        circle_color = get_random_color()
        play_random_sound()
        # Increment touch counter
        touch_count += 1

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the circle
    pygame.draw.circle(screen, circle_color, circle_pos, CIRCLE_RADIUS)

    # Draw the counter at the top right
    counter_text = font.render(f'{touch_count}', True, (0, 0, 0))  # Black text
    counter_rect = counter_text.get_rect()
    counter_rect.topright = (screen_width - 10, 10)  # 10 pixels from top-right corner
    screen.blit(counter_text, counter_rect)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()
