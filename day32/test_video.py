

import pytest

from playwright.sync_api import Playwright, sync_playwright

def test_capture(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(

        record_video_dir = "videos/",
        record_video_size = {"width":1028,"height":768}
    )
    page = context.new_page()

    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.wait_for_timeout(5000)

    # get_by_label()
    page.get_by_label("First name").fill("John")
    page.get_by_label("Last Name").fill("kenedy")
    page.get_by_label("Email").fill("adc@gmail.com")
    page.wait_for_timeout(5000)

    context.close()
    browser.close()