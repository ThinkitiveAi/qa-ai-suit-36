from playwright.sync_api import Page, expect

def add_patient(page: Page, patient: dict):
    page.get_by_role("tab", name="Patients").click()
    page.get_by_text("Patient List").click()
    page.get_by_text("Create").click()
    page.get_by_text("New Patient").click()
    page.get_by_text("Enter Patient Details").click()
    page.get_by_role("button", name="Next").click()
    
    # PATIENT DETAILS
    page.locator("(//p[text()='Profile Picture']/following::input[@type='file'])[1]").set_input_files("./Automation/utils/uploads/patient.jpeg")
    print(f"Random Name: {patient.get('patient_fname')} {patient.get('patient_lname')}")
    page.locator("input[name=\"firstName\"]").fill(patient.get("patient_fname"))
    page.locator("input[name=\"lastName\"]").fill(patient.get("patient_lname"))
    page.locator("[id=\"Patient\\ Details\"]").get_by_placeholder("Choose Date").fill(patient.get("patient_dob")[0])
    page.locator("[id=\"Patient\\ Details\"]").get_by_placeholder("Select", exact=True).first.click()
    page.get_by_role("option", name=patient.get("patient_gender"), exact=True).click()
    page.locator("input[name=\"timezone\"]").click()
    page.get_by_role("option", name=patient.get("patient_timezone")).click()
    
    # CONTACT INFORMATION
    page.get_by_placeholder("Enter Number").first.fill(patient.get("patient_mob_num"))
    page.locator("input[name=\"email\"]").fill(patient.get("patient_email"))
    
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Patient Details Added Successfully.").click()
    page.wait_for_timeout(1000)