import pytest
from conftest import Setup

class Demo_1(Setup):
    def test_sum(self):
        a = 10
        b = 20
        sum = a + b
        assert sum == 30


class Demo_2(Setup):
    def test_mul(self):
        a = 10
        b = 20
        mul = a * b
        assert mul == 200


class Demo_3(Setup):
    def test_div(self):
        a = 10
        b = 20
        div = b // a
        assert div == 3


class Demo_4(Setup):
    def test_m(self):
        a = 10
        b = 20
        mul = a * b
        assert mul == 200
