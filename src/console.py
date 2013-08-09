import os
from terminal import getTerminalSize

class Console(object):

	def __init__(self):
		self.cols, self.rows = getTerminalSize()
		print "rows %i" % self.rows
		print "cols %i" % self.cols
		self.rows = int(self.rows)
		self.cols = int(self.cols)

	def get_rows(self):
		return self.rows

	def get_cols(self):
		return self.cols