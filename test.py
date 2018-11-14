from add import add
from random import randint

def test_commut():
    a = randint(1, 10)
    b = randint(1, 10)
    assert add(a, b) == add(b, a)

def test_spec():
    a = randint(1, 10)
    b = randint(1, 10)
    assert add(a, b) == a + b
