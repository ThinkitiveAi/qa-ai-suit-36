from playwright.sync_api import Playwright
from Automation.pages.billing.billing_page import super_bill_from_encounter_billing, super_bill
from Automation.pages.billing.claim_page import claim_from_encounter, claim_from_superbill, claims
from Automation.pages.patient.patient_page import create_patient
from Automation.pages.scheduling.instant_appointment_page import instant_appointment
from Automation.pages.scheduling.new_appointments_page import new_appointment
from Automation.pages.scheduling.availability_page import availability
from Automation.test_data import patient_data, scheduling_data
from Automation.utils import creds
from Automation.utils.browser import login, open_browser

def test_scheduling(playwright: Playwright):
    
    page = open_browser(playwright)
    credential = {
        "url": creds.provider_url,
        "email": creds.provider_email,
        "password": creds.provider_password
    }
    
    billing_data = {
        "patient_name": f"{patient_data.PATIENT_FNAME} {patient_data.PATIENT_LNAME}",
        # "patient_name": "Mark Nichols",
        "place_of_services": "Office",
        "total_bill": "3600"
    }
    
    try:
        login(page, credential)
        create_patient(page, patient_data.patient_data)
        availability(page)
        patientId = new_appointment(page, scheduling_data.appointment_data)
        instant_appointment(page, scheduling_data.appointment_data)
        # super_bill_from_encounter_billing(page, billing_data, patientId)
        # super_bill(page, billing_data, patientId)
        claim_from_encounter(page, scheduling_data.appointment_data)
        # claim_from_superbill(page, scheduling_data.appointment_data, billing_data)
        claims(page, scheduling_data.appointment_data)
    except Exception as e:
        print(f"Test failed with error: {e}")
        print("Browser will remain open for debugging. Press Enter to close...")
        input()  # This will pause execution and keep browser open
        raise  # Re-raise the exception to fail the test