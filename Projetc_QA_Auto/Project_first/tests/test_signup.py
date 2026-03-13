import time

from playwright.sync_api import Page, expect, Playwright


def test_signup(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.automationexercise.com/signup")


# Alternative
def test_signup_Shortcut(page: Page):
    page.goto("https://www.automationexercise.com/signup")


#    page.get_by_role("combobox").select_option("option)--> Menu deroulant
# ---#termes = ID ,   .terms = class
# this fonction is to signup in the website for the registration
def test_signup_corelocators(page: Page):
    page.goto("https://www.automationexercise.com/signup")
    page.get_by_role("button", name="Einwilligen").click()
    page.locator('[data-qa="signup-name"]').fill("Junior")
    page.locator('[data-qa="signup-email"]').fill("junior74814615@gmail.com")
    page.locator('[data-qa="signup-button"]').click()


# --> not work   expect (page.get_by_text("This site asks for consent to use your data")).to_be_visible()
# --> not work    expect(page.get_by_role("button", name ="Einwilligen")).to_be_visible() me prend pas

def test_firefoxBrowser(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    page = firefoxBrowser.new_page()
    page.goto("https://www.automationexercise.com/signup")
    page.get_by_role("button", name="Einwilligen").click()
    page.locator('[data-qa="signup-name"]').fill("Junior")
    page.locator('[data-qa="signup-email"]').fill("junior74814615@gmail.com")
    page.locator('[data-qa="signup-button"]').click()
