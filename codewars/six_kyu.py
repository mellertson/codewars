import re, copy


__all__ = [
	'balance',
]


invalid_ptn = re.compile(r'[^a-zA-Z\d .]')
check_n_ptn = re.compile(r'(\d+)')
category_ptn = re.compile(r'([a-zA-Z]+)')
amount_ptn = re.compile(r'(\d+[.]\d+)')


def balance(book):
	"""
	Parse lines from a checkbook into a report

	:param book: The lines of the checkbook
	:type book: str
	:return: The lines of the report
	:rtype: str
	"""

	global invalid_ptn, check_n_ptn, category_ptn
	ilines = book.split('\n')
	olines = []
	m = amount_ptn.match(ilines[0])
	starting_bal = float(m.group(1)) if m else 0.0
	olines.append(f'Original Balance: {starting_bal:.2f}')
	amounts = []
	for line in ilines[1:]:
		if len(line) == 0:
			continue
		line = re.sub(invalid_ptn, '', line)
		check_match = check_n_ptn.match(line)
		check_n = check_match.group(1) if check_match else None
		category_match = category_ptn.search(line)
		category = category_match.group(1) if category_match else None
		amount_match = amount_ptn.search(line)
		amount = float(amount_match.group(1)) if amount_match else 0.0
		amount = int(amount * 100) / 100.0
		amounts.append(amount)

		# store the output line
		olines.append(f'{check_n} {category} {amount:.2f} Balance {starting_bal - sum(amounts):.2f}')
	olines.append(f'Total expense  {sum(amounts):.2f}')
	olines.append(f'Average expense  {sum(amounts) / len(amounts):.2f}')
	return '\r\n'.join(olines)

