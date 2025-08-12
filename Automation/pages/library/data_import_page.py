from playwright.sync_api import Page, Playwright, sync_playwright
from Automation.utils import creds
import pandas as pd
# Load CSV Data
df = pd.read_csv(creds.cpt_code_csv)



def data_import(page: Page, entity: list):
    page.get_by_role("tab", name="Library").click()
    # Data Import > Provider data
    page.get_by_text("Data Import").click()    
    page.get_by_role("button", name="Upload Data").click()
    page.get_by_placeholder("Select").click()
    page.get_by_role("option", name=entity[0]).click()
    
    file_input = page.query_selector('input[type="file"]')
    file_path = creds.provider_data_csv
    file_input.set_input_files(file_path)
    
    page.get_by_role("button", name="Upload").click()
    page.wait_for_timeout(3000)
    page.get_by_placeholder("Entity Type").click()
    page.get_by_role("option", name=entity[0]).click()
    
    # Data Import > CPT Code
    page.get_by_role("button", name="Upload Data").click()
    page.get_by_placeholder("Select").click()
    page.get_by_role("option", name=entity[1]).click()
    
    file_input = page.query_selector('input[type="file"]')
    file_path = creds.cpt_code_csv
    file_input.set_input_files(file_path)
    
    page.get_by_role("button", name="Upload").click()
    page.wait_for_timeout(3000)
    page.get_by_placeholder("Entity Type").click()
    page.get_by_role("option", name=entity[1]).click()
    page.locator("(//p[text()='CPT Catalog'])[1]").click()
    
    
    # # Data Import > Drug Catalog
    # page.get_by_role("button", name="Upload Data").click()
    # page.get_by_placeholder("Select").click()
    # page.get_by_role("option", name=entity[2]).click()
    
    # file_input = page.query_selector('input[type="file"]')
    # file_path = creds.
    # file_input.set_input_files(file_path)
    
    # page.get_by_role("button", name="Upload").click()
    # page.wait_for_timeout(3000)
    # page.get_by_placeholder("Entity Type").click()
    # page.get_by_role("option", name=entity[2]).click()
    
    
    # Data Import > ICD 10 Code
    page.get_by_role("button", name="Upload Data").click()
    page.get_by_placeholder("Select").click()
    page.get_by_role("option", name=entity[3]).click()
    
    file_input = page.query_selector('input[type="file"]')
    file_path = creds.icd_code_csv
    file_input.set_input_files(file_path)
    
    page.get_by_role("button", name="Upload").click()
    page.wait_for_timeout(3000)
    page.get_by_placeholder("Entity Type").click()
    page.get_by_role("option", name=entity[3]).click()
    
    
    # Data Import > HCPCS Code
    page.get_by_role("button", name="Upload Data").click()
    page.get_by_placeholder("Select").click()
    page.get_by_role("option", name=entity[4]).click()
    
    file_input = page.query_selector('input[type="file"]')
    file_path = creds.hcpcs_code_csv
    file_input.set_input_files(file_path)
    
    page.get_by_role("button", name="Upload").click()
    page.wait_for_timeout(3000)
    page.get_by_placeholder("Entity Type").click()
    page.get_by_role("option", name=entity[4]).click()
    
    
    # Data Import > LOINC Code
    page.get_by_role("button", name="Upload Data").click()
    page.get_by_placeholder("Select").click()
    page.get_by_role("option", name=entity[5]).click()
    
    file_input = page.query_selector('input[type="file"]')
    file_path = creds.loinc_code_csv
    file_input.set_input_files(file_path)
    
    page.get_by_role("button", name="Upload").click()
    page.wait_for_timeout(3000)
    page.get_by_placeholder("Entity Type").click()
    page.get_by_role("option", name=entity[5]).click()
    
    
    # Data Import > Patient Data
    page.get_by_role("button", name="Upload Data").click()
    page.get_by_placeholder("Select").click()
    page.get_by_role("option", name=entity[6]).click()
    
    file_input = page.query_selector('input[type="file"]')
    file_path = creds.patient_data_csv
    file_input.set_input_files(file_path)
    
    page.get_by_role("button", name="Upload").click()
    page.wait_for_timeout(3000)
    page.get_by_placeholder("Entity Type").click()
    page.get_by_role("option", name=entity[6]).click()
