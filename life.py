import os
import sys
from time import sleep
import random


rows, cols = os.popen('stty size', 'r').read().split()
rows = int(rows)-1 # cursor on new line
cols = int(cols) / 2


def enum(**enums):
	return type('Enum', (), enums)

STATES = enum(ALIVE=1, DEAD=0)
DRAW_AS = enum(ALIVE='#', DEAD='-')

class Cell(object):

	def __init__(self):
		super(Cell, self).__init__()
		self.state = STATES.DEAD

	def change_state(self, new_state):
		self.state = new_state

	def flip_state(self):
		if self.state == STATES.ALIVE:
			self.state = STATES.DEAD
		else:
			self.state = STATES.ALIVE

class TwoDArray(object):

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.array = []
		for f in range(width*height):
			self.array.append(None)

	def __iter__(self):
		return iter(self.array)

	def valid_indexes(self, x, y):
		return not( x < 0 or x >= self.width or y < 0 or y >= self.height )

	def get(self, x, y):
		if not self.valid_indexes(x, y):
			raise IndexError('Index out of bounds : (' + str(x) + ', ' + str(y) + ')')
		return self.array[x + self.width*y]

	def set(self, x, y, value):
		if not self.valid_indexes(x, y):
			raise IndexError('Index out of bounds : (' + str(x) + ', ' + str(y) + ')')
		self.array[x + self.width*y] = value

class Life(object):

	def __init__(self, height, width):
		self.area = TwoDArray(width, height)
		self.buffer_area = TwoDArray(width, height)
		self.rows = height
		self.cols = width
		for x in range(self.area.width):
			for y in range(self.area.height):
				self.area.set(x, y, Cell())
				self.buffer_area.set(x, y, Cell())
		# for f in range(width*height):
		# 	self.area.array.append(Cell())
		# 	self.buffer_area.array.append(Cell())

	@staticmethod
	def copy_cells(from_, to):
		for x in range(from_.width):
			for y in range(from_.height):
				to.get(x, y).state = from_.get(x, y).state

	def __repr__(self):
		return self.__str__(self);

	def __str__(self):
		result = []
		for cell in self.area:
			if cell.state == STATES.ALIVE:
				result.append(DRAW_AS.ALIVE)
			else:
				result.append(DRAW_AS.DEAD)
			result.append(' ')
		return ''.join(result)

	def get_alive_neighbours(self, area, x, y):
		neighbours = 0
		for offset_x in range(-1, 2):
			for offset_y in range(-1, 2):
				if offset_x == offset_y == 0:
					continue

				try:
					neighbours += self.area.get(x + offset_x, y + offset_y).state
				except IndexError, e:
					pass

		return neighbours


	def evolve(self):
		Life.copy_cells(self.area, self.buffer_area)

		for cell_num_x in range(self.area.width):
			for cell_num_y in range(self.area.height):
				neighbours = self.get_alive_neighbours(self.area, cell_num_x, cell_num_y)

				curr_cell = self.buffer_area.get(cell_num_x, cell_num_y)

				if neighbours == 3 and curr_cell.state == STATES.DEAD:
					curr_cell.state = STATES.ALIVE
				elif neighbours < 2 and curr_cell.state == STATES.ALIVE:
					curr_cell.state = STATES.DEAD
				elif neighbours > 3 and curr_cell.state == STATES.ALIVE:
					curr_cell.state = STATES.DEAD

		Life.copy_cells(self.buffer_area, self.area)

	def randomize(self):
		for f in self.area:
			if random.random() < 0.2:
				f.state = STATES.ALIVE
			else:
				f.state = STATES.DEAD

	def play(self):
		while 1:
			print
			print self
			self.evolve()

			#for debugging only, comment otherwise
			#sys.exit(0)

			sleep(0.3)

life = Life(rows, cols)
life.randomize()

try:
	life.play()
except KeyboardInterrupt, e:
	pass