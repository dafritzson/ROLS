class Settings():
	'''Hold all settings and back-end variables of the game'''

	def __init__(self):
		'''initialize all attributes'''
		self.screen_width =  800
		self.screen_height = 512
		self.bg_color = (3,181,133)
		self.tile_size = 16
		self.framerate = 1
		self.character_move_distance = 1
		self.character_move_block = 5
		#Charcter Settings
		self.character_speed = 0.08

		
		#Menu settings
		self.menu_color = (255, 255, 255)

		#Game Style
		self.text_color = (4,5,8)

		#Loop_counter
		self.loop_count = 0

		#Game State
		self.game_state = "main menu"
		self.game_states = ["main menu", "run", "game menu", "close"]

		#level1_map
		level1_map_tiles=3







