import pygame
import time
import random

pygame.init()

# defining colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display settings
dis_width = 1080
dis_height = 720

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("The Snake Game")

clock = pygame.time.Clock()

snake_block = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, pos)


def gameLoop():
    game_over = False
    game_close = False

    # Initial position
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    snake_speed = 15  # Default speed
    difficulty = "Medium"  # Default difficulty
    # Main menu
    while True:
        dis.fill(blue)
        message("Choose Difficulty:", yellow, [dis_width / 6, dis_height / 3 - 30])
        message("1. Easy", red if difficulty == "Easy" else yellow, [dis_width / 6 + 200, dis_height / 3])
        message("2. Medium", red if difficulty == "Medium" else yellow, [dis_width / 6 + 350, dis_height / 3])
        message("3. Hard", red if difficulty == "Hard" else yellow, [dis_width / 6 + 500, dis_height / 3])
        message("Press Enter to Start, ESC to Exit", yellow, [dis_width / 6, dis_height / 2])

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    snake_speed = 10
                    difficulty = "Easy"
                elif event.key == pygame.K_2:
                    snake_speed = 15
                    difficulty = "Medium"
                elif event.key == pygame.K_3:
                    snake_speed = 20
                    difficulty = "Hard"
                elif event.key == pygame.K_RETURN:
                    break
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.update()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            break

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press ENTER to Play Again or ESC to Quit", red, [dis_width / 6, dis_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameLoop()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        message(f"Difficulty: {difficulty}", white, [dis_width - 200, 10])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
