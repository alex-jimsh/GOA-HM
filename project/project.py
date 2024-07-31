import pygame #importing daddy pygame

pygame.init()

#setting x,y details
screen_width = 800
screen_length = 500

#clock variable for setting fps later
clock = pygame.time.Clock()

#setting details for screen, background, floor, enemy(snail)
screen = pygame.display.set_mode((screen_width, screen_length))
background_surface = pygame.image.load('img/darknight.jpg').convert()
ground_surface = pygame.image.load('img/ground.png').convert()
snail_surface = pygame.image.load('img/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 430))
game_over = pygame.image.load('img/game over.jpg').convert()
victory = pygame.image.load('img/victory.png').convert()
victory_font = pygame.font.Font('ttf/rock.ttf', 70)
main_surf = victory_font.render('MetalRun', False, 'red')
victory_surface = victory_font.render('Victory', False, 'white')
victory_surface1 = victory_font.render('YOU ROCK', False, 'white')
#creating sigma bicker and setting him
player_surface = pygame.image.load('img/bikerhd3.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (50, 442))

player_gravity = 0

# this is for collisions and game over and stuff
prev_collision = False 
collision_count = 0
game_over_displayed = False

#victory big W
victory_count = 0
victory_lap = 5 #gamer reaches this he is the winner horeyyyy
victory_achive = False

#heart system
heart_surface = pygame.image.load('img/heart.png').convert_alpha()
max_hearts = 3
hearts = max_hearts

#start menu
def menu():
    menu_font = pygame.font.Font('ttf/Rock.ttf', 50)
    main_menu = menu_font.render('Main Menu', False, 'white')
    start_game = menu_font.render('Start Game', False, 'white')
    Quit_game = menu_font.render('Quit', False, 'white')
    while True:
        screen.fill((0,0,0))
        screen.blit(main_menu, (300, 150))
        screen.blit(start_game, (300, 250))
        screen.blit(Quit_game, (300, 350))
        
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
             pygame.quit()
             exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
           if 300 <= event.pos[0] <= 500 and 250 <= event.pos[1] <= 350:
               return
           if 300 <= event.pos[0] <= 500 and 350 <= event.pos[1] <= 450:
               pygame.quit()
               exit()

        pygame.display.flip()
            
def losing():
    menu_font = pygame.font.Font('ttf/Rock.ttf', 50)
    # start_surface = menu_font.render('Play Again', False, 'white')
    quit_surface = menu_font.render('Quit', False, 'white')

    while True:
        screen.fill((0, 0, 0))
        # screen.blit(start_surface, (300, 50))
        screen.blit(game_over, (279, 128))
        screen.blit(quit_surface, (320, 400))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if 300 <= event.pos[0] <= 500 and 50 <= event.pos[1] <= 100:
                #     return  # start game
                if 320 <= event.pos[0] <= 500 and 400 <= event.pos[1] <= 450:
                    pygame.quit()
                    exit()
        pygame.display.flip()
def winning():
    menu_font = pygame.font.Font('ttf/Rock.ttf', 50)
    # start_surface = menu_font.render('Play Again', False, 'white')
    quit_surface = menu_font.render('Quit', False, 'white')

    while True:
        screen.fill((0, 0, 0))
        # screen.blit(start_surface, (550, 200))
        screen.blit(victory, (240, 110))
        screen.blit(victory_surface, (280, 50))
        screen.blit(quit_surface, (550, 300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if 550 <= event.pos[0] <= 800 and 200 <= event.pos[1] <= 300:
                #     return  # start game
                if 550 <= event.pos[0] <= 750 and 300 <= event.pos[1] <= 400:
                    pygame.quit()
                    exit()
        pygame.display.flip()
#main loop of game

run = True
menu()
while run:
    clock.tick(60)#fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
        

    keys = pygame.key.get_pressed()

     # Applying gravity to player
    player_gravity += 1
    player_rect.y += player_gravity

    #now time for our stupid dude to stop some
    if player_rect.bottom >= 442:
        player_rect.bottom = 442
        player_gravity = 0

    
    # Moving snail
    snail_rect.x -= 4
    if snail_rect.right < 0:
        snail_rect.left = screen_width
    #player dont go missing bye bye
    if player_rect.left > 800:
        player_rect.right = 0
        victory_count += 1
        lap_left = victory_lap - victory_count
        print(f'Lap left: {lap_left}')
    if victory_count >= victory_lap:
        victory_achive = True
    
    # Drawing everything on the screen
    screen.blit(background_surface, (0, 0))
    screen.blit(ground_surface, (0, 420))
    screen.blit(main_surf, (270, 50))
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
    
    for i in range(hearts):
        screen.blit(heart_surface, (10 + i * 40, 10))
    
    if keys[pygame.K_a] == True:
       player_rect.move_ip(-5, 0)
    if keys[pygame.K_d] == True:
       player_rect.move_ip(7, 0)
    if keys[pygame.K_s] == True:
       player_rect.move_ip(0, 5)
    if keys[pygame.K_w] == True:
       player_rect.move_ip(0, -5)
    
    # looking for collision (later thats gonna deal damage)
    if player_rect.colliderect(snail_rect) and not prev_collision:
        collision_count += 1
        hearts -= 1
        print(f'Hearts left: {hearts}')
        prev_collision = True

    # Reset collision flag if no longer colliding
    if not player_rect.colliderect(snail_rect):
        prev_collision = False
    prev_collision = player_rect.colliderect(snail_rect)

    # losing :((
    if hearts <= 0 and not game_over_displayed:
        losing()  # game end
        
        
    # winning :)))
    if victory_achive:
        winning()
        

    
    
    pygame.display.flip()#no display.update=no screen=nothing=sad gamer=no one plays 🙁 

pygame.quit()#gamer needs to take a sleep break