import pygame
import random

pygame.init()

width = 600
height = 600
fps = 60
red = (255, 0, 0)
green = (75, 145, 0)
blue = (0, 0, 255)
snake = (75, 145, 0)
wall = (155, 225, 0)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()


class Player():
    def __init__(self):
        self.x = 30
        self.y = 30
        self.width = 15
        self.height = 15
        self.color = snake
        self.speed_x = 0
        self.speed_y = 0

    def Draw(self):
        pygame.draw.rect(window, self.color, [self.x, self.y, self.width, self.height])

    def Move(self):
        if keys[pygame.K_DOWN] and self.speed_y != -1:
            self.speed_y = 1
            self.speed_x = 0
        if keys[pygame.K_UP] and self.speed_y != 1:
            self.speed_y = -1
            self.speed_x = 0
        if keys[pygame.K_LEFT] and self.speed_x != 1:
            self.speed_x = -1
            self.speed_y = 0
        if keys[pygame.K_RIGHT] and self.speed_x != -1:
            self.speed_x = 1
            self.speed_y = 0
        self.x += self.speed_x * 15
        self.y += self.speed_y * 15


class Food():
    def __init__(self):
        self.x = (random.randint(0, (width / 15) - 15)) * 15
        self.y = (random.randint(0, (height / 15) - 15)) * 15
        self.color = green
        self.width = 15
        self.height = 15

    def Draw(self):
        pygame.draw.rect(window, self.color, [self.x, self.y, self.width, self.height])


def Collision():
    if player.x == food.x and player.y == food.y:
        food.x = (random.randint(0, (width / 15) - 15)) * 15
        food.y = (random.randint(0, (height / 15) - 15)) * 15
        snake_tail.append([player.x, player.y])
    if player.x >= width:
        player.x = 0
    if player.x < 0:
        player.x = width
    if player.y >= height:
        player.y = 0
    if player.y < 0:
        player.y = height


snake_tail = []


def Snake_tail():
    for i in range(len(snake_tail)):
        a = len(snake_tail) - i - 1
        if a > 0:
            snake_tail[a] = snake_tail[a - 1]
        else:
            snake_tail[a] = [player.x, player.y, player.width, player.height]


def Collision_with_snake_tail():
    for i in range(len(snake_tail)):
        if i != 0:
            if snake_tail[0] == snake_tail[i]:
                print("Game over Мешок")



player = Player()
food = Food()
snake_tail.append([player.x, player.y, player.width, player.height])

tick = 0
level = 6
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    window.fill(wall)

    if tick == level:
        player.Move()
        Collision()
        Snake_tail()
        Collision_with_snake_tail()
        tick = 0
        if len(snake_tail) == 10:
            level = 5
        if len(snake_tail) == 20:
            level = 4
        if len(snake_tail) == 30:
            level = 3
        if len(snake_tail) == 40:
            level = 2
        if len(snake_tail) == 50:
            level = 1
    else:
        tick += 1
    for i in range(len(snake_tail)):
        pygame.draw.rect(window, player.color, snake_tail[i])
    player.Draw()
    food.Draw()
    clock.tick(fps)
    pygame.display.update()
pygame.quit()