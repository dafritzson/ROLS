import time
import pygame
from pygame.sprite import Group

from screen import Screen
from player import Player
from audio_mixer import AudioMixer
from level_map import LevelMap
from display_box import DisplayBox, DummyBox
from map_entity import GoldenMapTile


class ProgramData():
	'''Hold all program_variables and back-end variables of the game'''

	def __init__(self):
		'''initialize all attributes'''

		self.tile_size = 32
		self.framerate = 36

		#Game Style
		self.text_color = (4,5,8)


		#Game State
		self.game_state = "initialize"
		self.game_states = ["main menu", "run", "game menu", "battle" "close"]
		self.game_paused = False

		#General Counters
		self.arrow_value = 1
		
		#Create Groups
		self.timers = Group()
		self.items = Group()
		self.npcs = Group()	
		self.collisions = Group()
		self.map_entities = Group()
		self.display_boxes = Group()
		self.on_screen_entities = Group()

		#Initialize data in groups
		self.dummy_box = DummyBox()
		self.display_boxes.add(self.dummy_box)

		#Global variables
		self.interaction_obstacle = None

		#Create Objects
		#self.player = Player()
		self.golden_map_tile = GoldenMapTile(0,0)
		self.audio_mixer = AudioMixer()
		self.screen = Screen(self.tile_size)
		self.level_map = LevelMap(self.screen)

program_data = ProgramData()





