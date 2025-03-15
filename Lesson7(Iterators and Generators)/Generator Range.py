def genrange(start, end):
    while start <= end:
        yield start
        start +=1

# test zero
import unittest

class GenrangeTests(unittest.TestCase):
    def test_zero(self):
        res = list(genrange(1, 10))
        self.assertEqual(res, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()