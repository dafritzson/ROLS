import sys
from time import sleep
import pygame
import game_functions as gf
from display_box import DummyBox, DisplayBox
import audio_mixer as am
from timer import Timer




'''All Event functions will be handled in this file'''
def event_loop(groups, program_data, screen, player, menu, interaction_obstacle, audio_mixer):
	'''check for all event types'''
	event_list = pygame.event.get()
	for event in event_list:
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown(groups, event, program_data, screen, player, menu, interaction_obstacle, audio_mixer)
		elif event.type == pygame.KEYUP:
			keyup(event, program_data, player)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			mouse_click(program_data, screen, player, menu, mouse_x, mouse_y, audio_mixer)


def keydown(groups, event, program_data, screen, player, menu, interaction_obstacle, audio_mixer):
	'''check for all keydowns'''
	#If the player is alrady moving, reject the new movement direction and add that event back to the queue to process later
	if program_data.game_paused == False:
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
			program_data.arrow_value -= 1
			print(program_data.arrow_value)
			#dialog_box.up_press = True
			#dialog_box.down_press = False
		elif event.key == pygame.K_DOWN:
			program_data.arrow_value += 1
			print(program_data.arrow_value)
			#dialog_box.down_press = True
			#dialog_box.up_press = False


	#All other intraction key presses
	#Events with Action button
	if event.key == pygame.K_a: 
		if program_data.game_state == "run" and player.ready_for_interaction and program_data.game_paused == False:
			dialog_box = DisplayBox(program_data, screen, audio_mixer)
			groups.get('display_boxes').add(dialog_box)
			#Transfer necessary program_data to build the display box based on the interaction obstacle.
			dialog_box.message_key = interaction_obstacle.interaction_message
			dialog_box.message_type = interaction_obstacle.message_type
			dialog_box.response_options = interaction_obstacle.response_options
			dialog_box.response_messages = interaction_obstacle.response_messages
			dialog_box.visible = True
			program_data.game_paused = True
			dialog_box.prep_message()

			if interaction_obstacle.pickupable:
				audio_mixer.audio_key = 'sound_report'
				audio_mixer.load_sound()
				audio_mixer.play_sound()
				groups.get('map_entities').remove(interaction_obstacle)
				groups.get('collisions').remove(interaction_obstacle)
				groups.get('items').remove(interaction_obstacle)
				player.report_count += 1

			if interaction_obstacle.is_NPC:
				interaction_obstacle.face_player(player.direction)
				if interaction_obstacle.is_battler:
					audio_mixer.audio_key = 'battle_message'

			if interaction_obstacle.player_modifier:
				interaction_obstacle.modify_player(player)
				groups.get('timers').empty()
				mod_timer = Timer(program_data, interaction_obstacle, interaction_obstacle.player_modifier_duration)
				groups.get('timers').add(mod_timer)
	
		#Handle actions through a screen box (game is paused)
		elif program_data.game_paused == True and program_data.game_state == "run":
			if dialog_box.noise_on:
				audio_mixer.play_sound()
			if dialog_box.main_message_done == False:
				if dialog_box.typing == True:
					#don't switch or clear lines while typing
					pass
				else:
					if dialog_box.clear_on_click == True:
						dialog_box.clear_lines()
					else:
						dialog_box.switch_lines()
			elif dialog_box.main_message_done == True and dialog_box.message_sequence_done == False:
				dialog_box.run_responsive_message()
			#Close the displaybox
			else:
				dialog_box.clear_lines()
				dialog_box.visible = False
				groups.get('display_box').remove(dialog_box)
				program_data.game_paused = False




	if event.key == pygame.K_SPACE and program_data.game_state == "run":
		program_data.game_state = "game menu"
		pygame.mouse.set_visible(True)

	if event.key == pygame.K_BACKSPACE and program_data.game_state == "run":
		print("You have: " + str(player.report_count) + " files")

	if event.key == pygame.K_9:
		print(program_data.game_state)

def keyup(event, program_data, player):
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


def mouse_click(program_data, screen, player, menu, mouse_x, mouse_y, audio_mixer):
	if program_data.game_state == "main menu":
		button_clicked = menu.newgame_rect.collidepoint(mouse_x, mouse_y)
		if button_clicked:
			program_data.game_state = "run"
			audio_mixer.audio_key = 'main_theme'
			audio_mixer.play_music()
			#hide the mouse
			pygame.mouse.set_visible(False)
	if program_data.game_state == "game menu":
		button_clicked = menu.continuegame_rect.collidepoint(mouse_x, mouse_y)
		if button_clicked:
			program_data.game_state = "run"
			audio_mixer.audio_key = 'main_theme'
			audio_mixer.play_music()
			#hide the mouse
			pygame.mouse.set_visible(False)





