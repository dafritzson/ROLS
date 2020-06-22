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

def update_game(settings, screen, player, display_box, obstacles):
	#Draw player to screen
	player.blitme()
	#Draw display box
	display_box.blitme()
	#Draw obstacles
	for obstacle in obstacles:
		obstacle.update()
		obstacle.blitme()
		
	# make the most recently drawn screen visible			
	pygame.display.update()	

def update_player(settings, screen, player, display_box):
	player.check_collision()
	#standard player movement to respond to player movement flags set in the event loop
	if player.move_in_progress:
		if player.moving_right and player.rect.right < screen.rect.right:
			player.move_right()
		elif player.moving_left and player.rect.left > screen.rect.left:
			player.move_left()
		elif player.moving_up and player.rect.top > screen.rect.top:
			player.move_up()
		elif player.moving_down and player.rect.bottom < display_box.rect.top:
			player.move_down()

	#Finish the animation for all movements. Only run after a keyup ends the player movement.
	if player.move_count < 4 and player.finishing_animation:
		if player.direction == "right":
			player.move_right()
		elif player.direction == "left":
			player.move_left()
		elif player.direction == "up":
			player.move_up()
		elif player.direction == "down":
			player.move_down()
		else:
			pass
		player.move_count += 1

	#Reset animation count
	else:
		player.move_count = 0
		player.finishing_animation = False


def generate_obstacles(settings, screen, obstacles):
	new_desk = Desk(settings, screen, 200, 200)
	obstacles.add(new_desk)
	new_desk = Desk(settings, screen, 500, 250)
	obstacles.add(new_desk)


def build_map(settings, screen, obstacles):
	for y in range(0, screen.rect.height, settings.tile_size):
		for x in range(0, screen.rect.width, settings.tile_size):
			tile_key = screen.display.get_at((x, y))
			for tile in images.barrier_tiles:
				if tile == tile_key:
					wall = Wall(settings, screen, x, y)
					obstacles.add(wall)
