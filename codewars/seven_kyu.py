

__all__ = [
	'divisors',
]



def divisors(integer):
	"""
	Return a list of divisors of an integer

	NOTE: this function is not optimized for large primes

	:param integer: The integer
	:type integer: int
	:return: The list of divisors or primality string
	:rtype: list of int | str
	"""

	answer = []
	half = int(integer / 2)
	for i in range(2, half + 1):
		if integer % i == 0:
			answer.append(i)
	if len(answer) == 0:
		return f'{integer} is prime'
	return answer



