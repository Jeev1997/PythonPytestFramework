import pytest

def test_login():
    print("this is just login")
    assert True

@pytest.mark.skip
def test_loginfacebook():
    print("this is just login fb")
    assert True

def test_logininstgrame():
    print("this is just login insta")
    assert True

@pytest.mark.skip
def test_logintwitter():
    print("this is just login twt")
    assert True

def test_loginwhatsup():
    print("this is just login wats")
    assert True

def test_logingmail():
    print("this is just login mail")
    assert True