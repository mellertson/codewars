import re, math, os, sys


__all__ = [
	'solution',
	'binary_gap',
]


def solution(A):
	"""

	:param A:
	:type A: list of int
	:return:
	:rtype: int
	"""

	A_dict = {x:None for x in A}
	items = sorted(A_dict.keys())
	orange = range(1, 1000000)
	for i in orange:
		if i not in items:
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









