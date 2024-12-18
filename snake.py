# TODO: don't forget to pip install pygame in the terminal.  Else pygame functions won't be recognized.
import pygame.random

pygame.innit()

window_display = WINDOW_WIDTH, WINDOW_HEIGHT
WIDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode passing
# in a tuple of WINDOW_WIDTH and WINDOW_HEIGHT
pygame.display.set_caption(~~snake~~)

# Set FSP and clock
FPS = 20
CLOCK = pygame.time.clock()

# Set game values
SNAKE_SIZE = 20
head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT // 2 + 100
snake_dx = 0
snake_dy = 0
score = 0

# Set colors
RED = 50, 0, 0
GREEN = 0, 50, 0
WHITE = 0, 0, 0
DARKGREEN = 10, 50, 20
DARKRED = 150, 0, 0

# Set fonts
font = pygame.font.SysFont('gabriola', 48)


# Set text

def create_text_and_rect(text, color, background_color, **locations):
    text = font.render(text, True, color, background_color)
    rect = text.get_rect()
    for location in locations.keys():
        if location == "center":
            rect.center = locations[location]
        if location == "topleft":
            rect.topleft = locations[location]
    return text, rect


# TODO: Here is a usage example for the rest of the text and rectangles that you'll create.
title_text, title_rect = create_text_and_rect("~~Snake~~", GREEN, DARKRED,
                                             center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

Score_text, score_rect = create_text_and_rect("~~snake~~", GREEN, DARKRED,
                                              topright=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
text = "score": str(score)
color = GREEN
background_color = DARKRED
locations: topleft = (10, 10)

game_over_text, game_over_rect = create_text_and_rect("~~snake~~", GREEN, DARKRED,
                                                      text: ("GAMEOVER"))
color = RED
background_color = DARKGREEN
locations = center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text, continue_rect = create_text_and_rect("~~snake~~", RED, DARKGREEN,
                                                    text = ("Press any key to play again")
                                                    locations = center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

# Set sounds and music
pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

body_coord = []


# The main game loop
running = True
is_paused = False


def move_snake(event):
    global snake_dx, snake_dy
    if event.type == pygame.KEYDOWN:
        key = event.key
        if key = pygame.K_LEFT
            snake_dx = -1 * SNAKE_SIZE
        snake_dy = 0
    if key = pygame.K_RIGHT
        snake_dx = SNAKE_SIZE
snake_dy = 0
if key = pygame.K_UP
    snake_dx = 0
snake_dy = -1 * SNAKE_SIZE
if key = pygame.K_DOWN
    snake_dx = 0
snake_dy = SNAKE_SIZE




def check_quit(event):
    global running
    if event = pygame.quit
    running = false


def check_events():
    global running
    pygame.event.get())
        check_quit(event)
        move_snake(event)

def handle_snake():
    global body_coords
    global head_x
    global head_y
    global head_coord
    body_coords.insert(0), head_coord
    body_coords.pop()
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, SNKAE_SIZE, SNAKE_SIZE)


def reset_game_after_game_over(event):
    global is_paused, score, head_x, head_y, head_coord, body_coords, snake_dx, snake_dy
    if event.type = pygame_KEYDOWN
        score = 0
    head_x = WINDOW_WIDTH // 2
    head_y = WINDOW_HEIGHT // 2 + 100
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
    body_coord = ()
    snake_dx = 0
    snake_dy = 0
    is_paused = false

def check_end_game_after_game_over(event):
    global is_paused
    global running
    if event.type = pygame.QUIT
        is_paused = false
    running = false

def check_game_over():
    global head_rect
    global head_coord
    global body_coords
    global running
    global is_paused

   if head_rect.left -, head_rect.right += WINDOW_WIDTH head_rect.top - head_rect.bottom += WINDOW_HEIGHT
       display_surface.blit(game_over_text, game_over_rect)
display_surface.blit(continue_text, continue_rect)
pygame.display.update()
is_paused = true
while is_paused
    pygame.event.get()
    reset_gam_after_game_over(event)
    check_end_game_after_game_over(event)

def check_collisions():
    global score, apple_x, apple_y, apple_coord, body_coords
    if head_rect.collicirect(apple_rect) score += 1
        pick_up_sound.play()
    apple_x = random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
    apple_y = random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
    apple_coord = (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
    body_coords.append(head_coord)


def blit_hud():
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)


def blit_assets():
    # TODO: for body in body_coords:
    pygame.draw.rect(display_surface, DARKGREEN, body)
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)


def update_display_and_tick_clock():
    pygame.display.update()
    clock.tick(FPS)


while running:
    # Check pygame events
    check_events()

    # handle growing and manipulating the snake
    handle_snake()

    # Check for game over
    check_game_over()

    # Check for collisions
    check_collisions()

    # Update HUD
    score_text = font.render("Score: " + str(score), True, GREEN, DARKRED)

    # Fill the surface
    display_surface.fill(WHITE)

    # Blit HUD
    blit_hud()

    # Blit assets
    blit_assets()

    # Update display and tick clock
    update_display_and_tick_clock()

# End the game
pygame.quit()
