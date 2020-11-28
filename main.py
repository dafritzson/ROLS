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
from program_data import ProgramData
from player import Player
from menu import Menu, MainMenu, GameMenu
from battle_arena import BattleArena
from level_map import LevelMap
from obstacle import Desk, Wall, Item, Character
from NPC import NPC, NPC_Still, NPC_Battler
from map_entity import Carpet, GoldenMapTile
from timer import Timer

def run_game():
	#Initialize the program
	gf.initialize_program()
	program_data = ProgramData()
	clock = pygame.time.Clock()

	
	#Build map and objects
	gf.generate_obstacles(program_data)
	gf.build_map(program_data)

	#Variable for positioning items on the screen
	tile_unit = program_data.tile_size

	report = Item(tile_unit*17, tile_unit*34, program_data)
	report2 = Item(tile_unit*15, tile_unit*34, program_data)

	player = Player(tile_unit*6, tile_unit*10, program_data)
	boy = NPC_Still(tile_unit*18, tile_unit*41, program_data)
	battle_kid = NPC_Battler(tile_unit*17, tile_unit*38, program_data)

	battle_arena = BattleArena(program_data)
	
	program_data.npcs.add(boy)
	program_data.npcs.add(battle_kid)
	program_data.items.add(report)
	program_data.items.add(report2)
	program_data.map_entities.add(program_data.golden_map_tile)
	program_data.map_entities.add(program_data.items)
	program_data.map_entities.add(program_data.npcs)
	program_data.collisions.add(program_data.npcs)
	program_data.collisions.add(program_data.items)

	gf.set_map_position(program_data)

	#Add all groups that can collide with
	program_data.collisions.add(player)

	main_menu = MainMenu(program_data, player)
	game_menu = GameMenu(program_data, player)


	#Run main game loop
	while True:
		clock.tick_busy_loop(program_data.framerate)

		event.event_loop( program_data, player, main_menu)

		#State Machine
		if program_data.game_state == "initialize":
			program_data.screen.fill()
			program_data.game_state = "main menu"
		if program_data.game_state == "main menu":
			gf.run_menu(program_data, player, main_menu)

		elif program_data.game_state == "game menu":
			pygame.mixer.music.play()
			gf.run_menu(program_data, player, game_menu)

		elif program_data.game_state == "run":	
			gf.update_game(program_data, player)
			gf.update_player(program_data, player)
			gf.draw_display(program_data, player)

		elif program_data.game_state == "battle":
			gf.draw_battle_display(program_data, player, battle_arena)

		gf.update_display()
run_game()