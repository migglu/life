from states import STATES
from configparser import config

class Cell(object):

	def __init__(self):
		super(Cell, self).__init__()
		self.state = STATES.DEAD

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		result = []
		if self.state == STATES.ALIVE:
			result.append(config.alive_cell)
		else:
			result.append(config.dead_cell)
		return ''.join(result)

	def set_alive(self):
		self.state = STATES.ALIVE

	def set_dead(self):
		self.state = STATES.DEAD

	def is_alive(self):
		return self.state == STATES.ALIVE

	def is_dead(self):
		return not self.is_alive()

	def set_state(self, new_state):
		self.state = new_state

	def get_state(self):
		return self.state

	def flip_state(self):
		if self.state == STATES.ALIVE:
			self.state = STATES.DEAD
		else:
			self.state = STATES.ALIVE