import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Define the snake and food
snake_block = 20
snake_speed = 15

# Define the game loop
def gameLoop():

    game_over = False
    game_close = False

    # Initialize the snake's position
    snake_x = window_width / 2
    snake_y = window_height / 2

    # Initialize the snake's direction
    snake_direction_x = 0
    snake_direction_y = 0

    # Initialize the snake's length
    snake_list = []
    snake_length = 1

    # Define the food's initial position
    food_x = round(random.randrange(0, window_width - snake_block) / 20.0) * 20
    food_y = round(random.randrange(0, window_height - snake_block) / 20.0) * 20

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            game_window.fill(white)
            font_style = pygame.font.SysFont(None, 50)
            msg = font_style.render("You Lost! Press C-Play Again or Q-Quit", True, black)
            game_window.blit(msg, [window_width / 6, window_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_direction_x = -snake_block
                    snake_direction_y = 0
                elif event.key == pygame.K_RIGHT:
                    snake_direction_x = snake_block
                    snake_direction_y = 0
                elif event.key == pygame.K_UP:
                    snake_direction_y = -snake_block
                    snake_direction_x = 0
                elif event.key == pygame.K_DOWN:
                    snake_direction_y = snake_block
                    snake_direction_x = 0

        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_close = True

        snake_x += snake_direction_x
        snake_y += snake_direction_y
        game_window.fill(white)
        pygame.draw.rect(game_window, green, [food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake_body(snake_block, snake_list)
        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, window_width - snake_block) / 20.0) * 20
            food_y = round(random.randrange(0, window_height - snake_block) / 20.0) * 20
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def snake_body(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, black, [x[0], x[1], snake_block, snake_block])

gameLoop()