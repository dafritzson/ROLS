import time
import pygame
from pygame.sprite import Group
from screen import Screen
from golden_map_tile import GoldenMapTile

class Settings():
	'''Hold all game static variables'''
	def __init__(self):
		self.tile_size = 32
		self.framerate = 36

		#Game Style
		self.text_color = (4,5,8)

		self.screen = Screen(self.tile_size)
		self.golden_map_tile = GoldenMapTile(0,0)


settings = Settings()


from audio_mixer import AudioMixer
from display_box import DisplayBox
from level_map import LevelMap
class ProgramData():
	'''Hold all game program_variables and dynamic variables'''

	def __init__(self):
		'''initialize all attributes'''
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
		#self.dummy_box = DummyBox()
		#self.display_boxes.add(self.dummy_box)

		#Global variables
		self.interaction_obstacle = None

		#Create Objects
		self.audio_mixer = AudioMixer()
		self.level_map = LevelMap()



program_data = ProgramData()





