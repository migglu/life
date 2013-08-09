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
	def copy_cells(from_, to_):
		for x in range(from_.width):
			for y in range(from_.height):
				to_.get(x, y).set_state(from_.get(x, y).get_state())

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
					current_cell = self.area.get(x + offset_x, y + offset_y)
					if current_cell.is_alive():
						neighbours += 1
				except IndexError, e:
					pass

		return neighbours


	def evolve(self):
		Life.copy_cells(self.area, self.buffer_area)

		for cell_num_x in range(self.area.width):
			for cell_num_y in range(self.area.height):
				neighbours = self.get_alive_neighbours(self.area, cell_num_x, cell_num_y)

				curr_cell = self.buffer_area.get(cell_num_x, cell_num_y)

				if ( neighbours == 3 and curr_cell.is_dead() ) or ( curr_cell.is_alive() and ( neighbours < 2 or neighbours > 3 ) ):
					curr_cell.flip_state()

		Life.copy_cells(self.buffer_area, self.area)

	def randomize(self):
		for cell in self.area:
			if random.random() < 0.2:
				cell.set_alive()
			else:
				cell.set_dead()

	def play(self):
		while 1:
			print
			print self
			self.evolve()

			#for debugging only, comment otherwise
			#sys.exit(0)

			sleep(0.3)
