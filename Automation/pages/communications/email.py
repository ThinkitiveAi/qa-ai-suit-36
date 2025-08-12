from playwright.sync_api import Page

from Automation.utils import creds, data

def email(page: Page) -> None:
    page.get_by_role("tab", name="Communications").click()
    page.get_by_text("Email").click()
    page.get_by_text("Emails").click()
    page.locator("(//input[@type='checkbox'])[1]").check()
    page.get_by_role("button", name="Send Emails").click()
    page.get_by_placeholder("Select Template").click()
    page.get_by_role("option", name="Email template for follow up invitation").click()
    page.get_by_role("button", name="Send").click()
    # page.wait_for_timeout(10000)
    page.get_by_text("Email sent successfully to patients;").click()
    print("Email sent successfully to patients;")
    return page