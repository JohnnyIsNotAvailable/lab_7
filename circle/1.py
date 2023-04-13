import pygame

window = pygame.display.set_mode((1100, 700))
x = 550
y = 350
class Constants:
    radius = 10
    velocity = 30
    
clock = pygame.time.Clock()

done = True
while done:
    window.fill((255, 255, 255))
    
    clock.tick(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False 
       
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and x - Constants.velocity > 0: 
        x -= Constants.velocity
    if keys_pressed[pygame.K_RIGHT] and x - Constants.velocity < 1040: 
        x += Constants.velocity
    if keys_pressed[pygame.K_UP] and y - Constants.velocity > 0: 
        y -= Constants.velocity
    if keys_pressed[pygame.K_DOWN] and y - Constants.velocity < 650:
        y += Constants.velocity
    Object = pygame.draw.circle(window, (255, 0, 0), (x ,y), Constants.radius) 

    pygame.display.update()    
pygame.quit()