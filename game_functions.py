import pygame
from pygame.sprite import collide_rect
from menu import Menu
from display_box import DisplayBox
import images
from obstacle import Desk, Wall, NPC


def update_display():
	# make the most recently drawn screen visible			
	pygame.display.update()	

def run_menu(settings, screen, player, menu):
	'''run the main menu state'''
	menu.blitme()

def update_screen(settings, screen, display_box, level_map):
	'''Redraw the screen during each pass through the loop to prep for next frame of game image'''
	screen.fill()

def update_game(settings, obstacles, player, collisions, display_box):
	#Update obstacle positions
	player_is_interacting = False
	for obstacle in obstacles:
		#Updating the obstacle will move it if it is a dynamic obstacle in the obstacle group
		obstacle.update()
		if obstacle.interactable == True:
			#if pygame.sprite.collide_rect(obstacle, player):
			#	print("press enter")
			if player.rect.colliderect(obstacle.rect):
				if (obstacle.side_interactable and player.direction == obstacle.interaction_side) or not obstacle.side_interactable:
						player_is_interacting = True
						display_box.message_key = obstacle.interaction_message
				if obstacle.pickupable:
					print("You get a point")
	if player_is_interacting:	
		player.ready_for_interaction = True
	else:
		player.ready_for_interaction = False

def update_player(settings, screen, player, display_box):
	player.check_collisions()
	#standard player movement to respond to player movement flags set in the event loop
	if player.move_in_progress:
		if player.moving_right and player.rect.right < screen.rect.right:
			if player.rect.x > screen.rect.centerx + screen.rect.width / 3:
				player.animate_right()
				player.move_map_right()
			else:
				player.move_right()
		elif player.moving_left and player.rect.left > screen.rect.left:
			if player.rect.x < screen.rect.centerx - screen.rect.width / 3:
				player.animate_left()
				player.move_map_left()
			else:
				player.move_left()		
		elif player.moving_up and player.rect.top > screen.rect.top:
			if player.rect.y < screen.rect.height / 6:
				player.animate_up()
				player.move_map_up()
			else:
				player.move_up()		
		elif player.moving_down and player.rect.bottom < display_box.rect.top:
			if player.rect.y > screen.rect.centery + screen.rect.height / 8:
				player.animate_down()
				player.move_map_down()
			else:
				player.move_down()

	if player.finishing_animation:
		player.finish_animation()


def draw_display(settings, screen, player, level_map, display_box, obstacles):
	screen.fill()
	level_map.blitme()
	player.blitme()
	for obstacle in obstacles:
		obstacle.blitme()
	display_box.blitme()

def generate_obstacles(settings, screen, level_map, obstacles):
	new_desk = Desk(settings, screen, level_map, 208, 208)
	obstacles.add(new_desk)
	new_desk = Desk(settings, screen, level_map, 488, 240)
	obstacles.add(new_desk)


def build_map(settings, screen, level_map, obstacles):
	#For the given map recognize obstacles within the map image and add a obstacle object at its x and y location
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

			for tile in images.barrier_tiles:
				if tile_key1 == tile:
					wall = Wall(settings, screen, level_map, x, y)
					obstacles.add(wall)


