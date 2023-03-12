from exponitiate_number import exponitiate
from random import randint
from random import random as randfloat
import pytest


def test_zero_base():
    assert exponitiate(0, 1) == 0
    assert exponitiate(0, 0) == 1


def test_zero_base_negative_power():
    with pytest.raises(ZeroDivisionError):
        exponitiate(0, -1)


def test_positive_int_base():
    for i in range(5000):
        number = randint(1, 100)
        power = randint(-100, 100)
        assert abs(exponitiate(number, power) - pow(number, power)) < 0.00000001


def test_negative_int_base():
    for i in range(5000):
        number = randint(-100, -1)
        power = randint(-100, 100)
        assert abs(exponitiate(number, power) - pow(number, power)) < 0.00000001
