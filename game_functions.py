import math
import pygame
from pygame.sprite import collide_rect
from menu import Menu
from display_box import DisplayBox
import images
from obstacle import Desk, NPC
from map import Carpet, Wall


def update_display():
	# make the most recently drawn screen visible			
	pygame.display.update()	

def run_menu(settings, screen, player, menu):
	'''run the main menu state'''
	menu.blitme()

def update_screen(settings, screen, display_box, level_map):
	'''Redraw the screen during each pass through the loop to prep for next frame of game image'''
	screen.fill()

def update_game(settings, obstacles, player, collisions, display_box, timers):
	#Update obstacles and timers
	player.ready_for_interaction = False
	
	interaction_obstacle = None
	player_collision = player.get_collision_rect()

	current_time = pygame.time.get_ticks()
	for timer in timers:
		elapsed_time = timer.get_elapsed_time(current_time)
		if elapsed_time > timer.target_time:
			timer.requester.revert_player(player)
			timers.remove(timer)
		if settings.game_paused:
			timer.paused = True
		else:
			timer.paused = False
	
	for obstacle in obstacles:
		#Updating the obstacle will move it if it is a dynamic obstacle
		obstacle.update()

		#Functionality for obstacles that can interact with the player
		if obstacle.interactable == True:
			if player_collision.rect.colliderect(obstacle.rect):
				if (obstacle.side_interactable and player.direction == obstacle.interaction_side) or not obstacle.side_interactable:
						player.ready_for_interaction = True
						display_box.message_key = obstacle.interaction_message
						interaction_obstacle = obstacle
				break
	return interaction_obstacle
	
def update_player(settings, screen, player, display_box, tile_list):
	
	if player.finishing_animation:
		player.finish_animation(tile_list)
	else:	
		player.check_collisions()
		#standard player movement to respond to player movement flags set in the event loop
		# If keydown has happened so player should move
		if player.move_in_progress:
			# If player is not colliding with anything
			if player.colliding == False:
				# If right arrow is pressed and player is not about to run off the right side of screen
				if player.moving_right and player.rect.right < screen.rect.right:
					# If player is near edge of screen, move the map but not the player
					if player.rect.x > screen.rect.centerx + screen.rect.width / 3:
						player.animate_right()
						player.move_map_right()
						player.map_moving = True
					else:
						for tile in tile_list:
							if tile.tileY == player.current_tile.tileY and tile.tileX == player.current_tile.tileX + 1:
								print('current_tile: ({}, {})'.format(player.current_tile.tileX, player.current_tile.tileY))
								print('coordinates: ({}, {})'.format(player.current_tile.centerX, player.current_tile.centerY))
								print('target_tile: ({}, {})'.format(tile.tileX, tile.tileY))
								print('coordinates: ({}, {})'.format(tile.centerX, tile.centerY))
								player.move_right(tile)
								player.finishing_animation = True
						player.map_moving = False
				elif player.moving_left and player.rect.left > screen.rect.left:
					if player.rect.x < screen.rect.centerx - screen.rect.width / 3:
						player.animate_left()
						player.move_map_left()
						player.map_moving = True
					else:
						for tile in tile_list:
							if tile.tileY == player.current_tile.tileY and tile.tileX == player.current_tile.tileX - 1:
								print('current_tile: ({}, {})'.format(player.current_tile.tileX, player.current_tile.tileY))
								print('coordinates: ({}, {})'.format(player.current_tile.centerX, player.current_tile.centerY))
								print('target_tile: ({}, {})'.format(tile.tileX, tile.tileY))
								print('coordinates: ({}, {})'.format(tile.centerX, tile.centerY))
								player.move_left(tile)
								player.finishing_animation = True
						player.map_moving = False		
				elif player.moving_up and player.rect.top > screen.rect.top:
					if player.rect.y < screen.rect.height / 6:
						player.animate_up()
						player.move_map_up()
						player.map_moving = True
					else:
						for tile in tile_list:
							if tile.tileX == player.current_tile.tileX and tile.tileY == player.current_tile.tileY - 1:
								print('current_tile: ({}, {})'.format(player.current_tile.tileX, player.current_tile.tileY))
								print('coordinates: ({}, {})'.format(player.current_tile.centerX, player.current_tile.centerY))
								print('target_tile: ({}, {})'.format(tile.tileX, tile.tileY))
								print('coordinates: ({}, {})'.format(tile.centerX, tile.centerY))
								player.move_up(tile)
								player.finishing_animation = True
						player.map_moving = False		
				elif player.moving_down and player.rect.bottom < display_box.rect.top:
					if player.rect.y > screen.rect.centery + screen.rect.height / 8:
						player.animate_down()
						player.move_map_down()
						player.map_moving = True
					else:
						for tile in tile_list:
							if tile.tileX == player.current_tile.tileX and tile.tileY == player.current_tile.tileY + 1:
								print('current_tile: ({}, {})'.format(player.current_tile.tileX, player.current_tile.tileY))
								print('coordinates: ({}, {})'.format(player.current_tile.centerX, player.current_tile.centerY))
								print('target_tile: ({}, {})'.format(tile.tileX, tile.tileY))
								print('coordinates: ({}, {})'.format(tile.centerX, tile.centerY))
								player.move_down(tile)
								player.finishing_animation = True
						player.map_moving = False
			else:
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
			#print(golden_map_tile.x)
			#standard player movement to respond to player movement flags set in the event loop
			if player.move_in_progress:
				if player.colliding == False:
					if player.moving_right and player.rect.right < screen.rect.right:
						if player.x >= screen.rect.right - settings.tile_size*20:
							player.animate_right()
							player.move_map_right()
							player.map_moving = True
						else:
							player.move_right()
							player.map_moving = False
					elif player.moving_left and player.rect.left > screen.rect.left:
						if player.x <= screen.rect.left + settings.tile_size*20:
							player.animate_left()
							player.move_map_left()
							player.map_moving = True
						else:
							player.move_left()
							player.map_moving = False	
					elif player.moving_up and player.rect.top > screen.rect.top:
						if player.y <= screen.rect.top + settings.tile_size*20:
							player.animate_up()
							player.move_map_up()
							player.map_moving = True
						else:
							player.move_up()
							player.map_moving = False		
					elif player.moving_down and player.rect.bottom < screen.rect.bottom:
						if player.y > screen.rect.bottom - settings.tile_size*20:
							player.animate_down()
							player.move_map_down()
							player.map_moving = True
						else:
							player.move_down()
							player.map_moving = False
			


