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
