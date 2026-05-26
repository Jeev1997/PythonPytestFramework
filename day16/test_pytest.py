# pip install pytest

# skip test
# Grouping test
# parallel test
# ordering test
# fixture

import pytest

def test_m1():
    print("\n this is m1")

def test_m2():          # test functions
    print("this is m2")

def test_m3():
    print("this is m3")


# pytest day16/test_pytest.py
# pytest day16/test_pytest.py -s
# pytest day16/test_pytest.py -s -v
# pytest day16/test_pytest.py::test_m1