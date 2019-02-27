

__all__ = [
	'toJadenCase',
	'reverse_words',
]


def toJadenCase(string):
	"""
	Convert a sentence to have correct case for each word

	:param string: An improperly cased sentence.
	:type string: str
	:return: The sentence with corrected case for each word.
	:rtype: str
	"""

	jcs = string.split(' ')
	for i in range(len(jcs)):
		jcs[i] = jcs[i][0].upper() + jcs[i][1:]
	return ' '.join(jcs)


def reverse_words(text):
	words = text.split(' ')
	for i, word in enumerate(words):
		words[i] = word[::-1]
	return ' '.join(words)


