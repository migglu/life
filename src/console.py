import os

class Console(object):

	def __init__(self):
		self.rows, self.cols = os.popen('stty size', 'r').read().split()
		self.rows = int(self.rows)
		self.cols = int(self.cols)

	def get_rows(self):
		return self.rows

	def get_cols(self):
		return self.cols