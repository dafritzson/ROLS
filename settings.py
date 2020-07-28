import time
class Settings():
	'''Hold all settings and back-end variables of the game'''

	def __init__(self):
		'''initialize all attributes'''

		self.bg_color = (3,181,133)
		self.tile_size = 32
		self.framerate = 36

		#Game Style
		self.text_color = (4,5,8)


		#Game State
		self.game_state = "main menu"
		self.game_states = ["main menu", "run", "game menu", "close"]
		self.game_paused = False









