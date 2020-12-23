import sys
from time import sleep
import pygame
from program_variables import program_data as pd, settings
import game_functions as gf
from display_box import DummyBox, DisplayBox
from timer import Timer


'''All Event functions will be handled in this file'''
def event_loop(player, menu):
	'''check for all event types'''
	event_list = pygame.event.get()
	for event in event_list:
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown(event, player, menu)
		elif event.type == pygame.KEYUP:
			keyup(event, player)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			mouse_click(player, menu, mouse_x, mouse_y)


def keydown(event, player, menu):
	'''check for all keydowns'''
	#If the player is alrady moving, reject the new movement direction and add that event back to the queue to process later
	interaction_obstacle = pd.interaction_obstacle
	audio_mixer = pd.audio_mixer

	if pd.game_paused == False:
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
		for display_box in pd.display_boxes:
			if display_box.is_active:
				if event.key == pygame.K_UP:
					display_box.arrow_value_y -= 1
					
				elif event.key == pygame.K_DOWN:
					display_box.arrow_value_y += 1
	

	#All other intraction key presses
	#Events with Action button
	if event.key == pygame.K_a: 
		#First 'a' press before game is paused
		if pd.game_state == "run" and player.ready_for_interaction and pd.game_paused == False:
			dialog_box = DisplayBox()
			pd.display_boxes.add(dialog_box)
			#Transfer necessary pd to build the display box based on the interaction obstacle.
			dialog_box.message_key = interaction_obstacle.interaction_message
			dialog_box.message_type = interaction_obstacle.message_type
			dialog_box.response_options = interaction_obstacle.response_options
			dialog_box.response_messages = interaction_obstacle.response_messages
			dialog_box.is_visible = True
			pd.game_paused = True
			dialog_box.prep_message()

			if interaction_obstacle.pickupable:
				audio_mixer.audio_key = 'sound_report'
				audio_mixer.load_sound()
				audio_mixer.play_sound()
				pd.map_entities.remove(interaction_obstacle)
				pd.collisions.remove(interaction_obstacle)
				pd.items.remove(interaction_obstacle)
				player.report_count += 1

			if interaction_obstacle.is_NPC:
				interaction_obstacle.face_player(player.direction)
				if interaction_obstacle.is_battler:
					audio_mixer.audio_key = 'battle_message'

			if interaction_obstacle.player_modifier:
				interaction_obstacle.modify_player(player)
				pd.timers.empty()
				mod_timer = Timer(interaction_obstacle, interaction_obstacle.player_modifier_duration)
				pd.timers.add(mod_timer)
	
		#Handle all 'a' presses when game is paused
		if pd.game_paused == True and pd.game_state == "run":
			for display_box in pd.display_boxes:
				if display_box.noise_on:
					audio_mixer.play_sound()
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
					display_box.run_responsive_message()
				#Close the displaybox
				else:
					display_box.clear_lines()
					display_box.is_visible = False
					pd.display_boxes.remove(display_box)
					pd.game_paused = False


	if event.key == pygame.K_SPACE and pd.game_state == "run":
		pd.game_state = "game menu"
		pygame.mouse.set_visible(True)

	if event.key == pygame.K_BACKSPACE and pd.game_state == "run":
		print("You have: " + str(player.report_count) + " files")

	if event.key == pygame.K_9:
		print(pd.game_state)

def keyup(event, player):
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


def mouse_click(player, menu, mouse_x, mouse_y):
	audio_mixer = pd.audio_mixer

	if pd.game_state == "main menu":
		button_clicked = menu.newgame_rect.collidepoint(mouse_x, mouse_y)
		if button_clicked:
			pd.game_state = "run"
			audio_mixer.audio_key = 'main_theme'
			audio_mixer.play_music()
			#hide the mouse
			pygame.mouse.set_visible(False)
	if pd.game_state == "game menu":
		button_clicked = menu.continuegame_rect.collidepoint(mouse_x, mouse_y)
		if button_clicked:
			pd.game_state = "run"
			audio_mixer.audio_key = 'main_theme'
			audio_mixer.play_music()
			#hide the mouse
			pygame.mouse.set_visible(False)





