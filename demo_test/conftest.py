import pytest


@pytest.fixture(autouse=True,scope="class")
class Setup:
    def test_start(self):
        print("test started ..................................")

        yield
        print("setup closed successfully.......................")
