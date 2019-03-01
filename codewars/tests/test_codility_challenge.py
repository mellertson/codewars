import unittest, re
from random import randint
from timeout_decorator import timeout
from codewars.codility_challenge import *


class find_smallest_integer_in_set_Tests(unittest.TestCase):

	def setUp(self):
		self.max_length = 111111
		self.large1_length = int(self.max_length * 0.4)
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
			self.assertEqual(eO, find_smallest_integer_in_set(i))


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


class frog_jump_Tests(unittest.TestCase):

	def setUp(self):
		self.min = 1
		self.max = 1000000000

	def test_large1___ten_thousand_times(self):
		for i in range(100):
			x = randint(self.min, self.max)
			y = randint(x, self.max)
			d = randint(self.min, self.max)


class regex_Tests(unittest.TestCase):

	def print_line(self):
		print('\n' + '-' * 100 + '\n')

	def setUp(self):
		self.print_line()

	def tearDown(self):
		self.print_line()

	def test_pattern_finditer(self):
		# setup
		text = '''abcdefghijklmnopqrstuvwxyz
		Rubber duckies rub rubber with their feet
		1010010001000010000010000001000000010000000001
		'''
		str1 = r'abc'
		str2 = r'\b\w*be\w*\b'
		str3 = r'[Rr]ub\w*'
		ptn1 = re.compile(str1)
		ptn2 = re.compile(str2)
		ptn3 = re.compile(str3)

		# test: for ptn 1
		matches1 = ptn1.finditer(text)
		print(f"matches found with r'{str1}':")
		for match in matches1:
			print(match)

		# test: for ptn 2
		self.print_line()
		matches2 = ptn2.finditer(text)
		print(f"matches found with r'{str2}':")
		for match in matches2:
			print(match)

		# test: for ptn 3
		self.print_line()
		matches = ptn3.finditer(text)
		print(f"matches found with r'{str3}':")
		for match in matches:
			print(match)

	def match_and_print(self, raw_string, search_text, flags=None):
		if flags:
			ptn = re.compile(raw_string, flags=flags)
		else:
			ptn = re.compile(raw_string)
		matches = ptn.finditer(search_text)
		print(f"With regex pattern:\n\tr'{raw_string}'\n\nThe following matches were found:")
		for match in matches:
			print(f'\t{match}')
		print(f'\nIn the text: "{search_text}"')

	def test_beginning_end_of_string_regex____with_out_MULTILINE_flag(self):
		text = '''start end
start but not the end
start still not the end
start really the end'''
		pstart = r'^start'
		self.match_and_print(pstart, text)
		self.print_line()
		pend = r'end$'
		self.match_and_print(pend, text)

	def test_beginning_end_of_string_regex____with_MULTILINE_flag(self):
		text = '''start end
start but not the end
start still not the end
start really the end'''
		pstart = r'^start'
		self.match_and_print(pstart, text, flags=re.MULTILINE)
		self.print_line()
		pend = r'end$'
		self.match_and_print(pend, text, flags=re.MULTILINE)


class Gun_IO_Tests(unittest.TestCase):

	@classmethod
	def print_line(cls):
		print('\n' + '-' * 100 + '\n')

	def setUp(self):
		self.print_line()
		self.min = 1
		self.max = 2147483647

	def tearDown(self):
		self.print_line()

	def test_case1(self):
		# setup
		print('test_case1')
		N = 1

		# test
		r = gun_io_solution(N)


		# verify
		self.assertIsNone(r)

	def test_large1(self):
		''' 10,000 iterations '''

		# setup
		print('test_large1')

