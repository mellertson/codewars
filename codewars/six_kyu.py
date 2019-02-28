import re, copy


__all__ = [
	'balance',
]


balance_invalid_ptn = re.compile(r'[^a-zA-Z\d .]')
balance_line_ptn = re.compile(r'(\d+)[ ]+([a-zA-Z]+)[ ]+(\d+[.]\d+)')


def balance(book):
	"""
	Parse lines from a checkbook into a report

	:param book: The lines of the checkbook
	:type book: str
	:return: The lines of the report
	:rtype: str
	"""

	global balance_invalid_ptn, balance_line_ptn
	ilines = book.split('\n')
	olines = []
	line = re.sub(balance_invalid_ptn, '', ilines[0])
	obalance = float(line)
	olines.append(f'Original Balance: {obalance:.2f}')
	amounts = []
	for line in ilines[1:]:
		if len(line) == 0:
			continue
		line = re.sub(balance_invalid_ptn, '', line)
		m = balance_line_ptn.match(line)
		if m:
			check_n = m.group(1)
			category = m.group(2)
			amount = float(m.group(3))
			amount = int(amount * 100) / 100.0
			amounts.append(amount)

			# store the output line
			olines.append(f'{check_n} {category} {amount:.2f} Balance {obalance - sum(amounts):.2f}')
	olines.append(f'Total expense  {sum(amounts):.2f}')
	olines.append(f'Average expense  {sum(amounts) / len(amounts):.2f}')
	return '\r\n'.join(olines)

