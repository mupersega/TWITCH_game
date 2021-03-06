import pygame
import random


class Explosion:
	"""A class to manage explosion objects consisting of n particles. Particles are managed in arrays in this class, NOT
	as their own instantiated objects."""
	def __init__(self, game, position, size, rgb, inherited_velocity=None):
		self.game = game
		self.location = position
		self.size = size
		self.inherited_velocity = inherited_velocity or pygame.Vector2(0, 0)
		self.particles = []
		self.vecs = []
		self.cycle = 0
		self.rgb = rgb

		self.create_particles()

	def create_particles(self):
		# set particle sizes
		for _ in range(self.size):
			self.particles.append(random.randint(1, self.size))
		# set their magnitudes
		for i in range(self.size):
			self.vecs.append(pygame.Vector2(
				random.uniform(-.5, .5)*(self.size-self.particles[i]),
				random.uniform(-.5, .5)*(self.size-self.particles[i])
			) - self.inherited_velocity * .4)

	def draw(self):
		for i in range(self.size):
			pygame.draw.circle(self.game.screen, self.rgb, self.location + (self.vecs[i] * self.cycle), self.particles[1])

	def loop(self):
		if self.cycle > self.size * 5 and self in self.game.explosions.copy():
			self.game.explosions.remove(self)
		self.cycle += 1
		if self.cycle % 4 == 0:
			for i in range(self.size):
				self.particles[i] -= 1
		self.draw()

