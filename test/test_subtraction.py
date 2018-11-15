from ../src/math import sub
from random import randint

def test_spec():
    a = randint(1, 10)
    b = randint(1, 10)
    assert sub(a, b) == a + b

def test_commut():
    a = randint(1, 10)
    b = randint(1, 10)
    assert sub(a, b) == sub(b, a)

def test_assoc():
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 10)
    assert sub(a, sub(b, c)) == sub(sub(a, b), c)
