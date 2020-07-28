import math
import pygame
from pygame.sprite import collide_rect
from menu import Menu
from display_box import DisplayBox
import images
from obstacle import Desk, Wall, NPC, CoffeeMachine
from map_entity import Carpet


def update_display():
	# make the most recently drawn screen visible			
	pygame.display.update()	

def run_menu(settings, screen, player, menu):
	'''run the main menu state'''
	menu.blitme()


def draw_display(settings, screen, player, level_map, display_box, map_entities, on_screen_entities, npcs):
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
	for entity in map_entities:
		entity.blitme()

	#Draw NPC on top of player if it is below it
	player.blitme()
	for npc in npcs:
		if npc.y > player.y:
			npc.blitme()

	if display_box.visible == True:
		display_box.blitme()

def update_game(settings, obstacles, player, collisions, display_box, timers):
	#Update obstacles and timers
	player.ready_for_interaction = False
	
	interaction_obstacle = None
	player_collision = player.get_collision_rect()

	#Update game timers
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

	#Update game obstacles
	for obstacle in obstacles:
		#Updating the obstacle will move if it is a dynamic obstacle
		#if not settings.game_paused:
		obstacle.update()


		#Functionality for obstacles that can interact with the player
		if obstacle.interactable == True:
			if player_collision.rect.colliderect(obstacle.rect):
				if (obstacle.side_interactable and player.direction == obstacle.interaction_side) or not obstacle.side_interactable:
						player.ready_for_interaction = True
						interaction_obstacle = obstacle
				break
	return interaction_obstacle
	

def update_player(settings, screen, player, display_box, golden_map_tile, map_entities, static_map_entities):
	if not settings.game_paused:	
		if player.finishing_animation:
			player.finish_animation()

		player.check_collisions()
		if player.colliding:
			for ent in static_map_entities:
				ent.x = player.round_to_tileset(ent.x)
				ent.y = player.round_to_tileset(ent.y)
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


def generate_obstacles(settings, screen, level_map, obstacles, static_map_entities):
	new_desk = Desk(settings.tile_size*16, settings.tile_size*8, settings, screen, level_map)
	obstacles.add(new_desk)
	static_map_entities.add(new_desk)
	coffee_machine = CoffeeMachine(settings.tile_size*4, settings.tile_size*3, settings, screen, level_map)
	obstacles.add(coffee_machine)
	static_map_entities.add(coffee_machine)


def build_map(settings, screen, level_map, obstacles, map_entities, static_map_entities):
	#For the given map recognize obstacles within the map image and add a obstacle object at its x and y location
	for y in range(0, level_map.rect.height, settings.tile_size):
		for x in range(0, level_map.rect.width, settings.tile_size):
			tile_key1 = level_map.image.get_at((x+3, y+17))
			tile_key2 = level_map.image.get_at((x+6, y+10))
			tile_key3 = level_map.image.get_at((x+22, y+5))
			tile_key4 = level_map.image.get_at((x+25, y+13))
			tile_key5 = level_map.image.get_at((x+30, y+4))

			tile_key =[]
			tile_key.append(tile_key1)
			tile_key.append(tile_key2)
			tile_key.append(tile_key3)
			tile_key.append(tile_key4)
			tile_key.append(tile_key5)

			for tile in images.obstacle_tiles:
				if  tile == tile_key:
					wall = Wall(x, y, settings, screen, level_map)
					obstacles.add(wall)
					static_map_entities.add(wall)
			for tile in images.background_tiles:	
				if  tile == tile_key:
					carpet = Carpet(x, y, settings, screen)
					map_entities.add(carpet)
					static_map_entities.add(carpet)