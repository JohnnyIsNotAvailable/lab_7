import pygame
import os
import time 

_image_library = {}

def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image


def blit_rotate(surf, image, position, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(
        topleft = (position[0] - originPos[0], position[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(position) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (position[0] - rotated_offset.x,
                            position[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)



pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
clock = pygame.time.Clock()
main_clock = pygame.image.load("main_clock.png")


left_hand = pygame.image.load('left_hand.png')
right_hand = pygame.image.load('right_hand.png')

left_wigth, left_high = left_hand.get_size()
right_wigth, right_high = right_hand.get_size()

left_hand_angle = 90
right_hand_angle = 90


while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        screen.blit(main_clock, (-15, -15))

        position = (screen.get_width()/2, screen.get_height()/2)

        blit_rotate(screen, left_hand, position, (left_wigth/2, left_high/2), left_hand_angle)
        blit_rotate(screen, right_hand, position, (right_wigth/2, right_high/2), right_hand_angle)

        left_hand_angle -= 0.085
        right_hand_angle -= 0.0014166

        pygame.display.flip()
        clock.tick(90)

pygame.quit()
exit()