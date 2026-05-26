

from playwright.sync_api import Page

import datetime
import pytest

def test_screenshot(page:Page):

    page.goto("https://demowebshop.tricentis.com/")
    page.screenshot(path = "screenshot/first.png")

    timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # full page

    page.screenshot(path = f"screenshot/second_{timestamp}.png", full_page=True)
