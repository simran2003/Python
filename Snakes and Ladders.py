
import pygame #importing libraries 
import random 
row=7            #number of rows and colmuns
colmun=6
red = (255,0,0)           #these are the colours of the board
white = (255,255,255)
blue=(0,0,255)        #my first player is blue 
green=(28,198,57)     #my second player is green
pygame.init()         #for printing numbers on the checkerboard
square_dim = 60       #every square in my checkerboard is 60 by 60
pygame.display.set_caption('DICE GAME')    #just the caption of the window
board_display= pygame.display.set_mode((420,360)) # 7*60=420 and 6*60=360 
board_display.fill((127, 127, 127))   #background colour 
block=1  #this counter is used further in numbering the checkerboard

current_colour = red #this variable is used to toggle the colors of checkerboard b/w red and white

for i in range(0, row+1): 
	for j in range(0, colmun+1):
		#this is to toggle the colours of the checkerboard , its like a switch colour function  
		if current_colour == red:
			current_colour = white
		else:
			current_colour = red
		pygame.draw.rect(board_display, current_colour , (i * square_dim, j * square_dim, square_dim, square_dim))
#feautre 1
for x in range(0,row+1):   #this is for numbering the blocks, i have 42 squares
	for y in range (0,colmun+1):
		font = pygame.font.SysFont('Calibri',30)
		text = font.render(str(block),True,(0,0,0))
		board_display.blit(text,((y*square_dim)+8,(x*square_dim)+9))
		block=block+1
		pygame.display.update()
new_board=board_display.copy()  #this is to clear the board evrytime a player moves
px1=30   #these are the x and y positions of the centres of the circles
px2=30   #my circles represent the players
py1=30   #initially the players are in the centre of the first square which is where they start from
py2=30   #the centre of the square is square dimension/2 so 30,30
pygame.draw.circle(board_display,blue,(px1,py1),10)   #drawing the initial position of 
pygame.draw.circle(board_display,green,(px2,py2),10)  #both the players
pygame.display.update()
pygame.event.pump()            
pygame.time.delay(10000)

#this is the main game loop
while True:
	dice_1 = random.randint(1,6) #the first dice
	dice_2 = random.randint(1,6) #the second dice
	total_dice=dice_1+dice_2     #the total is the number of blocks player moves
	print('the dice rolled is',total_dice,".",'Player one moves',total_dice,"blocks")
	px1+=total_dice*60  #this updates the position of the player ie the player moves 
	                    #total dice from the most recent postion 
	if px1>420:       #420 is the lenght of my one row, if the x axis of my player goes beyond 420
		px1= px1-420  #ie the player moves beyon block 7 into the next row then its x should change acordingly
		py1= py1+60   #so i subtracted the lenght of the entire row from the players initial position
		              # so that the player moves to the next row
		board_display.blit(new_board,(0,0))   #and y axis of the centre just goes down by one block so by 60
		pygame.draw.circle(board_display,blue,(px1,py1),10)
		pygame.draw.circle(board_display,green,(px2,py2),10)
		pygame.display.update()
		pygame.event.pump()
		pygame.time.delay(10000)

	else:
		pygame.draw.circle(board_display,blue,(px1,py1),10) #if it is not supposed to move to the 
		pygame.display.update()                             #next row then it just moves new x1 in the same row
		board_display.blit(new_board,(0,0))
		pygame.draw.circle(board_display,blue,(px1,py1),10) 
		pygame.draw.circle(board_display,green,(px2,py2),10)
		pygame.display.update()
		pygame.event.pump()
		pygame.time.delay(10000)
	#this is for the second player to move
	dice1=random.randint(1,6)
	dice2=random.randint(1,6)
	dice_final=dice1+dice2
	print('the dice rolled is',dice_final,".",'Player two moves',dice_final,"blocks")
	px2+=dice_final*60

	if px2>420:
		px2=px2-420
		py2=py2+60
		board_display.blit(new_board,(0,0))
		pygame.draw.circle(board_display,green,(px2,py2),10)
		pygame.draw.circle(board_display,blue,(px1,py1),10)
		pygame.display.update()
		pygame.event.pump()
		pygame.time.delay(10000)
	
	else:
		pygame.draw.circle(board_display,green,(px2,py2),10)
		pygame.display.update()
		board_display.blit(new_board,(0,0))
		pygame.draw.circle(board_display,blue,(px1,py1),10)
		pygame.draw.circle(board_display,green,(px2,py2),10)
		pygame.display.update()
		pygame.event.pump()
		pygame.time.delay(10000)
	
# just incase the players move outside the board the game ends
#players can't move past the end of the board
# feature 2 
	if (px1>180 or py1>210) or (px2>180 or py2>210):
		break
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()	
#honestly i dont know what pygame.event.pump is but a TA fixed something for me
#he gave me this line of code

        
		
		
	
