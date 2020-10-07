import pygame
import math

def round_to_tileset(value_to_round, settings):
	return settings.tile_size * round(value_to_round / settings.tile_size)

