import playwright
from Automation.pages.library.template_page import template
from Automation.test_data.template_data import templates
from Automation.utils import creds
from Automation.utils.browser import login, open_browser


def test_template(playwright: playwright):
    
    page = open_browser(playwright)
    credential = {
        "url": creds.provider_url,
        "email": creds.provider_email,
        "password": creds.provider_password
    }
    login(page, credential)

    template(page, templates[0])
    template(page, templates[1])