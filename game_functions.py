import pygame
from pygame.sprite import collide_rect
from menu import Menu
from display_box import DisplayBox
#from object import Object
from barrier import Barrier, Object
import images

def update_screen(screen, settings, display_box, level_map):
	'''Redraw the screen during each pass through the loop to prep for next frame of game image'''
	screen.fill(settings.bg_color)
	#Draw map
	level_map.blitme()

def run_main_menu(screen, settings, player, menu):
	'''run the main menu state'''
	menu.blitme()
	# make the most recently drawn screen visible
	pygame.display.update()

def run_game_menu(screen, settings, player, menu):
	'''run the in game menu state'''
	menu.blitme()
	# make the most recently drawn screen visible
	pygame.display.update()

def update_game(screen, settings, player, display_box, objects, character):
	#Update Player position
	player.update_position()
	#Update all NPCs
	character.movement()
	#Update the screen visuals every other loop
	settings.loop_count += 1
	if settings.loop_count % 10 == 1:
		#Draw player to screen
		player.blitme()
		character.blitme()
		#Draw display box
		display_box.blitme()
		#Draw objects
		for obj in objects:
			obj.blitme()

		# make the most recently drawn screen visible			
		pygame.display.update()	


def generate_objects(screen, settings, objects):
	new_object = Object(screen, settings, 200, 200)
	objects.add(new_object)
	new_object = Object(screen, settings, 500, 250)
	objects.add(new_object)


def build_map(screen, settings, barriers):
	screen_rect = screen.get_rect()
	for y in range(0, screen_rect.height, settings.tile_size):
		for x in range(0, screen_rect.width, settings.tile_size):
			tile_key = screen.get_at((x, y))
			for tile in images.barrier_tiles:
				if tile == tile_key:
					wall = Barrier(screen, settings, x, y)
					barriers.add(wall)
