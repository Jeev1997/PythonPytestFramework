
# relative xpath

# //tagname[@attribute = 'value']

# //tagname[contains(@att, 'value')]

# //tagname[text()='value']

# //tagname[start-with(@att , 'value')]
import pytest

from playwright.sync_api import Page, expect

def test_xpath(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()
    page.wait_for_timeout(5000)

# xpath with contains

    product = page.locator("//h2/a[contains(@href, 'computer')]")
    print("Products count", product.count())

    prodtitle = product.all_text_contents()
    print("all titles", prodtitle)

    for i in prodtitle:
       print(i)