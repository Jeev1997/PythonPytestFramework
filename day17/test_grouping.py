import pytest

def test_login():
    print("this is just login")
    assert True

@pytest.mark.sanity
def test_loginfacebook():
    print("this is just login fb")
    assert True

def test_logininstgrame():
    print("this is just login insta")
    assert True

@pytest.mark.sanity
def test_logintwitter():
    print("this is just login twt")
    assert True

def test_loginwhatsup():
    print("this is just login wats")
    assert True

@pytest.mark.regression
def test_logingmail():
    print("this is just login mail")
    assert True

#pytest day17/test_grouping.py -s -v -m "sanity"
#pytest day17/test_grouping.py -s -v -m "sanity" -m "not regression
# pytest day17/test_grouping.py -s -v -m "sanity and regression"
# pytest day17/test_grouping.py -s -v -m "sanity"