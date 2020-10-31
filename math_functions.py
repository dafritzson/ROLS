import pygame
import math

def round_to_tileset(value_to_round, program_data):
	return program_data.tile_size * round(value_to_round / program_data.tile_size)

