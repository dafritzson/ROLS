import pygame

class AudioMixer():
	def __init__(self, settings):
		self.settings = settings
		pygame.mixer.init()


		self.sound_library = {
		'main_theme' : ".\\Audio\\Elevator Music.mp3",
		'sound_report' : ".\\Audio\\Item.wav",
		'sound_display_box' : ".\\Audio\\Display Box.wav"
		}
		self.audio_key = 'sound_report'
		self.sound_to_play = pygame.mixer.Sound(self.sound_library.get(self.audio_key))

	def load_sound(self):
		self.loaded_sound = self.sound_library.get(self.audio_key)
		self.sound_to_play = pygame.mixer.Sound(self.loaded_sound)

	def play_sound(self,):
		pygame.mixer.Sound.play(self.sound_to_play)

	def play_music(self):
		pygame.mixer.music.set_volume(0.1)
		self.song_to_play = self.sound_library.get(self.audio_key)
		pygame.mixer.music.load(self.song_to_play)
		pygame.mixer.music.play(-1)

	def stop_music(self):
		pygame.mixer.music.stop()
