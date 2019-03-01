import re, math, os, sys


__all__ = [
	'find_smallest_integer_in_set',
	'binary_gap',
]


def find_smallest_integer_in_set(A):
	"""

	:param A:
	:type A: list of int
	:return:
	:rtype: int
	"""

	for i in range(1, 1000000):
		if i not in A:
			return i


zeros_ptn = re.compile(r'(?=(10+1))')


def binary_gap(N):
	bg_str = bin(N)[2:]
	n = 0
	for s in zeros_ptn.findall(bg_str):
		l = len(s) - 2
		if l > n:
			n = l
	return n









