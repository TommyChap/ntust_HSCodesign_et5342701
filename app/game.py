# 1 - Import library
import pygame
from pygame.locals import *
import time
import random
from ctypes import *

# 2 – Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False, False]
playerpos = [0, 0]
acc = [0, 0]
arrows = []
badmans = []
hp = 8
level = 0;
arrow_select = 0;
lib = CDLL("./libmygpio.so")
lib.init()

# Time status
time_last = (time.time())
badman_make_time = time_last
time_change = False

# 3 – Load images
player = pygame.image.load("img/main_character.png")
bg = pygame.image.load("img/bg.png")
arrow = [pygame.image.load("img/bullet.png"), pygame.image.load("img/bullet2.png"), pygame.image.load("img/bullet3.png")]
goodman = pygame.image.load("img/goodman.png")
badman = [pygame.image.load("img/badman.png"), pygame.image.load("img/badman2.png"), pygame.image.load("img/badman3.png"), goodman]
gameover = pygame.image.load("img/gameover.png")

start_flag = 1
# 4 – Keep looping through
while start_flag:
    time_now = (time.time())
    if(time_last < time_now):
        time_last = time_now
        time_change = True
    else:
        time_change = False
    lib.Write((0xff >> (8 - hp)), 0)

    # 5 – Clear the screen before drawing it again
    screen.fill(0)

    # 6 – Draw the screen elements
    screen.blit(bg, (0, 0))
    screen.blit(player, playerpos)
    
    # 6-1 - Draw arrows
    index = 0
    for bullet in arrows:
        screen.blit(arrow[bullet[2]], bullet)
        if time_change:
            arrows[index][0] += 0.5
        if bullet[0] > 640:
            arrows.pop(index)
        index += 1
    
    # 6-2 - Draw badmans
    index = 0
    for monster in badmans:
        screen.blit(badman[monster[2]], monster)
        if time_change:
            badmans[index][0] -= 0.5 * monster[2]
        if monster[0] <= 0 :
            if monster[2] < 3:
				hp -= 1
            badmans.pop(index)
        index += 1
        
    # 6-2-1 - Make badman
    if(time_now - badman_make_time > 5):
      badman_make_time = time_now
      badmans.append([640, random.randint(0, 380), random.randint(0, level)])
    
    # 6-3 - Draw Score
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Score: "+str(acc[0]), True, (255, 255, 0),)
    textRect = text.get_rect()
    textRect.centerx = 50
    textRect.centery = 24
    screen.blit(text, textRect)
    
    # Kill to badman
    index_bullet = 0
    for bullet in arrows:
      index_monster = 0
      for monster in badmans:
          if (monster[0] - bullet[0]) > -3 and (monster[0] - bullet[0]) < 0 and (monster[1] - bullet[1]) > -100 and (monster[1] - bullet[1]) <= 0:
                if monster[2] == bullet[2]:
				    arrows.pop(index_bullet)
				    badmans.pop(index_monster)
				    if monster[2] < 3:
				        acc[0] += 1
				if monster[2] == 3:
					arrows.pop(index_bullet)
				    badmans.pop(index_monster)
				    acc[0] -= 10
          index_monster += 1
      index_bullet += 1
    
    # 7 – Update the screen
    pygame.display.flip()

    # 8 - loop through the events
    '''
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
            if event.key == K_z:
                acc[1] += 1
                arrows.append([playerpos[0] + 130, playerpos[1] + 86])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
    '''
    # 8 - Read Button
    button = lib.Read(1)
    keys[0] = button & 16    # up
    keys[1] = button & 4     # left
    keys[2] = button & 8     # down
    keys[3] = button & 2     # right
    keys[4] = button & 1     # fire
	
	# 8-1 - Select Level and arrow
	switch = lib.Read(0)
	level = switch & 3	# 2's LSB
	arrow_select = switch & 0xC0 # 2's MSB

    # 9 - Move Player
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5
    if keys[4]:
        acc[1] += 1
        arrows.append([playerpos[0] + 130, playerpos[1] + 86, arrow_select])
    
    if hp <= 0:
        start_flag = 0
        screen.fill(0)
        screen.blit(gameover, (0, 0))
        
while 1:
    pygame.display.flip()
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
