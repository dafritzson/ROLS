import sys
from time import sleep
import pygame
import game_functions as gf
from timer import Timer


pygame.mixer.init()
item_sound = pygame.mixer.music.load('.\\Audio\\Item.wav')
'''All Event functions will be handled in this file'''
def event_loop(settings, screen, player, menu, display_box, obstacles, map_entities, collisions, interaction_obstacle, timers):
	'''check for all event types'''
	event_list = pygame.event.get()
	for event in event_list:
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown(event, settings, screen, player, menu, display_box, obstacles, map_entities, collisions, interaction_obstacle, timers)
		elif event.type == pygame.KEYUP:
			keyup(event, settings, player)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			mouse_click(settings, screen, player, menu, mouse_x, mouse_y)


def keydown(event, settings, screen, player, menu, display_box, obstacles, map_entities, collisions, interaction_obstacle, timers):
	'''check for all keydowns'''
	#If the player is alrady moving, reject the new movement direction and add that event back to the queue to process later
	if settings.game_paused == False:
		if player.move_in_progress == True or player.finishing_animation == True:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				pygame.event.post(event)

		#If player is not moving process the movement direction
		if player.move_in_progress == False and player.finishing_animation == False:
			if event.key == pygame.K_RIGHT:
				player.moving_right = player.move_in_progress = True
				player.direction = "right"
			elif event.key == pygame.K_LEFT:
				player.moving_left = player.move_in_progress  = True
				player.direction = "left"
			elif event.key == pygame.K_UP:
				player.moving_up = player.move_in_progress = True
				player.direction = "up"
			elif event.key == pygame.K_DOWN:
				player.moving_down = player.move_in_progress = True
				player.direction = "down"
	else:
		if event.key == pygame.K_UP:
			display_box.up_press = True
			display_box.down_press = False
		elif event.key == pygame.K_DOWN:
			display_box.down_press = True
			display_box.up_press = False


	#All other intraction key presses
	#Events with Action button
	if event.key == pygame.K_a: 
		if settings.game_paused == True and settings.game_state == "run":
			if display_box.main_message_done == False:
				if display_box.typing == True:
					#don't switch or clear lines while typing
					pass
				else:
					if display_box.clear_on_click == True:
						display_box.clear_lines()
					else:
						display_box.switch_lines()
			elif display_box.main_message_done == True and display_box.message_sequence_done == False:
				display_box.run_response()
			#Close the displaybox
			else:
				display_box.visible = False
				settings.game_paused = False

		elif settings.game_state == "run" and player.ready_for_interaction:
			#Transfer necessary settings to build the display box based on the interaction obstacle.
			display_box.message_key = interaction_obstacle.interaction_message
			display_box.message_type = interaction_obstacle.message_type
			display_box.response_options = interaction_obstacle.response_options
			display_box.response_messages = interaction_obstacle.response_messages
			display_box.visible = True
			display_box.hold_blit = False
			settings.game_paused = True
			display_box.prep_message()

			if interaction_obstacle.pickupable:
				pygame.mixer.music.play()
				obstacles.remove(interaction_obstacle)
				map_entities.remove(interaction_obstacle)
				collisions.remove(interaction_obstacle)
				player.report_count += 1

			if interaction_obstacle.is_NPC:
				interaction_obstacle.face_player(player.direction)

			if interaction_obstacle.player_modifier:
				interaction_obstacle.modify_player(player)
				timers.empty()
				mod_timer = Timer(settings, interaction_obstacle, interaction_obstacle.player_modifier_duration)
				timers.add(mod_timer)


	if event.key == pygame.K_SPACE and settings.game_state == "run":
		settings.game_state = "game menu"
		pygame.mouse.set_visible(True)

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




