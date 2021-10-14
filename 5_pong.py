import pygame
import sys
import random


def ball_animation():

    global ball_speed_y
    global ball_speed_x

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.left <= 0 or ball.right >= WIDTH:
        ball_restart()
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT

def opponent_ai():
    if opponent.top < ball.y - 10:
        opponent.top += opponent_speed+50
    if opponent.bottom > ball.y + 10:
        opponent.bottom -= opponent_speed+50
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.top >= HEIGHT:
        opponent.top = HEIGHT

def ball_restart():
    global ball_speed_y, ball_speed_x

    ball.center = (WIDTH/2, HEIGHT/2)
    ball_speed_y = 7 * (random.choice((1, -1)))
    ball_speed_x = 7 * (random.choice((1, -1)))

# initialisation
pygame.init()
clock = pygame.time.Clock()

# screen setup
WIDTH = 1280
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pong")

# game rectangles
ball = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 30, 30)
player = pygame.Rect(WIDTH - 20, HEIGHT/2 - 70, 10, 140)
opponent = pygame.Rect(10, HEIGHT/2 - 70, 10, 140)

bg_colour = pygame.Color('grey12')
light_grey = (200, 200, 200)

# game variables
ball_speed_x = 7 * (random.choice((1, -1)))
ball_speed_y = 7
player_speed = 0
opponent_speed = 7


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 10
            if event.key == pygame.K_DOWN:
                player_speed += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed = 0
            if event.key == pygame.K_DOWN:
                player_speed = 0

    ball_animation()
    player_animation()
    opponent_ai()


    # visual
    screen.fill(bg_colour)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (WIDTH/2, 0), (WIDTH/2, HEIGHT))

    pygame.display.flip()   # flip used instead of update to update the entire screen everytime
    clock.tick(60)
