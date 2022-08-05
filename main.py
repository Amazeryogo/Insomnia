import pygame

global continue_game
continue_game = False


class MainCharacter:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 10
        self.image = pygame.image.load("smiling_ball.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.points = 0

    def move_forward(self):
        self.rect.x += self.speed * 2

    def move_backward(self):
        self.rect.x -= self.speed * 2

    def move_up(self):
        self.rect.y -= self.speed * 2

    def move_down(self):
        self.rect.y += self.speed * 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def add_point(self):
        self.points += 1

    def get_points(self):
        return self.points


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pygame.image.load("sprite2.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def movement(self):
        self.rect.x += self.speed * 2
        self.rect.y += self.speed * 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)


pygame.init()
# make the screen
screen = pygame.display.set_mode((700, 700))
# set background
background = pygame.image.load("background.png")
screen.blit(background, (0, 0))
pygame.display.set_caption("Insomnia")

# make a start button
start_button = pygame.image.load("start_button.png")
start_button = pygame.transform.scale(start_button, (200, 100))
start_button_rect = start_button.get_rect()
start_button_rect.x = 350
start_button_rect.y = 350
screen.blit(start_button, start_button_rect)
#if the start button is clicked, the game starts
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                continue_game = True
                break
    if continue_game:
        break
    pygame.display.update()

# draw the main screen character
main_character = MainCharacter()
# draw the enemy
enemy = Enemy(100, 100)
enemy.draw(screen)
# draw the main screen character
main_character.draw(screen)
# get input from the user
while continue_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_character.move_up()
            if event.key == pygame.K_DOWN:
                main_character.move_down()
            if event.key == pygame.K_LEFT:
                main_character.move_backward()
            if event.key == pygame.K_RIGHT:
                main_character.move_forward()
    # if a sprite goes off the screen, move it back to the other side of the screen
    if main_character.rect.x > 700:
        main_character.rect.x = 0
    if main_character.rect.x < 0:
        main_character.rect.x = 0
    if main_character.rect.y > 700:
        main_character.rect.y = 0
    if main_character.rect.y < 0:
        main_character.rect.y = 0

    if enemy.rect.x > 700:
        enemy.rect.x = 0
    if enemy.rect.x < 0:
        enemy.rect.x = 0
    if enemy.rect.y > 700:
        enemy.rect.y = 0
    if enemy.rect.y < 0:
        enemy.rect.y = 0
    enemy.movement()
    # if a main character collides with an enemy, reset the game
    if main_character.rect.colliderect(enemy.rect):
        main_character.rect.x = 0
        main_character.rect.y = 0
        main_character.points = 0
        enemy.rect.x = 100
        enemy.rect.y = 100
    # draw the main screen character
    main_character.draw(screen)
    enemy.draw(screen)
    # update the screen
    pygame.display.update()
    # wait for 1/60th of a second
    pygame.time.wait(1000 // 60)
    # clear the screen
    screen.blit(background, (0, 0))
