import pygame
from pygame.sprite import collide_rect
from menu import Menu
from display_box import DisplayBox
import images
from obstacle import Desk, Wall, GirlNPC


def update_screen(settings, screen, display_box, level_map):
	'''Redraw the screen during each pass through the loop to prep for next frame of game image'''
	screen.fill()
	#Draw map
	level_map.blitme()

def run_main_menu(settings, screen, player, menu):
	'''run the main menu state'''
	menu.blitme()
	# make the most recently drawn screen visible
	pygame.display.update()

def run_game_menu(settings, screen, player, menu):
	'''run the in game menu state'''
	menu.blitme()
	# make the most recently drawn screen visible
	pygame.display.update()

def update_game(settings, screen, player, level_map, display_box, obstacles):
	#Draw player to screen
	player.blitme()
	#Draw display box
	display_box.blitme()
	#Draw obstacles
	for obstacle in obstacles:
		obstacle.update()
		obstacle.blitme()
	
	#update_map(settings, screen, level_map, display_box, player)

	# make the most recently drawn screen visible			
	pygame.display.update()	

def update_player(settings, screen, player, level_map, display_box):
	player.check_collision()
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

	#Finish the animation for all movements. Only run after a keyup ends the player movement.
	if player.finishing_animation and not player.move_in_progress:
		#player.check_collision()
		if (player.direction == "right" or player.direction == "left") and player.rect.x % 8 != 0:
			if player.direction == "right":
				player.move_right()
			elif player.direction == "left":
				player.move_left()
		elif (player.direction == "up" or player.direction == "down") and player.rect.y % 8 != 0:
			if player.direction == "up":
				player.move_up()
			elif player.direction == "down":
				player.move_down()
		else:
			player.finishing_animation = False

def update_map(settings, screen, level_map, display_box, player):
	if player.move_in_progress or player.finishing_animation:
		if player.direction == "right" and player.rect.x > screen.rect.centerx + screen.rect.width / 3:
			level_map.move_map_right()
		if player.direction == "left" and player.rect.x < screen.rect.centerx - screen.rect.width / 3:
			level_map.move_map_left()
		if player.direction == "up" and player.rect.y > screen.rect.height / 3:
			level_map.move_map_up()
		if player.direction == "down" and player.rect.y < 2* screen.rect.height / 3:
			level_map.move_map_down()


def generate_obstacles(settings, screen, static_objects, obstacles):
	new_desk = Desk(settings, screen, 200, 200)
	obstacles.add(new_desk)
	static_objects.add(new_desk)
	new_desk = Desk(settings, screen, 500, 250)
	obstacles.add(new_desk)
	static_objects.add(new_desk)


def build_map(settings, screen, level_map, static_objects, obstacles):
	print(level_map.rect.height)
	print(level_map.rect.width)
	for y in range(0, level_map.rect.height, settings.tile_size):
		for x in range(0, level_map.rect.width, settings.tile_size):
			tile_key = level_map.image.get_at((x, y))
			for tile in images.barrier_tiles:
				if tile_key == tile:
					wall = Wall(settings, screen, x, y)
					obstacles.add(wall)
					static_objects.add(wall)

