from states import STATES, DRAW_AS

class Cell(object):

	def __init__(self):
		super(Cell, self).__init__()
		self.state = STATES.DEAD

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		result = []
		if self.state == STATES.ALIVE:
			result.append(DRAW_AS.ALIVE)
		else:
			result.append(DRAW_AS.DEAD)
		return ''.join(result)

	def change_state(self, new_state):
		self.state = new_state

	def flip_state(self):
		if self.state == STATES.ALIVE:
			self.state = STATES.DEAD
		else:
			self.state = STATES.ALIVE