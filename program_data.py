import time
class ProgramData():
	'''Hold all program_variables and back-end variables of the game'''

	def __init__(self):
		'''initialize all attributes'''

		self.tile_size = 32
		self.framerate = 36

		#Game Style
		self.text_color = (4,5,8)


		#Game State
		self.game_state = "main menu"
		self.game_states = ["main menu", "run", "game menu", "battle" "close"]
		self.game_paused = False

		#General Counters
		self.arrow_value = 1









