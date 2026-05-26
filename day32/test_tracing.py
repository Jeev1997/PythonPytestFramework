import pytest

# playwright show trace trace.zip

from playwright.sync_api import Playwright, sync_playwright

def test_capture(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True)
    page = playwright.chromium.launch(headless=False)
    page = context.new_page()

    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.wait_for_timeout(5000)

    # get_by_label()
    page.get_by_label("First name").fill("John")
    page.get_by_label("Last Name").fill("kenedy")
    page.get_by_label("Email").fill("adc@gmail.com")
    page.wait_for_timeout(5000)

    context.tracing.stop(path = "trace.zip")
    context.close()
    browser.close()