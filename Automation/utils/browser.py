from playwright.sync_api import Playwright, sync_playwright, expect, Page

def open_browser(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=300, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True, permissions=["camera", "microphone"])
    page = context.new_page()
    return page

def login(page: Page, login_creds: dict):
    page.goto(login_creds.get("url"))
    page.wait_for_timeout(1000)
    page.get_by_text("Hey, good to see you").click()
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill(login_creds.get("email"))
    page.locator("//input[@type='password']").click()
    page.locator("//input[@type='password']").fill(login_creds.get("password"))
    page.get_by_role("button", name="Let's get Started").click()
    page.wait_for_timeout(1000)
    return page