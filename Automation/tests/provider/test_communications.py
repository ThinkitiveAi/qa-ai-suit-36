from playwright.sync_api import Playwright, sync_playwright
from Automation.pages.communications.email import email
from Automation.utils import creds
from Automation.pages.library.data_import_page import data_import
from Automation.utils.browser import login, open_browser

def run(playwright: Playwright):
    
    page = open_browser(playwright)
    credential = {
        "url": creds.provider_url,
        "email": creds.provider_email,
        "password": creds.provider_password
    }
    login(page, credential)

    email(page)

with sync_playwright() as playwright:
    run(playwright)  