from playwright.sync_api import Playwright
from Automation.utils import creds
from Automation.pages.library.data_import_page import data_import
from Automation.utils.browser import login, open_browser

def test_library(playwright: Playwright):
    
    page = open_browser(playwright)
    credential = {
        "url": creds.provider_url,
        "email": creds.provider_email,
        "password": creds.provider_password
    }
    login(page, credential)
    
    entities = ["Provider Data", "CPT Code", "Drug Catalog", "ICD 10 Code", "HCPCS Code", "LOINC Code", "Patient Data"]
    data_import(page, entities)