
#get_by_alt_text() -- used for images
#get_by_text()
#get_by_role()
#get_by_label()
#get_by_placeholder()
#get_by_title()
#get_by_titleid()

from playwright.sync_api import Page, expect
def test_verify(page:Page):
    #page.goto("https://demo.nopcommerce.com/")
    #page.wait_for_timeout(5000)   # 5 sec
# get_by_alt_text()
    #expect(page.get_by_alt_text("nopCommerce demo store")).to_be_visible()

# get_by_text()
    #expect(page.get_by_text("Welcome to our store")).to_be_visible()  # text should be same in dome and UI

#get_by_role()
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.wait_for_timeout(5000)
    expect(page.get_by_role("heading", name = "Register")).to_be_visible()

#get_by_label()
    page.get_by_label("First name").fill("John")
    page.get_by_label("Last Name").fill("kenedy")
    page.get_by_label("Email").fill("adc@gmail.com")
    page.wait_for_timeout(5000)

#get_by_placeholder
    page.get_by_placeholder("Search store").fill("Apple")
    page.wait_for_timeout(5000)
    page.get_by_role("button", name = "submit").click()
    page.wait_for_timeout(5000)
