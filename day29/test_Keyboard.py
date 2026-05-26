
import pytest

from playwright.sync_api import Page

def test_key(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    main = page.locator("#input1")

    main.focus()

    page.keyboard.insert_text("welcome")

    page.wait_for_timeout(5000)

    page.keyboard.press("Control+A")

    page.keyboard.press("Control+C")

    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    page.keyboard.press("Control+V")

    page.wait_for_timeout(5000)

