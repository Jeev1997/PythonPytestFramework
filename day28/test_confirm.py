

import pytest

from playwright.sync_api import Page, expect


def test_conf(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)


    page.on("dailog", lambda dailog:dailog.dismiss())
    page.wait_for_timeout(5000)
    page.locator("#confirmBtn").click()
    page.wait_for_timeout(5000)
    text = page.locator("#demo").inner_text()

    print("displayed", text)

    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")