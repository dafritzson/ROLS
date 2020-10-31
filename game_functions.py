import math
import pygame
import math
import images
from pygame.sprite import collide_rect
from menu import Menu
from display_box import DisplayBox
from obstacle import Desk, Wall, CoffeeMachine
from NPC import NPC
from map_entity import Carpet


def update_display():
	# make the most recently drawn screen visible			
	pygame.display.update()	

def run_menu(program_data, screen, player, menu):
	'''run the main menu state'''
	menu.blitme()


def draw_display(groups, program_data, screen, player, level_map):
	'''
	#try to save memory by not drawing off screen entities
	for entity in map_entities:
		if on_screen_entities.has(entity):
			if entity.rect.right < screen.rect.left or entity.rect.left > screen.rect.right or entity.rect.bottom < screen.rect.top or entity.rect.top > screen.rect.bottom:
				on_screen_entities.remove(entity)
		else:
			on_screen_entities.add(entity)
	'''		
	screen.fill()
	
	level_map.blit_overlay()


	for entity in groups.get('map_entities'):
		entity.blitme()

	#Draw NPC on top of player if it is below it
	player.blitme()
	for npc in groups.get('npcs'):
		if npc.y > player.y:
			npc.blitme()

	for display_box in groups.get('display_boxes'):
		if display_box.visible == True:
			display_box.update()

def draw_battle_display(groups, program_data, screen, player, battle_arena):
	screen.fill_battle()


def update_game(groups, program_data, player):
	#Update obstacles and timers
	player.ready_for_interaction = False
	interaction_obstacle = None
	player_collision = player.get_collision_rect()

	#Update all display dialog boxes
	#for display_box in groups.get('display_boxes'):
	#	display_box.update()

	#Update game timers
	current_time = pygame.time.get_ticks()
	for timer in groups.get('timers'):
		elapsed_time = timer.get_elapsed_time(current_time)
		if elapsed_time > timer.target_time:
			timer.requester.revert_player(player)
			timers.remove(timer)
		if program_data.game_paused:
			timer.paused = True
		else:
			timer.paused = False

	#Update game obstacles
	for obstacle in groups.get('collisions'):
		#Updating the obstacle will move if it is a dynamic obstacle
		obstacle.update()

		#Functionality for obstacles that can interact with the player
		if obstacle.interactable == True:
			if player_collision.rect.colliderect(obstacle.rect):
				if (obstacle.side_interactable and player.direction == obstacle.interaction_side) or not obstacle.side_interactable:
						player.ready_for_interaction = True
						interaction_obstacle = obstacle
				break
	return interaction_obstacle
	

def update_player(groups, program_data, screen, player, golden_map_tile, level_map):
	if not program_data.game_paused:	
		if player.finishing_animation:
			player.finish_animation()

		player.check_collisions()
		if player.colliding:
			#Round player/map when colliding and make sure all elements are alligned
			player.finishing_animation = True
			player.finish_animation()
			
			#Set the player direction
			if player.move_in_progress:
				if player.moving_right:
					player.face_right()
				elif player.moving_left:
					player.face_left()
				elif player.moving_up:
					player.face_up()
				elif player.moving_down:
					player.face_down()
			player.finishing_animation = False
			player.colliding = False
		
		else:	
			#standard player movement to respond to player movement flags set in the event loop
			if player.move_in_progress:
				if player.colliding == False:
					if player.moving_right and player.rect.right < screen.rect.right:
						if player.x >= screen.rect.right - program_data.tile_size*6:
							player.animate_right()
							player.move_map_right()
							player.map_moving = True
						else:
							player.move_right()
							player.map_moving = False
					elif player.moving_left and player.rect.left > screen.rect.left:
						if player.x <= screen.rect.left + program_data.tile_size*6:
							player.animate_left()
							player.move_map_left()
							player.map_moving = True
						else:
							player.move_left()
							player.map_moving = False
					elif player.moving_up and player.rect.top > screen.rect.top:
						if player.y <= screen.rect.top + program_data.tile_size*6:
							player.animate_up()
							player.move_map_up()
							player.map_moving = True
						else:
							player.move_up()
							player.map_moving = False
		
					elif player.moving_down and player.rect.bottom < screen.rect.bottom:
						if player.y >= screen.rect.bottom - program_data.tile_size*6:
							player.animate_down()
							player.move_map_down()
							player.map_moving = True
						else:
							player.move_down()
							player.map_moving = False			

def generate_obstacles(groups, program_data, screen, level_map):
	new_desk = Desk(program_data.tile_size*16, program_data.tile_size*8, program_data, screen, level_map)
	groups.get('collisions').add(new_desk)
	#collisions.add(new_desk)
	groups.get('map_entities').add(new_desk)
	coffee_machine = CoffeeMachine(program_data.tile_size*17, program_data.tile_size*29, program_data, screen, level_map)
	groups.get('collisions').add(coffee_machine)
	#collisions.add(coffee_machine)
	groups.get('map_entities').add(coffee_machine)


def build_map(groups, program_data, screen, level_map):
	#For the given map recognize obstacles within the map image and add a obstacle object at its x and y location
	for y in range(0, level_map.rect.height, program_data.tile_size):
		for x in range(0, level_map.rect.width, program_data.tile_size):
			tile_key = level_map.image.get_at((x, y))

			for tile in images.obstacle_tiles:
				if  tile == tile_key:
					wall = Wall(x, y, program_data, screen, level_map)
					groups.get('collisions').add(wall)
					groups.get('map_entities').add(wall)

def set_map_position(groups, program_data, screen, level_map):
	level_map.rect_overlay.x = level_map.rect_overlay.x + program_data.tile_size*-12
	level_map.rect_overlay.y =  level_map.rect_overlay.y + program_data.tile_size*-33

	for ent in groups.get('map_entities'):
		ent.x = ent.x + program_data.tile_size*-12
		ent.y = ent.y + program_data.tile_size*-33



