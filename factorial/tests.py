import unittest

from factorial import factorial


class TestFactorial(unittest.TestCase):
	"""docstring for TestFactorial"""
	def test_factorial_returns_expected_value_for_positive_int(self):
		fact  = factorial(5)
		n = 5 * 4 * 3 * 2 
		self.assertEqual(fact, n)

	def test_factorial_retuns_1_for_0_value(self):
		self.assertEqual(factorial(0), 1)

	def test_factorial_raises_value_error_for_negative_int(self):
		self.assertRaises(ValueError, factorial, -9)

	def test_factorial_raises_type_error_for_float(self):
		self.assertRaises(TypeError, factorial, 3.8)

	def test_factorial_raises_type_error_for_string(self):
		self.assertRaises(TypeError, factorial, 'sdkfj')


if __name__ == '__main__':
	unittest.main()
