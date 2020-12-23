import pygame
import math
from program_variables import settings

def round_to_tileset(value_to_round):
	return settings.tile_size * round(value_to_round / settings.tile_size)

