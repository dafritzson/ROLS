import pygame
import sys
pygame.init()
pygame.display.set_caption("Real Office Life Simulator")
self.image = pygame.image.load('.\\Images\\Map\\cubicle_wall.png')
self.rect = self.image.get_rect()
flag = True
while flag:
	event_list = pygame.event.get()

	for event in event_list:
		if event.type == pygame.QUIT:
			sys.exit()
