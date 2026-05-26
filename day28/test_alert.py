import pytest

from playwright.sync_api import Page

@pytest.mark.skip
def test_alert(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)

    def fun(dailog):
        dailog.accept()

    page.on("dailog", fun)
    page.locator("#alertBtn").click()
    page.wait_for_timeout(5000)

def test_sec_alert(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)


    page.on("dailog",lambda dailog:dailog.accept())
    page.locator("#alertBtn").click()
    page.wait_for_timeout(5000)
