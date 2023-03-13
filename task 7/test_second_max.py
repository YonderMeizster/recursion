from random import randint
from second_max import get_second_max
import pytest


def test_1():
    with pytest.raises(ValueError):
        get_second_max([])
    with pytest.raises(ValueError):
        get_second_max([1])


def test_2():
    assert get_second_max([1, 2]) == 1
    assert get_second_max([2, 2]) == 2


def test_3():
    for _ in range(1000):
        length = randint(2, 40)
        values = [None] * length

        for i, _ in enumerate(values):
            values[i] = randint(-20, 20)

        assert get_second_max(values) == sorted(values)[-2]
