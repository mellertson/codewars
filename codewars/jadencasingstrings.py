

__all__ = [
	'toJadenCase',
]


def toJadenCase(string):
	jcs = string.split(' ')
	for jc in jcs:
		jc = jc[0].upper()
	return ' '.join(jcs)


