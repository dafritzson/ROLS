import sys
from time import sleep
import pygame
import game_functions as gf


'''All Event functions will be handled in this file'''
def event_loop(screen, settings, player, menu):
	'''check for all event types'''
	event_list = pygame.event.get()
	for event in event_list:
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown(event, screen, settings, player, menu)
		elif event.type == pygame.KEYUP:
			keyup(event, settings, player)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			mouse_click(screen, settings, player, menu, mouse_x, mouse_y)


def keydown(event, screen, settings, player, menu):
	'''check for all keydowns'''
	#If the player is alrady moving, reject the new movement direction and add that event back to the queue to process later
	if player.move_in_progress == True:
		pygame.event.post(event)
	#If player is not moving process the movement direction
	elif player.move_in_progress == False:
		if event.key == pygame.K_RIGHT:
			player.moving_right = player.move_animating = player.move_in_progress = True
			player.image = player.image_right
		elif event.key == pygame.K_LEFT:
			player.moving_left = player.move_animating = player.move_in_progress = True
			player.image = player.image_left
		elif event.key == pygame.K_UP:
			player.moving_up = player.move_animating = player.move_in_progress = True
		elif event.key == pygame.K_DOWN:
			player.moving_down = player.move_animating = player.move_in_progress = True
	#Process non-m0vement keydowns
	if event.key == pygame.K_SPACE and settings.game_state == "run":
		settings.game_state = "game menu"
		pygame.mouse.set_visible(True)

	if event.key == pygame.K_BACKSPACE and settings.game_state == "run":
		print("talk")

	if event.key == pygame.K_9:
		print(settings.game_state)

def keyup(event, settings, player):
	'''check for all keyups'''
	if event.key == pygame.K_RIGHT:
		player.moving_right = player.move_in_progress = False
	elif event.key == pygame.K_LEFT:
		player.moving_left = player.move_in_progress = False
	elif event.key == pygame.K_UP:
		player.moving_up = player.move_in_progress = False
	elif event.key == pygame.K_DOWN:
		player.moving_down = player.move_in_progress = False

def mouse_click(screen, settings, player, menu, mouse_x, mouse_y):
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




