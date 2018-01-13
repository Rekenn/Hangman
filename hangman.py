from static import GALLOWS

class Hangman:

	def __init__(self, hidden_word):
		self.CHANCES = len(GALLOWS) - 1
		self.miss = 0
		self.hidden_word = hidden_word
		self.win = set(hidden_word)
		self.letters = set()
		self.failed_letters = set()
	
	def draw_word(self):
		for i in range(len(self.hidden_word)):
			if self.hidden_word[i] in self.letters:
				print(self.hidden_word[i], end='')
			elif self.hidden_word[i] == ' ':
				print(' ', end='')
			else:
				print('_', end='')
		print()
	
	def draw_failed_letters(self):
		print("Failed letters: ", end='')
		for i in self.failed_letters:
			print(i, end=' ')
		print()

	def draw_gallows(self):
		print(GALLOWS[self.miss])

	def input_letter(self):
		letter = input("Write letter ").lower()
		if self.letter_in_word(letter) and self.check_letter_length(letter):
			self.letters.add(letter)
		elif self.letter_not_in_word(letter) and self.check_letter_length(letter):
			self.failed_letters.add(letter)
			self.miss += 1
	
	def letter_in_word(self, letter):
		return letter in self.hidden_word

	def check_letter_length(self, letter):
		return not len(letter) > 1

	def letter_not_in_word(self, letter):
		return not letter in self.failed_letters

	def is_won(self):
		return self.letters == self.win
