
import pytest

from login_pom import Loginpage

from playwright.sync_api import Page, expect

@pytest.mark.parametrize("username,password",[("pavanol","test@123")])
def test_all_tc(page:Page,username,password):
    page.goto("https://demoblaze.com/")

    #login

    obj = Loginpage(page)
    obj.perform_action(username,password)

    loc= page.locator("#cat")
    expect(loc).to_have_text("CATEGORIES")


    page.wait_for_timeout(5000)

