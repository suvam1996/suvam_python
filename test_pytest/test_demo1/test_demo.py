import pytest


@pytest.mark.skip
def test_sample_one():
    a = 5
    b = 6
    assert a == b, 'a is not equal b'


@pytest.mark.smoke
def test_sample_two():
    a = 55
    b = 65
    assert b > a


@pytest.mark.smoke
def test_sample_three():
    a = 10
    b = 20
    assert b > a


@pytest.mark.regression
def test_sample_four():
    a = 'suvam'
    b = 'sambit'
    assert a.__eq__(b), 'a is not equal'

