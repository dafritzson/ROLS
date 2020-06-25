"""
Main code for Real Office Life Simulator (ROLS)
Creator: Michael Bulua
Date: 4/26/2020
"""
#Import all libraries
import time
import os
import pygame	
from pygame.sprite import Group


#Import Function Files
import event_functions as event
import game_functions as gf

#Import Classes
from settings import Settings
from screen import Screen
from player import Player
from menu import Menu, MainMenu, GameMenu
from display_box import DisplayBox
from level_map import LevelMap
from obstacle import Desk, Wall, GirlNPC

def run_game():
	pygame.init()
	clock = pygame.time.Clock()
	settings = Settings()
	#screen = pygame.display.set_mode(size=(settings.screen_width, settings.screen_height))
	screen = Screen(settings)
	pygame.display.set_caption("Real Office Life Simulator")
	display_box = DisplayBox(settings, screen)
	obstacles = Group()
	collisions = Group()


	#Build map and objects
	level_map = LevelMap(settings, screen)
	gf.generate_obstacles(settings, screen, level_map, obstacles)
	gf.update_screen(settings, screen, display_box, level_map)
	gf.build_map(settings, screen, level_map, obstacles)
	#set map to background only:
	level_map.image = pygame.image.load('.\\Images\\Map\\test_map_background.png')


	#Add all groups the player can collide with
	collisions.add(obstacles)

	player = Player(settings, screen, level_map, display_box, collisions, obstacles)
	girl = GirlNPC(settings, screen, level_map, 500, 100)
	obstacles.add(girl)
	collisions.add(girl)

	main_menu = MainMenu(settings, screen, player)
	game_menu = GameMenu(settings, screen, player)

	image = pygame.image.load('.\\Images\\Map\\cubicle_wall.png')
	rect = image.get_rect()
	rect.midleft = screen.rect.midleft
	screen.display.blit(image, rect)
	for y in range(0, rect.height):
		for x in range(0, rect.width):
			tile_key1 = image.get_at((x, y))
			print(tile_key1)

	#Run main game loop
	while True:
		clock.tick_busy_loop(30)
		gf.update_screen(settings, screen, display_box, level_map)

		#State Machine
		if settings.game_state == "main menu":
			event.event_loop(settings, screen, player, main_menu)
			gf.run_menu(settings, screen, player, main_menu)

		elif settings.game_state == "game menu":
			event.event_loop(settings, screen, player, game_menu)
			gf.run_menu(settings, screen, player, game_menu)

		elif settings.game_state == "run":	
			event.event_loop(settings, screen, player, main_menu)
			gf.update_game(settings, obstacles)
			gf.update_player(settings, screen, player, display_box)
			gf.draw_display(settings, screen, player, level_map, display_box, obstacles)

		gf.update_display()

run_game()




