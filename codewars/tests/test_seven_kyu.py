import unittest
from codewars.seven_kyu import *


class divisors_Tests(unittest.TestCase):

	def test_should_pass(self):
		self.assertEquals([3, 5], divisors(15))
		self.assertEquals([2, 3, 4, 6], divisors(12))
		self.assertEquals("13 is prime", divisors(13))

	def test_lower_limits(self):
		self.assertEqual('2 is prime', divisors(2))
		self.assertEqual('3 is prime', divisors(3))
		self.assertEqual([2], divisors(4))
		self.assertEqual('5 is prime', divisors(5))
		self.assertEqual([2, 3], divisors(6))
		self.assertEqual('7 is prime', divisors(7))
		self.assertEqual([2, 4], divisors(8))
		self.assertEqual([3], divisors(9))
		self.assertEqual([2, 5], divisors(10))
		self.assertEqual('11 is prime', divisors(11))

	def test_median_range_limits(self):
		self.assertEqual([2, 3, 4, 6, 8, 12], divisors(24))
		self.assertEqual([5], divisors(25))

	def test_upper_limits(self):
		self.assertEqual('104723 is prime', divisors(104723))
		self.assertEqual('104729 is prime', divisors(104729))

