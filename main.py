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
from obstacle import Desk, Wall, NPC, Item

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


	#Build map and objects
	level_map = LevelMap(settings, screen)
	gf.generate_obstacles(settings, screen, level_map, obstacles)
	gf.update_screen(settings, screen, display_box, level_map)
	gf.build_map(settings, screen, level_map, obstacles)
	#set map to background only:
	level_map.image = pygame.image.load('.\\Images\\Maps\\test_map_background.png')
	report = Item(settings, screen, level_map, 300, 75)
	report2 = Item(settings, screen, level_map, 400, 75)

	player = Player(settings, screen, level_map, 300, 250, collisions, display_box, obstacles, report)
	girl = NPC(settings, screen, level_map, 500, 100, collisions, 50, 20)
	boy = NPC(settings, screen, level_map, 200, 75, collisions, 50, 20)
	items.add(report)
	items.add(report2)
	obstacles.add(boy)
	obstacles.add(girl)
	obstacles.add(items)

	#Add all groups that can collide with
	collisions.add(obstacles)
	collisions.add(player)

	main_menu = MainMenu(settings, screen, player)
	game_menu = GameMenu(settings, screen, player)

	#Run main game loop
	interaction_obstacle=None
	while True:
		clock.tick_busy_loop(30)
		event.event_loop(settings, screen, player, main_menu, display_box, obstacles, collisions, interaction_obstacle)

		#State Machine
		if settings.game_state == "main menu":
			gf.run_menu(settings, screen, player, main_menu)

		elif settings.game_state == "game menu":
			gf.run_menu(settings, screen, player, game_menu)

		elif settings.game_state == "run":	
			interaction_obstacle=gf.update_game(settings, obstacles, player, collisions, display_box)
			gf.update_player(settings, screen, player, display_box)
			gf.draw_display(settings, screen, player, level_map, display_box, obstacles)

		gf.update_display()

run_game()




