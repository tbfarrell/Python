import sys

import pygame

from Settings import settings

class AlienInvasion:
	"""Da overall class to manage game assets and general behavior """

	def __init__(self):
		"""initialize the game, create resources"""
		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))

		self.screen = pygame.display.set_mode((1200,800))
		pygame.display.set_caption("AlienInvasion")

		#background color
		self.bg_color = (255, 23, 0)

	def run_game(self):
		""" start the primary game loop."""
		while True:
			#watch for keyboard/mouse input

			#make exit button(?)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

					#make the most recently drawn screen visible.
					pygame.display.flip()

		for event in pygame.event.get():
			if event.type == pygame.QUIT():
				sys.exit()

		#redraw screen with each pass through the loop
		self.screen.fill(self.bg_color)

if __name__ == '__main__':
	#make a game instance and run it.
	ai = AlienInvasion()
	ai.run_game()
	