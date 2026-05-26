# pip install pytest-playwright -- to install playwright

# playwright install --- to install all the browsers


from playwright.sync_api import Page , expect
def test_url(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page).to_have_url("https://rahulshettyacademy.com/AutomationPractice/")

def test_tilte(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    Title = page.title()
    print(Title)
#pytest day18/test_pw.py::test_tilte -s -v --headed --browser chromium --browser firefox

#pytest day18/test_pw.py::test_tilte -s -v --headed --browser chromium --browser firefox -n 2

#pytest day18/test_pw.py::test_tilte -s -v --headed --browser chromium --browser firefox -n=2