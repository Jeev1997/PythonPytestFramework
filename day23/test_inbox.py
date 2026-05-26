import pytest

from playwright.sync_api import Page, expect

def test_inbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    filler = page.locator("#name")

    # expect(filler).to_be_visible()
    #
    # expect(filler).to_have_attribute("maxlength", 15)
    #
    # max = filler.get_attribute("maxlength")
    # print("value", max)

    filler.fill("John Kenedy")

    value = filler.input_value()

    print("value entered", value)

    page.wait_for_timeout(5000)