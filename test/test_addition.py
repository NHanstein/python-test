from ../src/math import add
from random import randint

def test_spec():
    a = randint(1, 10)
    b = randint(1, 10)
    assert add(a, b) == a + b

def test_commut():
    a = randint(1, 10)
    b = randint(1, 10)
    assert add(a, b) == add(b, a)

def test_assoc():
    a = randint(1, 10)
    b = randint(1, 10)
    c = randint(1, 10)
    assert add(a, add(b, c)) == add(add(a, b), c)
