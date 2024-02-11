import pytest


@pytest.fixture()
def setup_teardown():
    print('id input successfully')
    print('password input successfully')
    print('login successfully')
    yield
    print('logout successfully')

def test_1(setup_teardown):
    print('first test exicute successfully')

def test_2(setup_teardown):
    print('secound test exicute successfully')

