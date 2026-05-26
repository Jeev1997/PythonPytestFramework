import pytest

from playwright.sync_api import Page

import json
file = open("testdata/data.json", 'r')
all_data = json.load(file)

@pytest.mark.parametrize("email,password",[(data["email"],data["password"]) for data in all_data])
def test_ddjson(email,password , page:Page):
    page.goto("https://demowebshop.tricentis.com/login")
    page.locator("#Email").fill("email")
    page.locator("#Password").fill("password")
    page.locator("#Login").click()