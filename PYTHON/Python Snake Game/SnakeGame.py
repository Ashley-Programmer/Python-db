# import libraries
import pygame
import time
import random

snake_speed = 15

# window size
window_X = 720
window_Y = 480

# define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# initializing the pygame
pygame.init()
# initializing game window
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_X, window_Y))

# fps (frames per sec) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]
# defining first 4 blocks of snake body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# fruit position
fruit_position = [random.randrange(1, (window_X // 10)) * 10,
                  random.randrange(1, (window_Y // 10)) * 10]

fruit_spawn = True
# setting default snake direction, towards right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0
# displaying score function


def show_score(choice, color, font, size):
    # create font object score_font
    score_font = pygame.font.SysFont(font, size)
    # create the display surface object score_surface
    score_surface = score_font.render('Score: ' + str(score), True, color)
    # create a rectangular object for the text surface object
    score_react = score_surface.get_rect()
    # displaying text
    game_window.blit(score_surface, score_react)


# game over function
def game_over():
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    # creating a text surface on which text will be drawn
    game_over_react = game_over_surface.get_rect()
    # setting position of the text
    game_over_react.midtop = (window_X / 2, window_Y / 4)
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_react)
    pygame.display.flip()
    # after 2 seconds we will quit the program
    time.sleep(2)
    # deactivating pygame library
    pygame.quit()
    # quit the program
    quit()
# Main Function
