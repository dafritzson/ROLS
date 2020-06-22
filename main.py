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
	gf.generate_obstacles(settings, screen, obstacles)
	level_map = LevelMap(settings, screen)
	gf.update_screen(settings, screen, display_box, level_map)
	gf.build_map(settings, screen, obstacles)

	player = Player(settings, screen, display_box, collisions)
	girl = GirlNPC(settings, screen, 500, 100)
	obstacles.add(girl)

	#Add all groups the player can collide with
	collisions.add(obstacles)

	main_menu = MainMenu(settings, screen, player)
	game_menu = GameMenu(settings, screen, player)

	
	#Run main game loop
	while True:
		#event_type = pygame.event.get()
		#if event_type != []:
		#	print (event_type)
		clock.tick_busy_loop(30)
		#State Machine
		if settings.game_state == "main menu":
			event.event_loop(settings, screen, player, main_menu)
			gf.update_screen(settings, screen, display_box, level_map)
			gf.run_main_menu(settings, screen, player, main_menu)

		elif settings.game_state == "run":	
			event.event_loop(settings, screen, player, main_menu)
			gf.update_screen(settings, screen, display_box, level_map)
			gf.update_game(settings, screen, player, display_box, obstacles)
			gf.update_player(settings, screen, player, display_box)
			#print(pygame.key.get_repeat())
			
		elif settings.game_state == "game menu":
			event.event_loop(settings, screen, player, game_menu)
			gf.update_screen(settings, screen, display_box, level_map)
			gf.run_game_menu(settings, screen, player, game_menu)
run_game()




