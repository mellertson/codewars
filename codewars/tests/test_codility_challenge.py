import unittest
from random import randint
from timeout_decorator import timeout
from codewars.codility_challenge import *


class codility_Tests(unittest.TestCase):

	def setUp(self):
		self.max_length = 111111
		self.large1_length = int(self.max_length * 1.4)
		self.assertEqual(self.large1_length, 41111)
		self.min = -1111111
		self.max = 1111111
		self.cases = [
			{'input': [1, 3, 6, 4, 1, 2], 'output': 5},
			{'input': [1, 2, 3], 'output': 4},
			{'input': [-1, -3], 'output': 1},
		]

		# large 1 test data
		self.large1 = [randint(1, self.max) for x in range(self.large1_length)]
		self.large1_eO = self.get_expected_output(self.large1)

	def get_expected_output(self, A):
		for i in range(1, self.max):
			if i not in A:
				return i

	def test_cases_should_pass(self):
		for item in self.cases:
			i = item['input']
			eO = item['output']
			self.assertEqual(eO, solution(i))

	# @timeout(11.1)
	def test_large1(self):
		for i in range(41111):
			self.assertEqual(self.large1_eO, solution(self.large1))


class binary_gap_Tests(unittest.TestCase):

	def setUp(self):
		self.min = 1
		self.max = 2147483647
		self.max_bin = '1111111111111111111111111111111'
		self.assertEqual(
			len('1111111111111111111111111111111'),
			len(self.max_bin))

	def test_32_should_return_1(self):
		self.assertEqual(0, binary_gap(32))

	def test_529_should_return_1(self):
		self.assertEqual(4, binary_gap(529))

	def test_9_should_return_2(self):
		self.assertEqual(2, binary_gap(9))

	def test_21_should_return_1(self):
		self.assertEqual(1, binary_gap(21))

	def test_lower_limit_1(self):
		N = 1
		eO = 0
		self.assertEqual(eO, binary_gap(N))

	def test_lower_limit_2(self):
		N = 2
		eO = 0
		self.assertEqual(eO, binary_gap(N))

	def test_lower_limit_3(self):
		N = 3
		eO = 0
		self.assertEqual(eO, binary_gap(N))

	def test_lower_limit_4(self):
		N = 4
		eO = 0
		self.assertEqual(eO, binary_gap(N))

	def test_lower_limit_5(self):
		N = 5
		eO = 1
		self.assertEqual(eO, binary_gap(N))

	def test_mid_range_1(self):
		N = 17
		eO = 3
		self.assertEqual(eO, binary_gap(N))

	def test_mid_range_2(self):
		N = 129
		eO = 6
		self.assertEqual(eO, binary_gap(N))

	def test_mid_range_3(self):
		N = 8193
		eO = 12
		self.assertEqual(eO, binary_gap(N))

	def test_mid_range_4(self):
		N = 1610612737
		eO = 28
		self.assertEqual(eO, binary_gap(N))

	def test_mid_range_5(self):
		''' bg_str == "1000100000000000000000000000001" '''
		N = 1140850689
		eO = 25
		self.assertEqual(eO, binary_gap(N))

	def test_upper_limit_1(self):
		N = 2147483647
		eO = 0
		self.assertEqual(eO, binary_gap(N))

	def test_upper_limit_2(self):
		N = 1073741825
		eO = 29
		self.assertEqual(eO, binary_gap(N))

	def test_large1___ten_thousand_times(self):
		for xyz in range(10000):
			zeros = [0 for x in range(31)]
			zeros[0] = 1
			zeros[-1] = 1
			self.assertEqual(len(zeros), 31)
			i = randint(2, 29)
			zeros[i] = 1
			zeros = ''.join([str(x) for x in zeros])
			N = int(zeros, 2)
			eO = max([len(x) for x in zeros.split('1')])
			self.assertEqual(
				eO,
				binary_gap(N),
				'-'*100 + f'\nbinary_gap({N}) == {binary_gap(N)}\nbin({N}) == {bin(N)} where xyz == {xyz}')









