from ConfigParser import RawConfigParser
import os

class LifeCFGParser(object):

	def __init__(self, filenames):
		self.parser = RawConfigParser()
		self.set_defaults()
		self.read_cfg(filenames)
		for section in self.sections:
			self.__dict__.update(self.parser.items(section))

	def set_defaults(self):
		self.parser.add_section('TextRenderer')

		self.parser.set('TextRenderer', 'alive_cell', '#')
		self.parser.set('TextRenderer', 'dead_cell', '-')
		self.parser.set('TextRenderer', 'whitespace_after_cell', 'true')

		self.parser.add_section('LifeGame')
		self.parser.set('LifeGame', 'evolve_interval', 0.3)
		self.parser.set('LifeGame', 'random_alive_chance', 0.2)

		self.sections = self.parser.sections()

	def read_cfg(self, filenames):
		# print 'Reading file(s) ' + str(filenames) + '!'
		return self.parser.read(filenames)

	def write_cfg(self, filed):
		self.parser.write(filed)

config = LifeCFGParser(['life.cfg'])