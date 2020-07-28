import pygame
import time

class DisplayBox():
	'''class to define the display box at the bottom of the screen'''
	def __init__(self, settings, screen):
		self.settings = settings
		self.screen = screen
		
		#Font settings
		self.text_color = (4,65,33)
		self.font = pygame.font.SysFont('calibri', 20)

		self.color = (240, 240, 240)

		#Default display box locations
		self.width = self.screen.rect.width
		self.height = self.settings.tile_size*3
		self.left = self.screen.rect.left
		self.top = self.screen.rect.bottom - self.height
		self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

		self.response_width = self.screen.rect.width/2
		self.response_height = self.settings.tile_size*2
		self.response_left = self.screen.rect.right - self.response_width
		self.response_top = self.screen.rect.bottom - self.settings.tile_size*5

		self.rect_response = pygame.Rect(self.response_left , self.response_top, self.response_width, self.response_height)

		#Use the ";" character to indicate a break in the sentence. 
		#All breaks will clear the display box and start displaying after the break
		self.messages = {
		'intro' : "hello the_Guy", 
		'NPC_girl' : "Did you hear Bob and Karren went fishing last weekend?",
		'desk' : "This is my desk",
		'item_report_1' : "You found a level 1 BitCorp Report!",
		'coffee_machine' : "Enjoy your brew! ; The Guy drank his coffee and is feeling ready to work."
		}
		self.message_to_write = "Hello the_Guy"


		#Dynamic Attributes
		self.visible = False
		self.character_line_limit = 30
		self.message_key = 'intro'
		self.message_type = "default"
		self.response_options = ["Yes", "No"]
		self.response_messages = ["A", "B"]

		

	def prep_message(self):
		print("hi")
		#Reset display box, and counters and prep it for displaying the message
		self.message_to_write = self.messages.get(self.message_key)
		self.word_list = self.message_to_write.split()
		self.responses_number = len(self.response_options)
		self.response_line = 1
		self.reset_display_box_variables()
		
	def reset_display_box_variables(self):
		self.clear_lines()
		self.word_count = 0
		self.char_count = 0
		self.blit_count = 0
		self.blit_count_counter = 0

		#States of the message being written
		self.main_message_done = False
		self.message_sequence_done = False
		self.typing = False
		self.switching_lines = False
		self.switching_lines_count = 0

		#States of key preses for the display box
		self.down_press = False
		self.up_press = False

	def clear_lines(self):
		self.line1 = ""
		self.line1_words_only = ""
		self.line2 = ""	
		self.line2_words_only = ""
		self.line1_temp = ""
		self.line2_temp = ""
		self.current_active_line = 1
		self.clear_on_click = False

		
	def blitme(self):
		pygame.draw.rect(self.screen.display, self.color, self.rect)
		#print(self.main_message_done)

		if not self.main_message_done:
			if self.switching_lines:
				self.switching_lines_count +=1
				self.switch_lines()

			else:
				#itterate through all words in the message
				if self.word_count < (len(self.word_list)):
					self.current_word = self.word_list[self.word_count]
				else:
					self.main_message_done = True
					self.blit_lines()
					return
				
				#Handle message break character
				if self.current_word == ";":
					self.clear_on_click = True
					self.word_count += 1
					self.typing = False
					self.blit_lines()
					self.blit_next_arrow()
					return

				elif not self.clear_on_click:
					if self.current_active_line == 1:
						self.fill_line1()
						
					else:
						self.current_active_line = 2
						self.fill_line2()
		else:
			self.typing = False
			#Trigger a response if it is a reponsive type message
			if not self.message_sequence_done:
				if self.message_type == "responsive":
					pygame.draw.rect(self.screen.display, self.color, self.rect_response)
					self.blit_response()
					self.blit_response_arrow()
					if self.up_press:
						if self.response_line == 1:
							pass
						else:
							self.response_line -=1

					if self.down_press:
						if self.response_line == self.responses_number:
							pass
						else:
							self.response_line +=1
				else:
					self.message_sequence_done = True

		self.blit_lines()


	def fill_line1(self):
		if len(self.line1_words_only + self.current_word) <= self.character_line_limit:
			#Check if there are more characters in the given word
			if self.char_count < len(self.current_word):
				self.line1 += (self.current_word[self.char_count])
				self.char_count += 1
				self.typing = True
			else:
				self.line1_words_only = self.line1
				self.line1 += " "
				self.char_count = 0
				self.word_count += 1
		else:
			self.current_active_line = 2
			self.char_count = 0

	def fill_line2(self):
		if len(self.line2_words_only + self.current_word) <= self.character_line_limit:
			#Check if there are more characters in the given word
			if self.char_count < len(self.current_word):
				self.line2 += (self.current_word[self.char_count])
				self.char_count += 1
				self.typing = True
			else:
				self.line2_words_only = self.line2
				self.line2 += " "
				self.char_count = 0
				self.word_count += 1
		else:
			self.char_count = 0
			self.typing = False

	def switch_lines(self):
		self.switching_lines = True	
		if self.switching_lines_count == 0:
			self.line1_temp = self.line1
			self.line1 = ""
			self.line1_words_only = ""
			self.line2_temp = self.line2
			self.line2 = ""
			self.line2_words_only = ""
		elif self.switching_lines_count > 3:
			self.line1_temp = ""
			self.line1 = self.line2_temp
			self.line2_temp = ""
			self.switching_lines_count = 0
			self.switching_lines = False
		self.blit_lines()



	def blit_lines(self):
		#blit line1 and line2 to the screen on the screen
		self.line1_image = self.font.render(self.line1, True, self.text_color, self.color)
		self.line1_rect = self.line1_image.get_rect()
		self.line1_rect.left = self.rect.left + 5
		self.line1_rect.centery = self.rect.centery - self.rect.height/5
		self.screen.display.blit(self.line1_image, self.line1_rect)

		self.line2_image = self.font.render(self.line2, True, self.text_color, self.color)
		self.line2_rect = self.line2_image.get_rect()
		self.line2_rect.left = self.rect.left + 5
		self.line2_rect.centery = self.rect.centery + self.rect.height/5
		self.screen.display.blit(self.line2_image, self.line2_rect)

		self.line1_temp_image = self.font.render(self.line1_temp, True, self.text_color, self.color)
		self.line1_temp_rect = self.line1_temp_image.get_rect()
		self.line1_temp_rect.left = self.rect.left + 5
		self.line1_temp_rect.centery = self.rect.centery - self.rect.height/3
		self.screen.display.blit(self.line1_temp_image, self.line1_temp_rect)

		self.line2_temp_image = self.font.render(self.line2_temp, True, self.text_color, self.color)
		self.line2_temp_rect = self.line2_temp_image.get_rect()
		self.line2_temp_rect.left = self.rect.left + 5
		self.line2_temp_rect.centery = self.rect.centery
		self.screen.display.blit(self.line2_temp_image, self.line2_temp_rect)	

		if not self.typing and self.main_message_done == False:
			self.blit_next_arrow()	

	def blit_next_arrow(self):
		self.arrow_images = [pygame.image.load('.\\Images\\Misc\\down_arrow.png'), pygame.image.load('.\\Images\\Misc\\down_arrow.png'), pygame.image.load('.\\Images\\Misc\\down_arrow2.png')]
		#self.arrow_images = [pygame.image.load('.\\Images\\Misc\\down_arrow.png'), pygame.image.load('.\\Images\\Misc\\down_arrow.png'), pygame.image.load('.\\Images\\Misc\\down_arrow.png'), pygame.image.load('.\\Images\\Misc\\down_arrow.png'), pygame.image.load('.\\Images\\Misc\\down_arrow2.png'), pygame.image.load('.\\Images\\Misc\\down_arrow2.png'), pygame.image.load('.\\Images\\Misc\\down_arrow2.png'), pygame.image.load('.\\Images\\Misc\\down_arrow2.png')]
		self.blit_count_counter +=1 
		if self.blit_count_counter % 12 ==0:
			self.blit_count += 1
		self.arrow_image = self.arrow_images[self.blit_count%3]

		self.arrow_rect = self.arrow_image.get_rect()
		self.arrow_rect.left = self.rect_response.right - 30
		self.arrow_rect.centery = self.rect.bottom - 15
		self.screen.display.blit(self.arrow_image, self.arrow_rect)

	def blit_response(self):
		self.option_count = 0
		for opt in self.response_options:
			self.option_count += 1
			self.line_image = self.font.render(opt, True, self.text_color, self.color)
			self.line_rect = self.line_image.get_rect()
			self.line_rect.left = self.rect_response.left + 20
			self.line_rect.centery = self.rect_response.top + self.rect_response.height*self.option_count/3 
			self.screen.display.blit(self.line_image, self.line_rect)

	def blit_response_arrow(self):
		self.arrow_image = pygame.image.load('.\\Images\\Misc\\right_arrow.png')

		self.arrow_rect = self.arrow_image.get_rect()
		self.arrow_rect.left = self.rect_response.left + 5
		self.arrow_rect.centery = self.rect_response.top + self.rect_response.height/3 *self.response_line
		self.screen.display.blit(self.arrow_image, self.arrow_rect)

	def run_response(self):
		self.reset_display_box_variables()
		self.message_type = "default"
		self.message_to_write = self.response_messages[self.response_line - 1]
		self.word_list = self.message_to_write.split()


