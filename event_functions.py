import sys
from time import sleep
import pygame
import game_functions as gf

pygame.mixer.init()
item_sound = pygame.mixer.music.load('.\\Audio\\Item.wav')
'''All Event functions will be handled in this file'''
def event_loop(settings, screen, player, menu, display_box, obstacles, collisions,interaction_obstacle):
	'''check for all event types'''
	event_list = pygame.event.get()
	for event in event_list:
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown(event, settings, screen, player, menu, display_box, obstacles, collisions, interaction_obstacle)
		elif event.type == pygame.KEYUP:
			keyup(event, settings, player)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			mouse_click(settings, screen, player, menu, mouse_x, mouse_y)


def keydown(event, settings, screen, player, menu, display_box, obstacles, collisions, interaction_obstacle):
	'''check for all keydowns'''
	#If the player is alrady moving, reject the new movement direction and add that event back to the queue to process later
	if player.move_in_progress == True or player.finishing_animation == True:
		if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
			pygame.event.post(event)

	#If player is not moving process the movement direction
	if player.move_in_progress == False and player.finishing_animation == False:
		if event.key == pygame.K_RIGHT:
			player.moving_right = player.move_in_progress = True
		elif event.key == pygame.K_LEFT:
			player.moving_left = player.move_in_progress  = True
		elif event.key == pygame.K_UP:
			player.moving_up = player.move_in_progress = True
		elif event.key == pygame.K_DOWN:
			player.moving_down = player.move_in_progress = True
	
	#Process non-movement keydowns
	if event.key == pygame.K_SPACE and settings.game_state == "run":
		settings.game_state = "game menu"
		pygame.mouse.set_visible(True)

	#All other intraction key presses
	if event.key == pygame.K_a and settings.game_state == "run" and player.ready_for_interaction:
		display_box.prep_message()
		if player.can_pickup:
			pygame.mixer.music.play()
			obstacles.remove(interaction_obstacle)
			collisions.remove(interaction_obstacle)
			player.report_count += 1

	if event.key == pygame.K_BACKSPACE and settings.game_state == "run":
		print("You have: " + str(player.report_count) + " files")

	if event.key == pygame.K_9:
		print(settings.game_state)

def keyup(event, settings, player):
	'''check for all keyups'''
	if event.key == pygame.K_RIGHT and player.moving_right:
		player.moving_right = player.move_in_progress = False
		player.finishing_animation = True
	elif event.key == pygame.K_LEFT and player.moving_left:
		player.moving_left =  player.move_in_progress = False
		player.finishing_animation = True
	elif event.key == pygame.K_UP and player.moving_up:
		player.moving_up = player.move_in_progress = False
		player.finishing_animation = True
	elif event.key == pygame.K_DOWN and player.moving_down:
		player.moving_down =  player.move_in_progress = False
		player.finishing_animation = True
	else:
		pygame.event.clear()


def mouse_click(settings, screen, player, menu, mouse_x, mouse_y):
	if settings.game_state == "main menu":
		button_clicked = menu.newgame_rect.collidepoint(mouse_x, mouse_y)
		if button_clicked:
			settings.game_state = "run"
			#hide the mouse
			pygame.mouse.set_visible(False)
	if settings.game_state == "game menu":
		button_clicked = menu.continuegame_rect.collidepoint(mouse_x, mouse_y)
		if button_clicked:
			settings.game_state = "run"
			#hide the mouse
			pygame.mouse.set_visible(False)


	#if settings.game_state == "main menu":
		#button_clicked = menu.continuegame_rect.collidepoint(mouse_x, mouse_y)
		#if button_clicked:
			#print("Start a new game")




