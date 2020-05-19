class Calc:
    def add(self, x,y):
        return x + y


    def divide(self, x, y):
        if y == 0:
            raise ValueError('can not be 0')
        return x / y