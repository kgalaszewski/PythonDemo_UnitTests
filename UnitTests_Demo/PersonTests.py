import unittest
from Person import Person, Person2
from calc import Calc
from unittest.mock import MagicMock, patch

# wersja bez mocka
class PersonTests(unittest.TestCase):
    def setUp(self):
        self.calculator = Calc()
        self.subject = Person(self.calculator)


    def test_use_calc_to_divide(self):
        result = self.subject.use_calc_to_divide(10, 5)
        self.assertEqual(2, result)

        with self.assertRaises(ValueError):
            self.subject.use_calc_to_divide(10, 0)

# wersja z przykladem uzycia Magic Mocka
class PersonTests2(unittest.TestCase):
    
    def test_use_calc_to_divide(self):
        calc = Calc()
        calc.divide = MagicMock(return_value = 3)
        subect = Person(calc)

        result = subect.use_calc_to_divide(10, 5)
        self.assertNotEqual(2, result) # not equal because the mock should do the job

    # using patch
    def test_use_calc_to_divide2(self):        
        with patch.object(Calc, 'divide', return_value=2) as moj_moczek:
            moj_moczek.return_value = 2 # mowimy ze metoda tej klasy ma zwracac 2

            subject = Person2()
            result = subject.use_calc_to_divide(10, 5)

            self.assertEqual(2, result)
            
            moj_moczek.assert_called_with(10, 5) # sprawdzamy, czy zostal wywolany z poprawnymi parametrami

        moj_moczek.assert_called_once_with(10, 5) # to samo ale once i nie musi byc w scope with 
        



if __name__ == '__main__':
    unittest.main()