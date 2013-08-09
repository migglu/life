from states import STATES, DRAW_AS
from cell import Cell
from twodarray import TwoDArray
from time import sleep
import random

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
			result.append(str(cell))
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
