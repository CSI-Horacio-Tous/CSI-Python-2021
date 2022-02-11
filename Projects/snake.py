
import pygame
pygame.init() # inicia todos los médules de PuBame

yellow = (255, 255, 102) #Score
black = (0, 0, 0) #pantalla
red = (213, 50, 80) #game over
green = (0, 255, 0) #food
blue = (50, 153, 213) #snake

dis=pygame.display.set_mode((400,300))
pygame.display.set_caption("Snake game by HT") # ARaneserá el nombre del jusse
game_over=False

x1 = 150
y1 = 150

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type== pygame.QUIT: #cierra la pantalla al pinchar la (x))
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x1_change = -10
                y1_change = 0
            elif  event.key == pygame.K_d:
                x1_change = 10
                y1_change = 0
            elif  event.key == pygame.K_w:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_s:
                x1_change = 0
                y1_change = 10
    x1 += x1_change
    y1 += y1_change
        
    dis.fill(black)
    pygame.draw.rect(dis, blue, [x1 ,y1 ,10 ,10])#draw snake
    pygame.display.update() #actualiza los cambios que ocurtan en la pantalla       

    clock.tick(15) #velocidad
pygame.quit() #termina todo
quit()