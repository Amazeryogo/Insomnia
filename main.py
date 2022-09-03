import gearboy
import pygame
import random
from gearboy import xsf

global continue_game, LEVEL, DRAW_ENEMY
continue_game = False
LEVEL = 1
DRAW_ENEMY = True
BACKGROUND_IMAGE = "images/background.jpg"
STARTSCREEN = "images/startscreen.png"
STARTBUTTON = "images/startbutton.png"
HEART = "images/health.png"
GREYHEART = "images/greyheart.png"
BLACKHEART = "images/blackheart.png"
GHOST = "images/spirit.png"

pygame.init()
# make the screen
screen = pygame.display.set_mode((xsf['x'], xsf['y']))
# set background
background = pygame.image.load(STARTSCREEN)
background = pygame.transform.scale(background, (700, 700))
screen.blit(background, (0, 0))
pygame.display.set_caption("Insomnia")
# make a start button
start_button = pygame.image.load(STARTBUTTON)
start_button = pygame.transform.scale(start_button, (200, 100))
start_button_rect = start_button.get_rect()
start_button_rect.x = 250
start_button_rect.y = 250
screen.blit(start_button, start_button_rect)
# if the start button is clicked, the game starts
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                continue_game = True
                break
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if continue_game:
        break
    pygame.display.update()

# draw the main screen character
main_character = gearboy.UserControlledObject(0, 0, 50, "images/mc2.png", 0, 3)
# draw the enemy
enemy = gearboy.NonUserControlledObject(100, 0, 2, GHOST)
enemy.draw(screen)
# draw the main screen character
main_character.draw(screen)
# get input from the user
background = pygame.image.load(BACKGROUND_IMAGE)

health_point = gearboy.HealthPoints(100, 100, GREYHEART, screen)

saber = gearboy.Saber(300, 300, "images/saber1.png", screen)

font = pygame.font.SysFont('Atari', 30)
textbox = gearboy.Textbox(0, 600, 700, 600, font)

screen.blit(background, (0, 0))
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
    gearboy.Sakazuki.overflow(xsf['x'], xsf['y'], main_character)
    enemy.movement()
    gearboy.Sakazuki.overflow(xsf['x'], xsf['y'], enemy)
    # if a main character collides with an enemy, reset the game

    if gearboy.Sakazuki.check_collision(main_character, enemy):
        main_character.rect.x = random.randint(0, 700)
        main_character.rect.y = random.randint(0, 700)
        enemy.rect.x = random.randint(0, 700)
        enemy.rect.y = random.randint(0, 700)
        if main_character.saber:
            x = random.randint(0,3)
            if x == 1:
                enemy.remove_health()
                main_character.remove_health()
            else:
                enemy.remove_health()
        else:
            main_character.remove_health()

    if gearboy.Sakazuki.check_collision(main_character, health_point):
        health_point.rect.x = random.randint(0, 700)
        health_point.rect.y = random.randint(0, 700)
        main_character.add_health()

    if gearboy.Sakazuki.check_collision(main_character, saber):
        saber.rect.x = random.randint(0, 900)
        saber.rect.y = random.randint(0, 900)
        saber.acquired = True
        main_character.saber = True
        main_character.image = pygame.transform.scale(pygame.image.load("images/mcws1.png"), (64, 64))
        textbox.add_text("SABER ACQUIRED!",screen,250,600)
        pygame.display.update()



    gearboy.Sakazuki.overflow(xsf['x'], xsf['y'], health_point)
    gearboy.draw_hearts(screen, 0, 0, main_character, HEART)

    if main_character.health == 0:
        continue_game = False
        # display text that the game is over
        font = pygame.font.Font("Atari", 50)
        text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(text, (250, 250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            else:
                continue_game = True
                break
    if enemy.health == 0:
        DRAW_ENEMY = False
        enemy.speed = 0
        enemy.rect.x = 900
        enemy.rect.y = 900
        textbox.add_text("",screen,250,600)
        textbox.add_text("Congratulations You killed the ghost!",screen,0,600)
        pygame.display.update()

    if DRAW_ENEMY:
        enemy.draw(screen)
    if not saber.acquired:
        saber.draw(screen)
        health_point.draw(screen)
    else:
        health_point.rect.x = 900
        health_point.rect.y = 900
    main_character.draw(screen)
    gearboy.draw_hearts(screen, 550, 0, enemy, BLACKHEART)
    gearboy.draw_hearts(screen, 0, 0, main_character, HEART)
    # update the screen
    pygame.display.update()
    # wait for 1/60th of a second
    pygame.time.wait(1000 // 60)
    # clear the screen
    screen.blit(background, (0, 0))
