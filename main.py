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
import audio_mixer as am

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
	#Initialize game mixer
	pygame.mixer.init()
	settings = Settings()
	screen = Screen(settings)
	pygame.display.set_caption("Real Office Life Simulator")
	display_box = DisplayBox(settings, screen)
	
	#Create Groups
	timers = Group()
	items = Group()
	base_map_entities = Group()
	#overlay map entities include all interactable obstacles, and items
	overlay_map_entities = Group()
	#Use NPCs group to redraw NPCS to properly level NPCs nd player
	npcs = Group()
	collisions = Group()
	map_entities = Group()
	#Use on screen entities to stop drawing entities that are not on the screen
	on_screen_entities = Group()

	#Build map and objects
	screen.fill()
	level_map = LevelMap(settings, screen)
	gf.generate_obstacles(settings, screen, level_map, collisions, overlay_map_entities)
	gf.build_map(settings, screen, level_map, collisions, base_map_entities)
	golden_map_tile = GoldenMapTile(0, 0, settings, screen)

	#Variable for positioning items on the screen
	tile_unit = settings.tile_size

	report = Item(tile_unit*17, tile_unit*34, settings, screen, level_map)
	report2 = Item(tile_unit*15, tile_unit*34, settings, screen, level_map)

	player = Player(tile_unit*6, tile_unit*10, settings, screen, level_map, collisions, map_entities, overlay_map_entities, golden_map_tile)
	boy = NPC_Still(tile_unit*15, tile_unit*37, settings, screen, level_map, collisions, 50, 20)
	
	npcs.add(boy)
	items.add(report)
	items.add(report2)
	base_map_entities.add(golden_map_tile)
	overlay_map_entities.add(items)
	overlay_map_entities.add(npcs)
	collisions.add(npcs)
	collisions.add(items)
	map_entities.add(base_map_entities)
	map_entities.add(overlay_map_entities)
	map_entities.add(golden_map_tile)

	gf.set_map_position(settings, screen, level_map, map_entities)

	#Add all groups that can collide with
	collisions.add(player)

	main_menu = MainMenu(settings, screen, player)
	game_menu = GameMenu(settings, screen, player)

	#Set default interaction obstacle to None
	interaction_obstacle = None



	#Run main game loop
	while True:
		clock.tick_busy_loop(settings.framerate)

		event.event_loop(settings, screen, player, main_menu, display_box, map_entities, overlay_map_entities, collisions, interaction_obstacle, timers, items)

		#State Machine
		if settings.game_state == "main menu":
			gf.run_menu(settings, screen, player, main_menu)

		elif settings.game_state == "game menu":
			pygame.mixer.music.play()
			gf.run_menu(settings, screen, player, game_menu)

		elif settings.game_state == "run":	
			interaction_obstacle = gf.update_game(settings, player, collisions, display_box, timers)
			gf.update_player(settings, screen, player, display_box, golden_map_tile, map_entities, overlay_map_entities, level_map)
			gf.draw_display(settings, screen, player, level_map, display_box, map_entities, base_map_entities, overlay_map_entities, on_screen_entities, npcs, items)

		gf.update_display()
run_game()




