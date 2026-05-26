
'''
css selector

tag tag#id
tag tag.class
tag tag[attribute]
tag tag.class [attribute]


'''



import pytest
from playwright.sync_api import Page

def test_css(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(5000)
# id
    #page.locator("#small-searchterms").fill("computer")

# .class

    page.locator(".search-box-text ui-autocomplete-input").fill("t-shirt")

# attribute
    page.locator("input.[type=text]").fill("t-shirt")

# class and attribute
    page.locator("input.earch-box-text ui-autocomplete-input[type=text]").fill("t-shirt")
