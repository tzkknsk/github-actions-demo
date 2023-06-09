from sample.calc import Calc

def test_add():
    calc = Calc()
    assert calc.add(1, 3) == 4

def test_minus():
    calc = Calc()
    assert calc.minus(5, 3) == 2

def test_multiply():
    calc = Calc()
    assert calc.multiply(2, 3) == 6

def test_divide():
    calc = Calc()
    assert calc.divide(10, 2) == 5