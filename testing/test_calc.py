import calc, pytest
from functools import reduce
from operator import sub

class TestAdd:
    def test_none(self):
        assert calc.add() == 0

    def test_one(self):
        assert calc.add(1) == 1

    def test_two(self):
        assert calc.add(1, 2) == 3

    def test_three(self):
        assert calc.add(1, 2, 3) == 6

    def test_several(self):
        assert calc.add(1, 2, 3, 4, 5, 6) == sum(range(1, 7))



class TestSub:
    def test_none(self):
        with pytest.raises(ValueError):
            calc.sub()

    def test_one(self):
        assert calc.sub(1) == -1

    def test_two(self):
        assert calc.sub(1, 2) == -1

    def test_three(self):
        assert calc.sub(1, 2, 3) == -4

    def test_several(self):
        assert calc.sub(1, 2, 3, 4, 5, 6) == reduce(sub, range(1, 7))
