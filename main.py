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
from obstacle import Desk, Wall, GirlNPC



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

	player = Player(settings, screen, level_map, 300, 250, collisions, display_box, obstacles)
	girl = GirlNPC(settings, screen, level_map, 500, 100, collisions)
	obstacles.add(girl)

	#Add all groups that can collide with
	collisions.add(obstacles)
	collisions.add(player)

	main_menu = MainMenu(settings, screen, player)
	game_menu = GameMenu(settings, screen, player)

	#Run main game loop
	while True:
		clock.tick_busy_loop(30)
		event.event_loop(settings, screen, player, main_menu, display_box)

		#State Machine
		if settings.game_state == "main menu":
			gf.run_menu(settings, screen, player, main_menu)

		elif settings.game_state == "game menu":
			gf.run_menu(settings, screen, player, game_menu)

		elif settings.game_state == "run":	
			gf.update_game(settings, obstacles, player, collisions)
			gf.update_player(settings, screen, player, display_box)
			gf.draw_display(settings, screen, player, level_map, display_box, obstacles)

		gf.update_display()

run_game()




