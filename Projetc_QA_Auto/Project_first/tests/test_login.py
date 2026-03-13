import time

from playwright.sync_api import Page, expect, Playwright


# Alternative
def test_login_Shortcut(page: Page):
    page.goto("https://www.automationexercise.com/signup")


# this fonction is for the login the site
def test_login_corelocators(page: Page):
    page.goto("https://www.automationexercise.com/signup")
    page.get_by_role("button", name="Einwilligen").click()
    page.locator('[data-qa="login-email"]').fill("junior74814615@gmail.com")
    page.locator('[data-qa="login-password"]').fill("09w0823@Junior")
    page.locator('[data-qa="login-button"]').click()


# --> not work   expect (page.get_by_text("This site asks for consent to use your data")).to_be_visible()
# --> not work    expect(page.get_by_role("button", name ="Einwilligen")).to_be_visible() me prend pas
