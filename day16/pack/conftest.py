import pytest

@pytest.fixture
def setup():
    print("browser chrome")
    yield
    print("teardown")