import unittest
from calc import Calc

class CalcTests(unittest.TestCase):
    def setUp(self):
        self.subject = Calc()

    def test_add(self):
        result = self.subject.add(10, 5)
        self.assertEqual(result, 15)

    def test_divide(self):
        result = self.subject.divide(10, 5)
        self.assertEqual(2, result)

        with self.assertRaises(ValueError):
            self.subject.divide(10, 0)

if __name__ == '__main__':
    unittest.main()