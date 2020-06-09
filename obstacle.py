import pygame
from pygame.sprite import Sprite


class Obstacle(Sprite):
	def __init__(self, screen, settings, x, y):
		super(Obstacle, self).__init__()
		self.screen = screen
		self.settings = settings
		self.x = x
		self.y = y

		self.image = None
		self.rect = None

		#position
		self.rect.x = self.x
		self.rect.y = self.y

# This class may not be a necessary abstaction since it may not be different than the parent Obstacle class
class StaticObstacle(Obstacle):
	def __init__(self, screen, settings, x, y):
		super().__init__(screen, settings, x, y)

		#Load Image
		self.image = None
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

	def blitme(self):
		self.screen.blit(self.image, self.rect)

class Desk(StaticObstacle):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)

        #Load image
        self.image = pygame.image.load('.\\Images\\Objects\\desk.png')
        self.image = pygame.transform.scale(self.image, (110, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

class Wall(StaticObstacle):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        self.image = pygame.image.load('.\\Images\\Map\\cubicle_wall.png')
        self.rect = self.image.get_rect()

class DynamicObstacle(Obstacle):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)

		#***Why is display_box needed for an NPC class?***
        # self.display_box = display_box

		# Character movement states
        self.move_in_progress = False
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.colliding = False

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

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class GirlNPC(DynamicObstacle):
    def __init__(self, screen, settings, x, y):
        super().__init__(screen, settings, x, y)
        #Character movement states
        self.move_in_progress = False
        self.moving_right = True
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.colliding = False

        #Load player image surface and define rectangle
        self.image = pygame.image.load('.\\Images\\Character\\the_girl.png')
        self.image = pygame.transform.scale(self.image, (35, 85))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.x = 500
        self.rect.y = 100

        #NPC exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)