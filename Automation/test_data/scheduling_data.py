from playwright.sync_api import Page

from Automation.test_data import patient_data
from Automation.utils import constants, creds, data, local_data
from Automation.test_data.patient_data import PATIENT_MOB_NUM, PATIENT_EMAIL
appointmnt_status = ["Scheduled", "Confirmed", "Checked In", "Signed Off", "Cancelled", "No Show"]
appointment_data = {
    # "patient_name": "Andre Olson",
    "patient_name": f"{patient_data.PATIENT_FNAME} {patient_data.PATIENT_LNAME}",
    "cheif_complaint": "Fever and Chills",
    "new_appointment_note": "Patient has had fever and chills for two days. No cough or shortness of breath. Mild body aches present. Evaluation and tests recommended.",
    "instant_appointment_note": "Urgent visit scheduled to address patient’s acute concerns.",
    "icd_code": ["E119", "Type 2 diabetes mellitus without complications"],
    "icd_code_2": ["A010", "Typhoid fever"],
    "cpt_code": ["4509", "Unlisted laparoscopic procedure, liver"],
    "cpt_code2": ["90834","Psychotherapy"],
    "carePlan": "Diabetes Management Plan",
    "followUp": "Please continue taking medicines as prescribed",
    "signOffNote": "Patient consultation complete E11.9 - Type 2 diabetes mellitus without complications via virtual visit. Medical history, symptoms, and treatment plan reviewed and documented. Proceeding with sign-off."
}
def appointment_details(page: Page, appointment_status:str):
    page.get_by_role("tab", name="Appointment Details").click()
    # assert page.locator(f"//p[text()='Primary Provider']/following::p[text()='{local_data.provider1}']").is_visible(), "Primary Provider Is Not Visible"
    # assert page.locator(f"//p[text()='Primary Provider']/following::p[text()='Julie Mark']").is_visible(), "Primary Provider Is Not Visible"
    assert page.locator(f"//p[text()='Appointment Status']/following::p[text()='{appointment_status}']").is_visible(), "Appointment Status Is Not Visible"
    assert page.get_by_role("paragraph").filter(has_text=constants.appointment_type[0]).is_visible(), "Appointment Type Is Not Visible"
    assert page.get_by_role("paragraph").filter(has_text=appointment_data.get("cheif_complaint")).is_visible(), "Cheif Complaint Is Not Visible"

def insurance_details(page: Page):
    page.get_by_role("tab", name="Insurance Details").click()
    assert page.locator(f"//p[text()='Insurance Type']/following::p[text()='{patient_data.patient_data['insurance_order_of_benefits']} Insurance']").is_visible(), "Insurance Type Is Not Visible"
    assert page.locator(f"//p[text()='Payer Name']/following::p[text()='{constants.insurance[0]}']").is_visible(), "Payer Name Is Not Visible"
    assert page.locator(f"//p[text()='Insurance ID Number']/following::p[text()='{patient_data.patient_data['insurance_id']}']").is_visible(), "Insurance Id Is Not Available"
    
def verify_appointment_and_patient_details(page: Page, appointment_status, time, patientId):
    page.get_by_role("heading", name=appointment_status).get_by_text(appointment_status).click()
    page.get_by_text(f"{data.weekday} {data.day} {data.month} {data.year} at {time}").click()          # page.get_by_text("Sunday 9 Feb 2025 at 04:00 AM").click()
    
    page.locator(f"//p[@class='MuiTypography-root MuiTypography-body1 css-jt8q9e' and text()='{local_data.provider1}']").click()
    page.locator(f"//p[@class='MuiTypography-root MuiTypography-body1 css-1o3gpbg' and text()='{local_data.pg_name}']").click()

    page.get_by_role("heading", name=f"{appointment_data.get('patient_name')} ({patientId})").click(click_count=3)
    page.get_by_text(PATIENT_MOB_NUM, exact=True).click()
    page.get_by_text(PATIENT_EMAIL, exact=True).click()