import time
import pygame
from pygame.sprite import Sprite


class Timer(Sprite):
	'''class to define the display box at the bottom of the screen'''
	def __init__(self, settings, requester, target_time):
		super(Timer, self).__init__()
		self.settings = settings
		self.requester = requester
		self.target_time = target_time
		self.last_time = pygame.time.get_ticks()
		self.elapsed_time = 0
		self.paused = False

	def get_elapsed_time(self, current_time):
		self.current_time = current_time
		if self.paused == False:
			self.elapsed_time = self.elapsed_time + (self.current_time - self.last_time)
			self.last_time = self.current_time
		else:
			self.elapsed_time = self.elapsed_time
			self.last_time = self.current_time

		return (self.elapsed_time/1000)

	def reset_timer(self):
		self.elapsed_time = 0

