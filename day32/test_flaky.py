
from playwright.sync_api import Page
import pytest

#pytest day32/test_flaky.py --headed --reruns 3

#pip install rerunfailures

def test_flaky(page:Page):
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.wait_for_timeout(5000)

    # get_by_label()
    page.get_by_label("First name").fill("John")
    page.get_by_label("Last Name").fill("kenedy")
    page.get_by_label("Email").fill("adc@gmail.com")
    page.wait_for_timeout(5000)