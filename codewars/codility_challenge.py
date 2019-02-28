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


zeros_ptn = re.compile(r'(10+1)')


def binary_gap(N):
	bg_str = bin(N)[2:]
	m = zeros_ptn.search(bg_str)
	if m is None:
		return 0
	else:
		n = 0
		for g in m.groups():
			if len(g) > n:
				n = len(g)
		return n - 2