def draw_display(settings, screen, player, level_map, display_box, map_entities):
	screen.fill()
	#level_map.blitme()
	for entity in map_entities:
		entity.blitme()
	player.blitme()

	if display_box.visible == True:
		display_box.blitme()

def generate_obstacles(settings, screen, level_map, obstacles):
	new_desk = Desk(settings.tile_size*16, settings.tile_size*8, settings, screen, level_map)
	obstacles.add(new_desk)
	coffee_machine = CoffeeMachine(settings.tile_size*4, settings.tile_size*3, settings, screen, level_map)
	obstacles.add(coffee_machine)


def build_map(settings, screen, level_map, obstacles, map_entities, tile_list):
	#For the given map recognize obstacles within the map image and add an obstacle object at its x and y location
	tile_x = 0
	tile_y = 0
	for y in range(0, level_map.rect.height, settings.tile_size):
		for x in range(0, level_map.rect.width, settings.tile_size):
			tile_key1 = level_map.image.get_at((x, y))
			#tile_key2 = level_map.image.get_at((x+1, y))
			#tile_key3 = level_map.image.get_at((x+2, y))
			#tile_key4 = level_map.image.get_at((x, y+1))
			#tile_key5 = level_map.image.get_at((x+1, y+1))
			#tile_key6 = level_map.image.get_at((x+2, y+1))
			#tile_key7 = level_map.image.get_at((x, y+3))
			#tile_key8 = level_map.image.get_at((x+1, y+3))
			#tile_key8 = level_map.image.get_at((x+2, y+3))

			for tile in images.obstacle_tiles:
				if  tile == tile_key1:
					wall = Wall(x, y, settings, screen)
					wall.centerX = x + settings.tile_size / 2
					wall.centerY = y + settings.tile_size / 2
					wall.tileX = tile_x
					wall.tileY = tile_y
					obstacles.add(wall)
					tile_list.add(wall)
					tile_x += 1
			for tile in images.background_tiles:	
				if  tile == tile_key1:
					carpet = Carpet(x, y, settings, screen)
					carpet.centerX = x + settings.tile_size / 2
					carpet.centerY = y + settings.tile_size / 2
					carpet.tileX = tile_x
					carpet.tileY = tile_y
					map_entities.add(carpet)
					tile_list.add(carpet)
					tile_x += 1
		# Keep track of tile row and column to provide grid position
		tile_y += 1
		tile_x = 0
	print('tile_list length: {}'.format(len(tile_list)))


