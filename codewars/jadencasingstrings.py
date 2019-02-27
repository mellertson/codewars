

__all__ = [
	'toJadenCase',
]


def toJadenCase(string):
	jcs = string.split(' ')
	for i in range(len(jcs)):
		jcs[i] = jcs[i][0].upper() + jcs[i][1:]
	return ' '.join(jcs)


