import pygame
import time
import audio_mixer as am

class BattleArena():
	'''class to define the battle arena'''
	def __init__(self, program_data, screen, audio_mixer):
		self.program_data = program_data
		self.screen = screen
		self.audio_mixer = audio_mixer

		self.backgorund_color = (240, 240, 240)


	def blitme(self):
		pass