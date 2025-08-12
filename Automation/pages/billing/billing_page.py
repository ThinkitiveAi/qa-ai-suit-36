from playwright.sync_api import Page, expect
from Automation.test_data.scheduling_data import appointment_data
from Automation.utils import creds, data, local_data

def super_bill_from_encounter_billing(page: Page, billing: dict, patientId):
    page.get_by_role("tab", name="Billing").click()
    page.get_by_role("menuitem", name="Billing").get_by_text("Billing").click()
    page.get_by_role("tab", name="Encounter For Billing").click()
    
    page.get_by_role("button", name="Filters").click()
    page.get_by_role("button", name="Clear Filter").click()
    page.get_by_role("button", name="Patient Name").click()
    page.get_by_placeholder("Search Patient").fill(billing['patient_name'])
    page.get_by_role("option", name=billing['patient_name']).click()
    page.get_by_role("button", name="Patient Name").click()
    page.get_by_role("button", name="Apply").click()
    page.wait_for_timeout(1000)
    
    page.locator(f"(//p[text()='{billing.get('patient_name')}']/following::div[@class='MuiBox-root css-gmuwbf'])[1]").click()
    
    page.get_by_role("menuitem", name="Create Superbill").click()
    page.get_by_role("heading", name="Create Super Bill").click()
    page.wait_for_timeout(1000) 
    # page.get_by_role("heading", name=f"{billing['patient_name']} ({patientId})").click()
    
    page.get_by_placeholder("Select Service Location").click()
    page.get_by_role("option", name=local_data.pg_location).click()
    
    page.locator("(//p[text()='Place Of Services']/following::input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name=billing['place_of_services'], exact=False).click()
    
    page.get_by_placeholder("Date Of Service").fill(data.two_days_ago)
    
    page.locator("(//p[text()='Service State']/following::input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="Alaska (AK)").click()  
       
    page.get_by_placeholder("Select Rendering Provider").fill(local_data.provider1)
    page.get_by_role("option", name=local_data.provider1).click()
    
    # page.get_by_placeholder("Prior Authorization").click()
    page.get_by_placeholder("Select Billing Provider").click()
    page.get_by_placeholder("Select Billing Provider").fill(local_data.provider2)
    page.get_by_role("option", name=local_data.provider2).click()
    page.get_by_placeholder("Select Referring Provider").fill(local_data.provider2)
    page.get_by_role("option", name=local_data.provider2).click()
    page.get_by_placeholder("Select Ordering Provider").fill(local_data.provider1)
    page.get_by_role("option", name=local_data.provider1).click()
    
    page.get_by_text("Diagnosis Code").click()
    page.locator(f"//p[text()='{appointment_data['icd_code'][0]}']/ancestor::div[@role='row']//div[text()='{appointment_data['icd_code'][1]}']").click(click_count=3)
    page.get_by_placeholder("Search & select ICD Code").fill(appointment_data['icd_code_2'][0])
    page.get_by_role("option", name=f"{appointment_data['icd_code_2'][0]} {appointment_data['icd_code_2'][1]}").click()
    page.locator(f"//p[text()='{appointment_data['icd_code_2'][0]}']").click(click_count=3)
    
    page.get_by_text("Procedure Code").click()
    # page.get_by_placeholder("Search & select CPT Code").fill(appointment_data['cpt_code'][0])
    # page.get_by_role("option", name=f"{appointment_data['cpt_code'][0]} - {appointment_data['cpt_code'][1]}").click()
    
    for i, j in zip(range(1,5), ["8P-Action not performed, Reas", "3P-PQRI Perf Measure Exclusio", "2P-PQRI Perf Measure Exclusio", "1P-PQRI Perf Measure Exclusio"]):
        page.locator(f"(//p[text()='Modifiers']/following::input[@placeholder='Select'])[{i}]").click()
        page.get_by_role("option", name=f"{j}").click()
    
    for i in range(1, 5):
        page.locator(f"(//p[text()='Diagnosis Pointer']/following::input[@type='text'])[{i}]").fill(f"{i}")

    page.locator("//input[@placeholder='Quantity']").fill("20")
    page.get_by_placeholder("Charges").fill("200")
    page.locator("(//p[text()='Discount Type']/following::input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="Percentage").click()
    
    page.get_by_placeholder("Discount").fill("10")
    page.wait_for_timeout(2000)
    
    assert billing["total_bill"] in page.get_by_placeholder("Total").input_value(), "Incorrect_Total"
    page.get_by_role("button", name="Save Bill").click()
    page.wait_for_timeout(1000) 
    
def super_bill(page: Page, billing: dict, patientId):
    page.get_by_role("tab", name="Billing", exact=True).click()
    page.get_by_role("menuitem", name="Billing").get_by_text("Billing").click()
    page.get_by_role("tab", name="Super Bill").click()
    page.get_by_role("button", name="Create Super Bill").click()
    page.get_by_role("heading", name="Create Super Bill").click()
    page.get_by_placeholder("Select Patient").click()
    page.get_by_placeholder("Select Patient").fill(f"{billing['patient_name']}")
    page.get_by_text(f"{billing['patient_name']}").click()
    page.wait_for_timeout(1000)
    # page.get_by_role("heading", name=f"{billing['patient_name']} ({patientId})").click(click_count=3)
    # Patient Details
    page.locator(f"//p[text()='Patient ID']/following::p[text()='{patientId}']").click()
    page.locator(f"//p[text()='Name']/following::p[text()='{billing['patient_name']}']").click()
    page.get_by_placeholder("Select Service Location").click()
    page.get_by_role("option", name=local_data.pg_location).click()
    
    page.locator("(//p[text()='Place Of Services']/following::input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name=billing["place_of_services"], exact=False).click()
    
    page.get_by_placeholder("Date Of Service").fill(data.two_days_ago)
    
    page.locator("(//p[text()='Service State']/following::input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="Alaska (AK)").click()  
    
    page.get_by_placeholder("Select Rendering Provider").fill(local_data.provider1)
    page.get_by_role("option", name=local_data.provider1).click()
    
    # page.get_by_placeholder("Prior Authorization").click()
    
    page.get_by_placeholder("Select Billing Provider").click()
    page.get_by_placeholder("Select Billing Provider").fill(local_data.provider2)
    page.get_by_role("option", name=local_data.provider2).click()
    page.get_by_placeholder("Select Referring Provider").fill(local_data.provider2)
    page.get_by_role("option", name=local_data.provider2).click()
    page.get_by_placeholder("Select Ordering Provider").fill(local_data.provider1)
    page.get_by_role("option", name=local_data.provider1).click()
    
    page.get_by_text("Diagnosis Code").click()
    page.get_by_placeholder("Search & select ICD Code").fill(appointment_data['icd_code'][0])
    page.get_by_role("option", name=f"{appointment_data['icd_code'][0]} {appointment_data['icd_code'][1]}").click()
    page.locator(f"//p[text()='{appointment_data['icd_code'][0]}']/ancestor::div[@role='row']//div[text()='{appointment_data['icd_code'][1]}']").click(click_count=3)
    
    page.get_by_text("Procedure Code").click()
    page.get_by_placeholder("Search & select CPT Code").fill(appointment_data['cpt_code'][0])
    page.get_by_role("option", name=f"{appointment_data['cpt_code'][0]} - {appointment_data['cpt_code'][1]}").click()
    
    page.locator("(//p[text()='Modifiers']/following::input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="8P-Action not performed, Reas").click()
    page.locator("(//p[text()='Modifiers']/following::input[@placeholder='Select'])[2]").click()
    page.get_by_role("option", name="3P-PQRI Perf Measure Exclusio").click()
    page.locator("(//p[text()='Modifiers']/following::input[@placeholder='Select'])[3]").click()
    page.get_by_role("option", name="2P-PQRI Perf Measure Exclusio").click()
    page.locator("(//p[text()='Modifiers']/following::input[@placeholder='Select'])[4]").click()
    page.get_by_role("option", name="1P-PQRI Perf Measure Exclusio").click()
    
    page.locator("(//p[text()='Diagnosis Pointer']/following::input[@type='text'])[1]").fill("1")
    page.locator("(//p[text()='Diagnosis Pointer']/following::input[@type='text'])[2]").fill("2")
    page.locator("(//p[text()='Diagnosis Pointer']/following::input[@type='text'])[3]").fill("3")
    page.locator("(//p[text()='Diagnosis Pointer']/following::input[@type='text'])[4]").fill("4")

    page.get_by_placeholder("Quantity").fill("20")
    page.get_by_placeholder("Charges").fill("200")
    page.locator("(//p[text()='Discount Type']/following::input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="Percentage").click()
    
    page.get_by_placeholder("Discount").fill("10")
    page.wait_for_timeout(2000)
    
    assert billing["total_bill"] in page.get_by_placeholder("Total").input_value(), "Incorrect_Total"
    page.get_by_role("button", name="Save Bill").click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("tab", name="Super Bill").click()
    page.get_by_role("button", name="Filters").click()
    page.get_by_role("button", name="Patient Name").click()
    page.get_by_placeholder("Search Patient").click()
    page.get_by_role("option", name=billing['patient_name']).click()
    page.get_by_role("button", name="Apply").click()
    
    # page.locator(f"(//p[text()='{billing['patient_name']}']/following::div[text()='{billing['place_of_services'].upper()}']/following::div[text()='{billing['total_bill']}']/following::div[@class='MuiBox-root css-gmuwbf'])[1]").click()