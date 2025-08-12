from playwright.sync_api import Playwright, Page
from Automation.pages.patient.req_patient_page import add_patient
from Automation.pages.scheduling.availability_page import availability
from Automation.pages.collaboration.open_encounter_page import OpenEncounter
from Automation.test_data import patient_data, scheduling_data
from Automation.utils import creds, data, local_data
from Automation.utils.browser import login, open_browser

def test_add_and_edit_task(page: Page, playwright: Playwright):

    page = open_browser(playwright)
    credential = {
        "url": creds.provider_url,
        "email": creds.provider_email,
        "password": creds.provider_password
    }
    login(page, credential)
    add_patient(page, patient_data.patient_data)
    availability(page)
    open_encounter = OpenEncounter(page)
    open_encounter.encounter_flow(scheduling_data.appointment_data)