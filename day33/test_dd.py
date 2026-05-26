
import pytest

from playwright.sync_api import Page, expect

list = ["laptop", "Gift card", "smartphone"]

@pytest.mark.parametrize("item", list)
def test_data(item ,page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").fill(item)
    page.locator("//input[@value='Search']").click()

    #Assertion
    value = page.locator("h2 a").nth(0)
    expect(value).to_contain_text(item, ignore_case=True)