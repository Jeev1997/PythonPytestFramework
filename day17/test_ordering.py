import pytest

# pip install pytest-ordering need to install

@pytest.mark.order(3)
def test_loginfacebook():
    print("this is just login fb")
    assert True

@pytest.mark.order(1)
def test_logininstgrame():
    print("this is just login insta")
    assert True


@pytest.mark.order(2)
def test_logintwitter():
    print("this is just login twt")
    assert True

