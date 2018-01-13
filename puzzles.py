from sys import exit
from argparse import ArgumentParser
from random import Random
from static import easy_puzzles, difficult_puzzles

class Puzzles:
	
	def __init__(self):
		self.parser = ArgumentParser()
		self.args = None
		self.rnd = Random()
		self.random_word = None

		self.add_arguments()
		self.select_level()
				
	def add_arguments(self):
		self.parser.add_argument("-e", "--easy", action="store_true",
								help="Draws easy puzzles")
		self.parser.add_argument("-d", "--difficult", action="store_true",
								 help="Draws difficult puzzles")
		self.parser.add_argument("-f", "--file", help="Draws puzzles from file")
		self.args = self.parser.parse_args()
	
	def select_level(self):
		if self.args.file:
			self.word_from_file()
		elif self.args.easy:
			self.easy_word()
		elif self.args.difficult:
			self.difficult_word()
		else:
			print("Word hasn't been drawn")
			exit()

	def file_len(self):
		count = 0
		with open(self.args.file, 'r') as f:
			for line in f:
				count += 1
		return count

	def word_from_file(self):
		try:
			read_file = open(self.args.file, 'r')
		except FileNotFoundError:
			print("Can't find file with puzzles")
			exit()
		size = self.file_len()
		self.random_word = read_file.readlines()[self.rnd.randrange(size)].rstrip()
		read_file.close()
	
	def easy_word(self):
		size = len(easy_puzzles)
		self.random_word = easy_puzzles[self.rnd.randrange(size)]

	def difficult_word(self):
		size = len(difficult_puzzles)
		self.random_word = difficult_puzzles[self.rnd.randrange(size)]
