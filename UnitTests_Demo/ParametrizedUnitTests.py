class FakeDbContext:
    def __init__(self):
        super().__init__()

    def get_data(self):
        return True

class KlasaUzywajacaDbContext:
    def przetworz_dane(self, x: int, db_context):
        if db_context.get_data():
            return x

import pytest
from MsiPrestige import MsiPrestige
from unittest import mock

# IMPORTANT FOR PYTEST TO WORK IT AS A TEST CLASS
# CLASS NAME SHOULD START WITH "Test"

class TestKlasaUDbc:
    def setup(self):
        self.subject = KlasaUzywajacaDbContext()

    def test_przetworz_dane(self):
        db_context = FakeDbContext()
        db_context.get_data = mock.Mock(return_value=True)
        result = self.subject.przetworz_dane(5, db_context)
        assert result == 5


class TestMsiPrestige():    
    def setup(self):
        self.subject = MsiPrestige()

    test1data = [
        (2, 2, 4),
        (3, 3, 9),
        (4, 4, 16),
        (5, 5, 25),
        (6, 6, 36)
    ]
    @pytest.mark.parametrize("x, y, expected", test1data)
    def test_oblicz_pole_kwadratu(self, x: int, y: int, expected: int):
        result = self.subject.oblicz_pole_kwadratu(x, y)
        assert result == expected

    def test_co_sie_odpierdala(self):
        assert 2 == 2






