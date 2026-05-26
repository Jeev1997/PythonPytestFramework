# Fixture are normal function --- used for reuseable code


#Scope = Function -- after every function
#Scope = Module   -- after every module
#Scope = class    -- only after class
#Scope = session  -- only after session

import pytest

@pytest.fixture
def setup(scope="function"):
    print("\n Browser chrome")

def test_m1(setup):
    print("\n this is m1")

def test_m2(setup):          # test functions
    print("this is m2")

def test_m3(setup):
    print("this is m3")


# pytest day16/test_pytest.py
# pytest day16/test_pytest.py -s
# pytest day16/test_pytest.py -s -v
# pytest day16/test_pytest.py::test_m1