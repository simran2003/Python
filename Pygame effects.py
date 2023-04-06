
import pygame
#Loading image on my drawing window
src_img = pygame.image.load(input("please type your file name"))
(x,y) = src_img.get_size()
drawing_window = pygame.display.set_mode((x,y))
drawing_window.blit(src_img, (0, 0))
pygame.display.update()

while True:    
#  to get positions of clicks
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (a1, b1)= pygame.mouse.get_pos()


        elif event.type == pygame.MOUSEBUTTONUP:
            (a2, b2) = pygame.mouse.get_pos()
# to  inverse the r,g,b values
            for i in range(a1, a2 +1):
                for j in range(b1, b2+1):

                    (r, g, b, _) = src_img.get_at((i, j))
                    drawing_window.set_at((i, j), (255-r, 255-g, 255-b))
                 
            pygame.display.update()

        else:
            pass
        pygame.display.update()
    

# exit the pygame window 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
