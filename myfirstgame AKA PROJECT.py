#myfirstgame AKA PROJECT
import pygame

pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('smoooothhh Runner')
#changing the screen display name
clock = pygame.time.Clock()
#creating clock time
test_font = pygame.font.Font('font.ttf',60)
#(font type,font size)
sky_surface = pygame.image.load('skyy.png')
#here the 800 and 400 before where we set was our height and width the pygames is just like graph but the point of origin at the start but here its at the left top the starting of the window to increse in right we have to add in x coordinator and to increase downwards its sopposed to be  decreased y co ordinator
ground_surface = pygame.image.load('ground.png').convert()
ground_surface2 = pygame.image.load('ground.png').convert()
#.covert function makes our image something that py games can easily work with but the .convert after the closing brakets make it an error
text_surface = test_font.render(' game',False,'grey')
#(text,AA(anti alising),color)

enemy_surface = pygame.image.load('snail.png').convert_alpha()
enemy_x_pos = 900

player_surf = pygame.image.load('player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(center = (80,300))
while True:
    for event in pygame.event.get():
        #creating a option to close the winndow
        if event.type == pygame.QUIT:
            #quit is a inbuilt function the one written in caps
            pygame.quit()
            exit()
           #works
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,425))
    screen.blit(ground_surface2,(500,425))
    screen.blit(text_surface,(420,80))
    enemy_x_pos -= 8
    # moving the enemy position by -= in the while loop
    if enemy_x_pos < -100: 
        enemy_x_pos = 990
        #used if statement to make the snail reappearing
    
    screen.blit(enemy_surface,(enemy_x_pos,395))
    screen.blit(player_surf,(80,345))
    #cuuzz py games follow an order 

    #when its set at 0,0 it mean from start point
    #here we are 
    # asking the window to surface and display our 400 and 800 at the 0,0 value of place
    
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print('collosion')



    pygame.display.update()
    clock.tick(60)
    

    pygame.quit(160)

 