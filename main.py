"""
Main code for Real Office Life Simulator (ROLS)
Creator: Michael Bulua
Date: 4/26/2020
"""
#Import all libraries
import os
import random
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
from obstacle import Desk, Wall, NPC, NPC_Still, Item
from map_entity import Carpet, GoldenMapTile
from timer import Timer

def run_game():
	pygame.init()
	clock = pygame.time.Clock()
	settings = Settings()
	screen = Screen(settings)
	pygame.display.set_caption("Real Office Life Simulator")
	display_box = DisplayBox(settings, screen)
	
	#Create Groups
	timers = Group()
	items = Group()
	static_map_entities = Group()
	npcs = Group()
	obstacles = Group()
	collisions = Group()
	map_entities = Group()
	on_screen_entities = Group()

	#Build map and objects
	screen.fill()
	level_map = LevelMap(settings, screen)
	gf.generate_obstacles(settings, screen, level_map, obstacles, static_map_entities)
	gf.build_map(settings, screen, level_map, obstacles, map_entities, static_map_entities)
	golden_map_tile = GoldenMapTile(0, 0, settings, screen)

	#Variable for positioning items on the screen
	tile_unit = settings.tile_size

	report = Item(tile_unit*7, tile_unit*3, settings, screen, level_map)
	report2 = Item(tile_unit*9, tile_unit*3, settings, screen, level_map)

	player = Player(tile_unit*4, tile_unit*5, settings, screen, level_map, collisions, obstacles, map_entities, static_map_entities, golden_map_tile)
	girl = NPC_Still(tile_unit*16, tile_unit*3, settings, screen, level_map, collisions, 50, 20)
	boy = NPC_Still(tile_unit*5, tile_unit*6, settings, screen, level_map, collisions, 50, 20)
	
	npcs.add(boy)
	npcs.add(girl)
	items.add(report)
	items.add(report2)
	static_map_entities.add(items)
	static_map_entities.add(golden_map_tile)
	obstacles.add(npcs)
	obstacles.add(items)
	map_entities.add(obstacles)
	map_entities.add(golden_map_tile)


	#Add all groups that can collide with
	collisions.add(obstacles)
	collisions.add(player)

	main_menu = MainMenu(settings, screen, player)
	game_menu = GameMenu(settings, screen, player)

	#Set default interaction obstacle to None
	interaction_obstacle = None

	#Run main game loop
	while True:
		clock.tick_busy_loop(settings.framerate)

		event.event_loop(settings, screen, player, main_menu, display_box, obstacles, map_entities, collisions, interaction_obstacle, timers)

		#State Machine
		if settings.game_state == "main menu":
			gf.run_menu(settings, screen, player, main_menu)

		elif settings.game_state == "game menu":
			gf.run_menu(settings, screen, player, game_menu)

		elif settings.game_state == "run":	
			interaction_obstacle = gf.update_game(settings, obstacles, player, collisions, display_box, timers)
			gf.update_player(settings, screen, player, display_box, golden_map_tile, map_entities, static_map_entities)
			gf.draw_display(settings, screen, player, level_map, display_box, map_entities, on_screen_entities, npcs)

		gf.update_display()

run_game()




