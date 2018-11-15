from ..math import mul
from random import randint

def test_spec():
    a = randint(1, 10)
    b = randint(1, 10)
    assert mul(a, b) == a * b

def test_commut():
    a = randint(1, 10)
    b = randint(1, 10)
    assert mul(a, b) == mul(b, a)

def test_assoc():
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 10)
    assert mul(a, mul(b, c)) == mul(mul(a, b), c)
