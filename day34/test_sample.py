
# pip install pytest-html
#--html=report.html --self_contained-html --capture=tee-sys (to capture failed TC SS)
import pytest


from playwright.sync_api import Page, expect

def test_main(page:Page):
    page.goto("https://google.com")
    expect(page).to_have_title("Google")


def test_main1(page:Page):
    page.goto("https://www.bing.com/?toWww=1&redig=1C010FD757DD4BC0BB1AFF86EEE6C052")
    expect(page).to_have_title("bing123")

def test_main2(page:Page):
    page.goto("https://demoblaze.com/")
    expect(page).to_have_title("STORE")