import pygame
import datetime
import os

pygame.init()

center = (400, 400)
clock_radius = 400

white_color=(255, 255, 255)
black_color=(0, 0, 0)
red_color=(255, 0, 0)

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("CLOCK")
clock = pygame.time.Clock()


mickey_clock = pygame.image.load(os.path.join('main_clock.png'))
mickey_clock = pygame.transform.scale(mickey_clock, (800,800))

mickey_min = pygame.image.load(os.path.join('right_hand.png'))
mickey_min = pygame.transform.scale(mickey_min,(400, 80))
mickey_min_rect = mickey_min.get_rect()
mickey_min_rect.center = (400, 400)

mickey_sec = pygame.image.load(os.path.join('left_hand.png'))
mickey_sec = pygame.transform.scale(mickey_sec,(500, 70))
mickey_sec_rect=mickey_sec.get_rect()
mickey_sec_rect.center=(400, 400)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                
    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute
    hour = current_time.hour
                
    screen.fill(black_color)
    pygame.draw.circle(screen, white_color, center, clock_radius - 10, 10)
    pygame.draw.circle(screen, white_color, center, 12)
        
    screen.blit(mickey_clock, (0, 0))
        

    mickey_min_move = pygame.transform.rotate(mickey_min,( -1 * (6 * minute) + 80))
    mickey_min_rect_move = mickey_min_move.get_rect()
    mickey_min_rect_move.center = mickey_min_rect.center
    screen.blit(mickey_min_move, mickey_min_rect_move)
        
    mickey_sec_move = pygame.transform.rotate(mickey_sec,(-1 * (6 * second) + 160))
    mickey_sec_rect_move = mickey_sec_move.get_rect()
    mickey_sec_rect_move.center = mickey_sec_rect.center
    screen.blit(mickey_sec_move, mickey_sec_rect_move)
        
    pygame.display.update()
    clock.tick(90)

pygame.quit()