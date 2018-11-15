from ..math import div
from random import randint

def test_spec():
    a = randint(1, 10)
    b = randint(1, 10)
    assert div(a, b) == a / b

def test_nocommut():
    a = randint(1, 10)
    b = randint(1, 10)
    # Find one that isn't equal to a
    while b == a:
        b = randint(1, 10)
    assert div(a, b) != div(b, a)
