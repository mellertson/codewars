import unittest
from codewars.eight_kyu import *


class toJadenCase_Tests(unittest.TestCase):

	def test_should_pass(self):
		# setup
		quote = "How can mirrors be real if our eyes aren't real"

		# test
		r = toJadenCase(quote)

		# verify
		self.assertEqual(r, "How Can Mirrors Be Real If Our Eyes Aren't Real")


class reverse_words_Tests(unittest.TestCase):
	
	def test_should_pass(self):
		self.assertEqual(
			reverse_words('The quick brown fox jumps over the lazy dog.'),
			'ehT kciuq nworb xof spmuj revo eht yzal .god')
		self.assertEqual(
			reverse_words('apple'),
			'elppa')
		self.assertEqual(
			reverse_words('a b c d'),
			'a b c d')
		self.assertEqual(
			reverse_words('double  spaced  words'),
			'elbuod  decaps  sdrow')




