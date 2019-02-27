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
			'ehT kciuq nworb xof spmuj revo eht yzal .god',
			reverse_words('The quick brown fox jumps over the lazy dog.'))
		self.assertEqual(
			'elppa',
			reverse_words('apple'))
		self.assertEqual(
			'a b c d',
			reverse_words('a b c d'))
		self.assertEqual(
			'elbuod  decaps  sdrow',
			reverse_words('double  spaced  words'))

	def test_anagram(self):
		self.assertEqual(
			'desserts stressed',
			reverse_words('stressed desserts'))





