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
		self.rect_interaction = None
		self.interactable = False

	def interact_with_player(self):
		pass

	def update(self):
		pass
	
	def blitme(self):
		#self.level_map.image.blit(self.image, self.rect)
		self.rect.x = self.x
		self.rect.y = self.y
		self.screen.display.blit(self.image, self.rect)


# This class may not be a necessary abstaction since it may not be different than the parent Obstacle class
class StaticObstacle(Obstacle):
	def __init__(self, settings, screen, level_map, x, y):
		super().__init__(settings, screen, level_map, x, y)


class Desk(StaticObstacle):
	def __init__(self, settings, screen, level_map, x, y):
		super().__init__(settings, screen, level_map, x, y)

		#Load image
		self.image = pygame.image.load('.\\Images\\Objects\\desk.png')
		self.image = pygame.transform.scale(self.image, (55, 40))
		self.rect = self.image.get_rect()

		self.rect_interaction = self.rect.inflate(0, 0)
		self.interactable = True


class Wall(StaticObstacle):
	def __init__(self, settings, screen, level_map, x, y):
		super().__init__(settings, screen, level_map, x, y)
		self.image = pygame.image.load('.\\Images\\Map\\cubicle_wall.png')
		self.rect = self.image.get_rect()

class DynamicObstacle(Obstacle):
	def __init__(self, settings, screen, level_map, x, y, collisions):
		super().__init__(settings, screen, level_map, x, y)
		self.collisions = collisions
		# Character movement states
		self.move_in_progress = False
		self.direction = "none"
		self.speed = 3
		self.animation_count = 0

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		self.movement()

	def movement(self):
		pass

		#Player exact positions
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)


	#Functions to move the Dynamic Obstacle in different directions with corresponding animation
	def move_right(self):
		self.x = self.x + self.speed
		self.image = self.image_right[self.animation_count % 12]
		self.animation_count += 1
		self.direction = "right"

	def move_left(self):
		self.x = self.x - self.speed
		self.image = self.image_left[self.animation_count % 12]
		self.animation_count += 1
		self.direction = "left"

	def move_up(self):
		self.y = self.y - self.speed
		self.image = self.image_up[self.animation_count % 12]
		self.animation_count += 1
		self.direction = "up"

	def move_down(self):
		self.y = self.y + self.speed
		self.image = self.image_down[self.animation_count % 12]
		self.animation_count += 1
		self.direction = "down"

	def check_collisions(self):
		#If player collides with an object rectangle, stop the player from moving in that direction
		collided = False
		self.collisions.remove(self)
		if  pygame.sprite.spritecollide(self, self.collisions, False):
			self.move_back()
			collided = True
		self.collisions.add(self)

		return collided

	def move_back(self):
		if self.direction =="right":
			self.x = self.x - self.speed
		elif self.direction == "left":
			self.x = self.x + self.speed
		elif self.direction == "up":
			self.y = self.y + self.speed
		elif self.direction == "down":
			self.y = self.y - self.speed
	

class GirlNPC(DynamicObstacle):
	def __init__(self, settings, screen, level_map, x, y, collisions):
		super().__init__(settings, screen, level_map, x, y, collisions)

		#Load player image surface and define rectangle
		self.image = pygame.image.load('.\\Images\\Character\\the_girl.png')
		self.image = pygame.transform.scale(self.image, (35, 85))
		self.rect = self.image.get_rect()
		self.rect_interaction = self.rect.inflate(20, 20)
		self.interactable = False




		#First move direction
		self.moving_right = True


	def movement(self):
		# Leaving this as the default DynamicObstacle movement but probably should be changed to something more generic then overwritten in child classes
		self.check_collisions()
		if self.moving_right:
			if self.x < 700:
				self.x = self.x + self.speed
				self.direction ="right"
			else:
				self.moving_right = False
				self.moving_down = True
		elif self.moving_down:
			if self.y < 300:
				self.y = self.y + self.speed
				self.direction ="down"
			else:	
				self.moving_down = False
				self.moving_up = True
		elif self.moving_up:
			if self.y > 100:
				self.y = self.y - self.speed
				self.direction ="up"
			else:
				self.moving_up = False
				self.moving_left = True
		elif self.moving_left:
			if self.x > 500:
				self.x = self.x - self.speed
				self.direction ="left"
			else:
				self.moving_left = False
				self.moving_right = True 
