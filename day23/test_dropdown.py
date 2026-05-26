from itertools import count

import pytest

from playwright.sync_api import Page, expect

def test_drop(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select option 3 way
    # 1st way

    value = page.locator("#country")
    #value.select_option(value= "Japan")
    # value.select_option("Japan") # 2nd way

    value.select_option(index=8)   # 3rd way
    page.wait_for_timeout(5000)


   # to select all the options

    all = page.locator("#country>option")
    expect(all).to_have_count(10)

    allvalue=all.all_text_contents()
    print("options value", allvalue)


    textbox= [text.strip() for text in allvalue]

    for item in textbox:
        print("item", item)



