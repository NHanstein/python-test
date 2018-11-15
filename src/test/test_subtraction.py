from ..math import sub
from random import randint

def test_spec():
    a = randint(1, 10)
    b = randint(1, 10)
    assert sub(a, b) == a - b

def test_nocommut():
    a = randint(1, 10)
    b = randint(1, 10)
    # Find one that isn't equal to a
    while b == a:
        b = randint(1, 10)
    assert sub(a, b) != sub(b, a)

def test_commutabs():
    a = randint(1, 10)
    b = randint(1, 10)
    assert abs(sub(a, b)) == abs(sub(b, a))
