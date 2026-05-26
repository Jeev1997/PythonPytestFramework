
from playwright.sync_api import Page

class Loginpage:
    def __init__(self, page: Page):
        self.page = page
        self.loginlink = self.page.locator("#login2")
        self.userfield = self.page.locator("#loginusername")
        self.passwordfield = self.page.locator("#loginpassword")
        self.loginbutton = self.page.locator("button[onclick='logIn()']")



     #actions
    def perform_action(self, username,password):
        self.loginlink.click()
        self.userfield.fill("username")
        self.passwordfield.fill("password")
        self.loginbutton.click()
