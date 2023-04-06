
#imported random to get the image 
#random module to find a random integer b/w given intervals
#sys for the command line argument 
import pygame
import random
import sys
i = sys.argv[1]
#this is to load the image and i think get the size
src_img = pygame.image.load(i)
(wid, hgt) = src_img.get_size()
#my scaling factor is 5 and this increases the screen size by scaling factor 
win_sfc = pygame.display.set_mode((5*wid,5*hgt))
#x and y are the width and height of the image 
#nested loops are to find each pixel and to get the color 
for y in range(hgt):
    for x in range (wid):
        (r, g, b, _) = src_img.get_at((x, y))        
#will Get the red, green, and blue of the Colour at Pixel x, y
        red = r//50
        green= g//50
        blue= b//50
        a = x*5
        b = y*5

        for i in range (red) :
            #formula to find the number of circles to be drawn
            pixelx = random.randint((a),(a+3))
            pixely = random.randint((b),(b+3))
            #pixel x and pixel y are the coordinates of the centre of the circles 
            pygame.draw.circle(win_sfc,(255,0,0),(pixelx,pixely),1)
        for i in range (green):
            pixelx = random.randint((a),(a+3))
            pixely = random.randint((b),(b+3))
            pygame.draw.circle(win_sfc,(255,0,0),(pixelx,pixely),1)
        for i in range (blue) :
            pixelx = random.randint((a),(a+3))
            pixely = random.randint((b),(b+3))
            pygame.draw.circle(win_sfc,(0,0,255),(pixelx, pixely),1)

pygame.display.update()#to update the image on the pygame window
while True:#this is an event controlled loop to show the output, it was taught in the class
    #so i'm not using time.delay hope ur okay with it !
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()	

