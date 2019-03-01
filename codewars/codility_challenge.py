import re, math, os, sys


__all__ = [
	'find_smallest_integer_in_set',
	'binary_gap',
	'solution',
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


def solution(message, K):
	'''
	Crop words from a message with max chars of K

	:param message:
	:type message: str
	:param K:
	:type K: int
	:return:
	:rtype: str
	'''

	p = re.compile(r'\b[a-zA-Z]+\b')
	r = ''
	matches = p.findall(message)
	for word in matches:
		if len(r) == 0:
			if len(word) <= K:
				r = word
			else:
				return ''
		else:
			if len(f'{r} {word}') <= K:
				r = f'{r} {word}'
			else:
				return r
	return r







