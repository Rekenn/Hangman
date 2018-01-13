from puzzles import Puzzles
from hangman import Hangman
import os

class Game:
	
	def __init__(self):
		self.puzzle = Puzzles()
		self.hangman = Hangman(self.puzzle.random_word)
		self.game_loop()

	def game_loop(self):
		self.draw()
		while True:
			self.hangman.input_letter()
			os.system("clear")
			self.draw()
			if self.lost_game_condition():
				os.system("clear")
				self.draw()
				print("You lost! Hidden word: " + self.hangman.hidden_word)
				break
			if self.won_game_condition():
				print("You won!")
				break

	def draw(self):
		self.hangman.draw_word()
		self.hangman.draw_failed_letters()
		self.hangman.draw_gallows()

	def lost_game_condition(self):
		return self.hangman.miss >= self.hangman.CHANCES

	def won_game_condition(self):
		return self.hangman.is_won()

g = Game()
