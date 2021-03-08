import pygame

import cfg
from class_hangar import Hangar
from class_location import Location


class Station:
	"""Station object containing and positioning player bays and hangars."""
	def __init__(self, game, station_number, hangars=cfg.default_hangars):
		# First station needs to init as num 0
		self.game = game
		self.screen = game.screen
		self.on_screen = True
		self.sn = station_number
		if self.sn == 0:
			self.hangar_count = 20
		else:
			self.hangar_count = 6
		self.kind = 'station'
		self.x = cfg.st_x_offset + self.sn * cfg.station_spacing
		self.y = cfg.st_y_offset
		self.width = cfg.station_width
		self.height = cfg.y_pad + (self.hangar_count * (
			cfg.y_pad + cfg.facility_h))
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.rgb = cfg.st_colour
		self.dock_location = Location((self.rect.right + (
			cfg.facility_w * 7), self.rect.bottom + 20))
		self.approach_velocity = False

		# iterables
		self.hangars = []
		self.hold = []

		self.station_setup()

	def station_setup(self):
		# construct i hangars
		if self.sn == 0:
			h = 20
		else:
			h = 6
		for i in range(h):
			self.new_hangar()

	def new_hangar(self):
		new_hangar = Hangar(self, len(self.hangars))
		self.hangars.append(new_hangar)

	def draw(self):
		pygame.draw.rect(self.screen, self.rgb, self.rect)

	def loop(self):
		self.draw()
