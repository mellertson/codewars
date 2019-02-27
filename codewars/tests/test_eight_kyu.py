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
