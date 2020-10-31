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
from screen import Screen
from player import Player
from menu import Menu, MainMenu, GameMenu
from display_box import DisplayBox, DummyBox
from battle_arena import BattleArena
from audio_mixer import AudioMixer
from level_map import LevelMap
from obstacle import Desk, Wall, Item, Character
from NPC import NPC, NPC_Still, NPC_Battler
from map_entity import Carpet, GoldenMapTile
from timer import Timer

def run_game():
	pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.mixer.init()
	pygame.init()
	clock = pygame.time.Clock()
	program_data = ProgramData()
	screen = Screen(program_data)
	pygame.display.set_caption("Real Office Life Simulator")
	audio_mixer = AudioMixer(program_data)
	display_box = DisplayBox(program_data, screen, audio_mixer)
	
	#Create Groups
	timers = Group()
	items = Group()
	npcs = Group()
	collisions = Group()
	map_entities = Group()
	display_boxes = Group()
	on_screen_entities = Group()

	groups = {'timers' : timers, 'items' : items, 'npcs' : npcs, 'collisions' : collisions, 'map_entities' : map_entities, 'display_boxes' : display_boxes, 'on_screen_entities' : on_screen_entities}

	#Build map and objects
	screen.fill()
	level_map = LevelMap(program_data, screen)
	gf.generate_obstacles(groups, program_data, screen, level_map)
	gf.build_map(groups, program_data, screen, level_map)
	golden_map_tile = GoldenMapTile(0, 0, program_data, screen)
	dummy_box = DummyBox()
	groups.get('display_boxes').add(dummy_box)

	#Variable for positioning items on the screen
	tile_unit = program_data.tile_size

	report = Item(tile_unit*17, tile_unit*34, program_data, screen, level_map)
	report2 = Item(tile_unit*15, tile_unit*34, program_data, screen, level_map)

	player = Player(tile_unit*6, tile_unit*10, program_data, screen, level_map, collisions, map_entities, golden_map_tile)
	boy = NPC_Still(tile_unit*15, tile_unit*37, program_data, screen, level_map, collisions)
	battle_kid = NPC_Battler(tile_unit*17, tile_unit*38, program_data, screen, level_map, collisions)

	battle_arena = BattleArena(program_data, screen, audio_mixer)
	
	npcs.add(boy)
	npcs.add(battle_kid)
	items.add(report)
	items.add(report2)
	map_entities.add(golden_map_tile)
	map_entities.add(items)
	map_entities.add(npcs)
	map_entities.add(golden_map_tile)
	collisions.add(npcs)
	collisions.add(items)

	gf.set_map_position(groups, program_data, screen, level_map)

	#Add all groups that can collide with
	collisions.add(player)

	main_menu = MainMenu(program_data, screen, player)
	game_menu = GameMenu(program_data, screen, player)

	#Set default interaction obstacle to None
	interaction_obstacle = None


	#Run main game loop
	while True:
		clock.tick_busy_loop(program_data.framerate)

		event.event_loop(groups, program_data, screen, player, main_menu, interaction_obstacle, audio_mixer)

		#State Machine
		if program_data.game_state == "main menu":
			gf.run_menu(program_data, screen, player, main_menu)

		elif program_data.game_state == "game menu":
			pygame.mixer.music.play()
			gf.run_menu(program_data, screen, player, game_menu)

		elif program_data.game_state == "run":	
			interaction_obstacle = gf.update_game(groups, program_data, player)
			gf.update_player(groups, program_data, screen, player, golden_map_tile, level_map)
			gf.draw_display(groups, program_data, screen, player, level_map)

		elif program_data.game_state == "battle":
			gf.draw_battle_display(groups, program_data, screen, player, battle_arena)

		gf.update_display()
run_game()




