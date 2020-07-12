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
from map import Carpet, GoldenMapTile

def run_game():
	pygame.init()
	clock = pygame.time.Clock()
	settings = Settings()
	#screen = pygame.display.set_mode(size=(settings.screen_width, settings.screen_height))
	screen = Screen(settings)
	pygame.display.set_caption("Real Office Life Simulator")
	display_box = DisplayBox(settings, screen)
	
	#Create Groups
	#obstacles defines all obstacles besides the player
	obstacles = Group()
	#collisions defines all collideable obstacles including the player
	collisions = Group()
	#items defines all items the player can interact with
	items = Group()
	#map_entities defines all obstacles, NPCs, items and background tiles that make up the map
	map_entities = Group()

	#Build map and objects
	level_map = LevelMap(settings, screen)
	gf.generate_obstacles(settings, screen, level_map, obstacles)
	gf.update_screen(settings, screen, display_box, level_map)
	gf.build_map(settings, screen, level_map, obstacles, map_entities)
	goldenMapTile = GoldenMapTile(0, 0, settings, screen)

	#set map to background only:

	#variables for positioning items on the screen
	tile_unit = settings.tile_size
	item_unit = settings.tile_size/2

	report = Item(item_unit*16, item_unit*3, settings, screen, level_map)
	report2 = Item(item_unit*19, item_unit*3, settings, screen, level_map)

	player = Player(tile_unit*4, tile_unit*10, settings, screen, level_map, collisions, display_box, obstacles, map_entities, goldenMapTile)
	girl = NPC(500, 100, settings, screen, level_map, collisions, 50, 20)
	boy = NPC_Still(tile_unit*5, tile_unit*4, settings, screen, level_map, collisions, 50, 20)
	items.add(report)
	items.add(report2)
	obstacles.add(boy)
	obstacles.add(girl)
	obstacles.add(items)
	map_entities.add(obstacles)
	map_entities.add(goldenMapTile)


	#Add all groups that can collide with
	collisions.add(obstacles)
	collisions.add(player)

	main_menu = MainMenu(settings, screen, player)
	game_menu = GameMenu(settings, screen, player)

	#Set default interaction obstacle to None
	interaction_obstacle = None

	#Run main game loop
	while True:
		print(goldenMapTile.rect.x)
		clock.tick_busy_loop(30)
		event.event_loop(settings, screen, player, main_menu, display_box, obstacles, collisions, interaction_obstacle)


		#State Machine
		if settings.game_state == "main menu":
			gf.run_menu(settings, screen, player, main_menu)

		elif settings.game_state == "game menu":
			gf.run_menu(settings, screen, player, game_menu)

		elif settings.game_state == "run":	
			interaction_obstacle = gf.update_game(settings, obstacles, player, collisions, display_box)
			gf.update_player(settings, screen, player, display_box)
			gf.draw_display(settings, screen, player, level_map, display_box, map_entities)

		gf.update_display()

run_game()




