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
#from program_data import ProgramData
from program_variables import program_data as pd, settings
from player import Player
from menu import Menu, MainMenu, GameMenu
from battle_arena import BattleArena
from level_map import LevelMap
from obstacle import Desk, Wall, Item, Character
from NPC import NPC, NPC_Still, NPC_Battler
from timer import Timer

def run_game():
	#Initialize the program
	gf.initialize_program()
	clock = pygame.time.Clock()

	
	#Build map and objects
	gf.generate_obstacles()
	gf.build_map()

	#Variable for positioning items on the screen
	tile_unit = settings.tile_size

	report = Item(tile_unit*17, tile_unit*34)
	report2 = Item(tile_unit*15, tile_unit*34)

	player = Player(tile_unit*6, tile_unit*10)
	boy = NPC_Still(tile_unit*18, tile_unit*41)
	battle_kid = NPC_Battler(tile_unit*17, tile_unit*38)

	battle_arena = BattleArena()
	
	pd.npcs.add(boy)
	pd.npcs.add(battle_kid)
	pd.items.add(report)
	pd.items.add(report2)
	pd.map_entities.add(settings.golden_map_tile)
	pd.map_entities.add(pd.items)
	pd.map_entities.add(pd.npcs)
	pd.collisions.add(pd.npcs)
	pd.collisions.add(pd.items)

	gf.set_map_position()

	#Add all groups that can collide with
	pd.collisions.add(player)

	main_menu = MainMenu(player)
	game_menu = GameMenu(player)


	#Run main game loop
	while True:
		clock.tick_busy_loop(settings.framerate)

		event.event_loop(player, main_menu)

		#State Machine
		if pd.game_state == "initialize":
			settings.screen.fill()
			pd.game_state = "main menu"
		if pd.game_state == "main menu":
			gf.run_menu(player, main_menu)

		elif pd.game_state == "game menu":
			pygame.mixer.music.play()
			gf.run_menu(player, game_menu)

		elif pd.game_state == "run":	
			gf.update_game(player)
			gf.update_player(player)
			gf.draw_display(player)

		elif pd.game_state == "battle":
			gf.draw_battle_display(player, battle_arena)

		gf.update_display()
run_game()