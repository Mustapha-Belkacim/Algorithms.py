def factorial(n):
	if not isinstance(n, int):
		raise TypeError(f'Function is not defined for non-integer values, {n} is not an integer')
	if n < 0:
		raise ValueError(f'Function is not defined for negitave values, {n} is negative')
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
