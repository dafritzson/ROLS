import sys
from time import sleep
import pygame

sound_library = {
'main_theme' : ".\\Audio\\Elevator Music.mp3",
'sound_report' : ".\\Audio\\Item.wav",
'sound_display_box' : ".\\Audio\\Display Box.wav"
}

def play_sound(sound):
	sound_to_play = sound_library.get(sound)
	pygame.mixer.Sound.play(pygame.mixer.Sound(sound_to_play))
	pygame.mixer.stop

def play_music(song):
	pygame.mixer.music.set_volume(0.1)
	song_to_play = sound_library.get(song)
	pygame.mixer.music.load(song_to_play)
	pygame.mixer.music.play(-1)
