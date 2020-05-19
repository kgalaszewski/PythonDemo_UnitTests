from calc import Calc

class Person:
    def __init__(self, calculator):
        self.calculator = calculator

    def use_calc_to_divide(self, x: int, y: int):
        return self.calculator.divide(x, y)

class Person2:

    def use_calc_to_divide(self, x: int, y: int):
        return Calc().divide(x, y)