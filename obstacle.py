import pygame
from pygame.sprite import Sprite


class Obstacle(Sprite):
	def __init__(self, settings, screen, level_map, x, y):
		super(Obstacle, self).__init__()
		self.screen = screen
		self.settings = settings
		self.level_map = level_map
		self.x = x
		self.y = y
		self.image = None
		self.rect = None

	def update(self):
		pass
	
	def blitme(self):
		#self.level_map.image.blit(self.image, self.rect)
		self.screen.display.blit(self.image, self.rect)


# This class may not be a necessary abstaction since it may not be different than the parent Obstacle class
class StaticObstacle(Obstacle):
	def __init__(self, settings, screen, level_map, x, y):
		super().__init__(settings, screen, level_map, x, y)

	def blitme(self):
		self.screen.display.blit(self.image, self.rect)

class Desk(StaticObstacle):
	def __init__(self, settings, screen, level_map, x, y):
		super().__init__(settings, screen, level_map, x, y)

		#Load image
		self.image = pygame.image.load('.\\Images\\Objects\\desk.png')
		self.image = pygame.transform.scale(self.image, (55, 40))
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.rect
		
		#position
		self.rect.x = self.x
		self.rect.y = self.y

class Wall(StaticObstacle):
	def __init__(self, settings, screen, level_map, x, y):
		super().__init__(settings, screen, level_map, x, y)
		self.image = pygame.image.load('.\\Images\\Map\\cubicle_wall.png')
		self.rect = self.image.get_rect()

		#position
		self.rect.x = self.x
		self.rect.y = self.y

class DynamicObstacle(Obstacle):
	def __init__(self, settings, screen, level_map, x, y):
		super().__init__(settings, screen, level_map, x, y)

		# Character movement states
		self.move_in_progress = False
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.colliding = False

	def update(self):
		self.movement()

	def movement(self):
		# Leaving this as the default DynamicObstacle movement but probably should be changed to something more generic then overwritten in child classes
		if self.moving_right:
			if self.rect.x < 700:
				self.x += self.settings.character_speed
			else:
				self.moving_right = False
				self.moving_down = True
		elif self.moving_down:
			if self.y < 300:
				self.y += self.settings.character_speed
			else:	
				self.moving_down = False
				self.moving_up = True
		elif self.moving_up:
			if self.y > 100:
				self.y -= self.settings.character_speed
			else:
				self.moving_up = False
				self.moving_left = True
		elif self.moving_left:
			if self.x > 500:
				self.x -= self.settings.character_speed
			else:
				self.moving_left = False
				self.moving_right = True 
		self.rect.x = int(self.x)
		self.rect.y = int(self.y)

class GirlNPC(DynamicObstacle):
	def __init__(self, settings, screen, level_map, x, y):
		super().__init__(settings, screen, level_map, x, y)
		#Character movement states
		self.move_in_progress = False
		self.moving_right = True
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.colliding = False

		#Load player image surface and define rectangle
		self.image = pygame.image.load('.\\Images\\Character\\the_girl.png')
		self.image.set_alpha(255)

		self.image = pygame.transform.scale(self.image, (35, 85))
		self.rect = self.image.get_rect()
		self.rect.x = 500
		self.rect.y = 100

		#NPC exact position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)