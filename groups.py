import pygame
from pygame.sprite import Group

class Groups():
	'''class to hold all groups. Only vcreate one instance'''
	def __init__(self):
		#Create Groups
		timers = Group()
		items = Group()
		#Use NPCs group to redraw NPCS to properly level NPCs nd player
		npcs = Group()
		collisions = Group()
		map_entities = Group()
		screen_boxes = Group()
		#Use on screen entities to stop drawing entities that are not on the screen
		on_screen_entities = Group()