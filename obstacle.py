import random
import pygame
from pygame.sprite import Sprite

random.seed()

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
		self.interaction_side = "up"

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
		self.moving_back = False
		self.direction = "right"
		self.speed = 3
		self.animation_count_f = 0
		self.animation_count_b = 0

		self.finishing_animation = False
		self.collided = False

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		self.image_left = [pygame.image.load('.\\Images\\Player\\Walk_Left\\left1.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left1.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Left\\left1.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left2.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left2.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Left\\left2.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left3.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left3.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Left\\left3.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left4.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left4.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Left\\left4.png')]

		self.image_right = [pygame.image.load('.\\Images\\Player\\Walk_Right\\right1.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right1.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Right\\right1.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right2.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right2.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Right\\right2.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right3.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right3.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Right\\right3.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right4.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right4.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Right\\right4.png')]

		self.image_up = [pygame.image.load('.\\Images\\Player\\Walk_Up\\up1.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up1.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Up\\up1.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up2.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up2.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Up\\up2.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up3.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up3.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Up\\up3.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up4.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up4.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Up\\up4.png')]

		self.image_down = [pygame.image.load('.\\Images\\Player\\Walk_Down\\down1.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down1.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Down\\down1.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down2.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down2.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Down\\down2.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down3.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down3.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Down\\down3.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down4.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down4.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Down\\down4.png')]


	def update(self):
		self.movement()

	def movement(self):
		pass


	#Functions to move the Dynamic Obstacle in different directions with corresponding animation
	def move_right(self):
		self.x = self.x + self.speed
		self.image = self.image_right[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "right"

	def move_left(self):
		self.x = self.x - self.speed
		self.image = self.image_left[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "left"

	def move_up(self):
		self.y = self.y - self.speed
		self.image = self.image_up[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "up"

	def move_down(self):
		self.y = self.y + self.speed
		self.image = self.image_down[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "down"

	def check_collisions(self):
		#If player collides with an object rectangle, stop the player from moving in that direction
		self.collided = False
		self.collisions.remove(self)
		if  pygame.sprite.spritecollide(self, self.collisions, False):
			self.move_back()
			self.moving_back = True
			self.collided = True
		self.collisions.add(self)

	def move_back(self):
		self.animation_count_b += 1
		if self.direction =="right":
			self.x = self.x - self.speed
			self.image = self.image_right[self.animation_count_b % 12]

		elif self.direction == "left":
			self.x = self.x + self.speed
			self.image = self.image_left[self.animation_count_b % 12]

		elif self.direction == "up":
			self.y = self.y + self.speed
			self.image = self.image_up[self.animation_count_b % 12]

		elif self.direction == "down":
			self.y = self.y - self.speed
			self.image = self.image_down[self.animation_count_b % 12]
	
	def finish_animation(self):
		#Finish the animation for all movements. Only run after a keyup ends the player movement.
		if (self.direction == "right" or self.direction == "left") and self.rect.x % 8 != 0:
			if self.moving_back:
				self.move_back()
			elif self.direction == "right" and not self.collided:
				self.move_right()
			elif self.direction == "left" and not self.collided:
				self.move_left()
		elif (self.direction == "up" or self.direction == "down") and self.rect.y % 8 != 0:
			if self.moving_back:
				self.move_back()
			elif self.direction == "up" and not self.collided:
				self.move_up()
			elif self.direction == "down" and not self.collided:
				self.move_down()
		
		else:
			self.finishing_animation = False
			self.moving_back = False

class NPC(DynamicObstacle):
	def __init__(self, settings, screen, level_map, x, y, collisions, move_width, move_height):
		super().__init__(settings, screen, level_map, x, y, collisions)
		self.move_width = move_width
		self.move_height = move_height

		#Load player image surface and define rectangle
		self.image = pygame.image.load('.\\Images\\Character\\the_girl.png')
		self.image = pygame.transform.scale(self.image, (35, 85))
		self.rect = self.image.get_rect()
		self.rect_interaction = self.rect.inflate(20, 20)
		self.interactable = False
		self.speed = 1

		#First move direction
		self.moving_right = True


	def change_direction(self):
		x = {"right": 0 ,"left":1, "up":2, "down":3}
		rand_num = random.randint(1,3)
		#print(x.get(self.direction))
		num = (x.get(self.direction) + rand_num) % 4
		key_list = list(x.keys()) 
		val_list = list(x.values()) 
		self.direction = key_list[val_list.index(num)]


	def movement(self):
		# Leaving this as the default DynamicObstacle movement but probably should be changed to something more generic then overwritten in child classes
		self.check_collisions()
		rand_num = random.randint(1,100)

		#60% chance to stay still
		if rand_num<=60:
			pass
		#30% chance of moving in the same direction
		elif rand_num <= 90:
			
			if self.direction == "right":
				self.move_right()
			elif self.direction == "left":
				self.move_left()
			elif self.direction == "up":
				self.move_up()
			elif self.direction == "down":
				self.move_down()
		else:
			self.change_direction()

		if self.direction == "right":
			self.move_right()
		elif self.direction == "left":
			self.move_left()
		elif self.direction == "up":
			self.move_up()
		elif self.direction == "down":
			self.move_down()


