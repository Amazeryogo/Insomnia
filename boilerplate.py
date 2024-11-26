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
                    if event.key == pygame.K_q:
                        continue_game = False
    # if a sprite goes off the screen, move it back to the other side of the screen
    gearboy.GeneralFunctions.overflow(xsf['x'], xsf['y'], main_character)
    enemy.movement()
    gearboy.GeneralFunctions.overflow(xsf['x'], xsf['y'], enemy)
    # if a main character collides with an enemy, reset the game

    if gearboy.GeneralFunctions.check_collision(main_character, enemy):
        main_character.rect.x = random.randint(0, 700)
        main_character.rect.y = random.randint(0, 700)
        enemy.rect.x = random.randint(0, 700)
        enemy.rect.y = random.randint(0, 700)
        if main_character.saber:
            x = random.randint(0, 3)
            if x == 1:
                enemy.remove_health()
                main_character.remove_health()
            else:
                enemy.remove_health()
        else:
            main_character.remove_health()

    if gearboy.GeneralFunctions.check_collision(main_character, health_point):
        health_point.rect.x = random.randint(0, 700)
        health_point.rect.y = random.randint(0, 700)
        main_character.add_health()

    if gearboy.GeneralFunctions.check_collision(main_character, saber):
        saber.rect.x = random.randint(0, 900)
        saber.rect.y = random.randint(0, 900)
        saber.acquired = True
        main_character.saber = True
        main_character.image = pygame.transform.scale(pygame.image.load("images/mcws1.png"), (64, 64))
        textbox.add_text("SABER ACQUIRED!", screen, 250, 600)
        pygame.display.update()

    for k in tnt:
        if gearboy.GeneralFunctions.check_collision(main_character,k) :
            main_character.rect.x = random.randint(0, 700)
            main_character.rect.y = random.randint(0, 700)
            if not k.blasted:
                main_character.remove_health()
                main_character.remove_health()
                k.image = pygame.transform.scale(pygame.image.load("images/bomb_blasted.png"), (64, 64))
                k.blasted = True
            elif k.blasted:
                main_character.remove_health()
            pygame.display.update()

    for k in tnt:
        if gearboy.GeneralFunctions.check_collision(enemy,k):
            if k.blasted:
                enemy.add_health()

            pygame.display.update()

    gearboy.GeneralFunctions.overflow(xsf['x'], xsf['y'], health_point)
    gearboy.draw_hearts(screen, 0, 0, main_character, HEART)

    if enemy.health <= 0:
        DRAW_ENEMY = False
        enemy.speed = 0
        enemy.rect.x = 900
        enemy.rect.y = 900
        textbox.add_text("", screen, 250, 600)
        textbox.add_text("Congratulations You killed the ghost!", screen, 0, 600)
        pygame.display.update()
    elif main_character.health <=0:
        DRAW_ENEMY = False
        enemy.speed = 0
        enemy.rect.x = 900
        enemy.rect.y = 900
        textbox.add_text("", screen, 250, 600)
        textbox.add_text("Oh no, you lost!", screen, 0, 600)
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
    for k in tnt:
        k.draw(screen)
    gearboy.draw_hearts(screen, 550, 0, enemy, BLACKHEART)
    gearboy.draw_hearts(screen, 0, 0, main_character, HEART)
    # update the screen
    pygame.display.update()
    # wait for 1/60th of a second
    pygame.time.wait(1000 // 60)
    # clear the screen
    screen.blit(background, (0, 0))