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
from player import Player
from character import Character
from menu import Menu, MainMenu, GameMenu
from display_box import DisplayBox
#from object import Object
from level_map import LevelMap
from barrier import Barrier, Object
from obstacle import GirlNPC

def run_game():
	pygame.init()
	
	settings = Settings()
	screen = pygame.display.set_mode(size=(settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Real Office Life Simulator")
	display_box = DisplayBox(screen, settings)
	objects = Group()
	barriers = Group()
	collisions = Group()
	NPCs = Group()
	
	#Build map and objects
	gf.generate_objects(screen, settings, objects)
	level_map = LevelMap(screen, settings)
	gf.update_screen(screen, settings, display_box, level_map)
	gf.build_map(screen, settings, barriers)

	player = Player(screen, settings, display_box, collisions)
	girl = Character(screen, settings, display_box)
	# New method using the new obstacles. Also, why is display_box passed as an arg to Character()?
	# girl = obstacle.GirlNPC(screen, settings, x, y)
	NPCs.add(girl)

	#Add all groups the player can collide with
	collisions.add(objects)
	collisions.add(barriers)
	collisions.add(NPCs)
	main_menu = MainMenu(screen, settings, player)
	game_menu = GameMenu(screen, settings, player)

	
	#Run main game loop
	while True:
		#State Machine
		if settings.game_state == "main menu":
			event.event_loop(screen, settings, player, main_menu)
			gf.update_screen(screen, settings, display_box, level_map)
			gf.run_main_menu(screen, settings, player, main_menu)

		elif settings.game_state == "run":	
			event.event_loop(screen, settings, player, main_menu)
			gf.update_screen(screen, settings, display_box, level_map)
			gf.update_game(screen, settings, player, display_box, objects, girl)
			
		elif settings.game_state == "game menu":
			event.event_loop(screen, settings, player, game_menu)
			gf.update_screen(screen, settings, display_box, level_map)
			gf.run_game_menu(screen, settings, player, game_menu)
run_game()




