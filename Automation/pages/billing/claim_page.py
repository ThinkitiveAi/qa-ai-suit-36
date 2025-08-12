from playwright.sync_api import Playwright, sync_playwright, expect, Page

from Automation.test_data import scheduling_data
from Automation.utils import constants, data, local_data

provider_account_details = [{
    "bank_name": "State Bank of India",
    "routing_number": "110000000",
    "branch_code": "SBI123",
    "branch_address": "123 MG Road, Mumbai, Maharashtra",
    "account_type": "Savings",
    "account_number": "9876543210"
},
{
    "bank_name": "HDFC Bank",
    "routing_number": "220000000",
    "branch_code": "HDFC456",
    "branch_address": "456 Park Street, Kolkata, West Bengal",
    "account_type": "Business Savings",
    "account_number": "1234567890"
}]

modifiers = [
        "8P-Action not performed, Reas",
        "3P-PQRI Perf Measure Exclusio",
        "2P-PQRI Perf Measure Exclusio",
        "1P-PQRI Perf Measure Exclusio"
    ]
def claim_filter(page: Page, appointment: dict):
    page.get_by_role("tab", name="Billing").click()
    page.get_by_role("menuitem", name="Billing").get_by_text("Billing").click()
    page.get_by_role("tab", name="Claims").click()
    page.get_by_role("heading", name="Submitted Claims").click()
    
    page.get_by_role("button", name="Filters").click()
    page.get_by_role("button", name="Clear Filter").click()

    page.get_by_role("button", name="Claim Status").click()
    page.get_by_placeholder("Claim Status").click()
    page.get_by_role("option", name="Submitted").click()
    page.get_by_role("button", name="Claim Status").click()
    
    page.get_by_role("button", name="Patients").click()
    page.get_by_placeholder("Patients").fill(appointment['patient_name'])
    page.get_by_role("option", name=appointment['patient_name']).click()
    page.get_by_role("button", name="Patients").click()
    
    page.get_by_role("button", name="Providers").click()
    page.get_by_placeholder("providers").click()
    page.get_by_role("option", name=local_data.provider1).click()
    page.get_by_role("button", name="Providers").click()
    page.get_by_role("button", name="Apply").click()
    
def add_claim_modifiers(page: Page):
    for i, j in zip(range(1,5), modifiers):
        page.locator(f"(//p[text()='Modifiers']/following::input[@placeholder='Select'])[{i}]").click()
        page.get_by_role("option", name=f"{j}").click()
       
    for i, j in zip(range(1,5), ["A", "B", "C", "D"]):
        page.locator(f"(//p[text()='Diagnosis Pointer']/following::input[@type='text'])[{i}]").fill(j)

def edit_claim_modifiers(page: Page, cpt: dict, expected_total: str):
    for i, j in zip(range(1,5), modifiers):
        page.locator(f"(//h6[text()='{cpt['cpt_code2'][0]} - {cpt['cpt_code2'][1]}']/ancestor::div[@class='MuiBox-root css-1mqt0j0']//input[@placeholder='Select'])[{i}]").click()
        page.get_by_role("option", name=f"{j}").click()
        
    for i, j in zip(range(1,5), ["A", "B", "C", "D"]):
        page.locator(f"(//h6[text()='{cpt['cpt_code2'][0]} - {cpt['cpt_code2'][1]}']/following::p[text()='Diagnosis Pointer']/following::input[@type='text'])[{i}]").fill(j)
        
    page.locator(f"//h6[text()='{cpt['cpt_code2'][0]} - {cpt['cpt_code2'][1]}']/ancestor::div[@class='MuiBox-root css-1mqt0j0']//input[@placeholder='Quantity']").fill("10")
    page.locator(f"//h6[text()='{cpt['cpt_code2'][0]} - {cpt['cpt_code2'][1]}']/ancestor::div[@class='MuiBox-root css-1mqt0j0']//input[@placeholder='Charges']").fill("100")
    page.locator(f"(//h6[text()='{cpt['cpt_code2'][0]} - {cpt['cpt_code2'][1]}']/ancestor::div[@class='MuiBox-root css-1mqt0j0']//p[text()='Discount Type']/following::input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="Amount").click()
    page.locator(f"//h6[text()='{cpt['cpt_code2'][0]} - {cpt['cpt_code2'][1]}']/ancestor::div[@class='MuiBox-root css-1mqt0j0']//input[@placeholder='Discount']").fill("50")
    page.wait_for_timeout(2000)
    
    assert "950" in page.locator(f"//h6[text()='{cpt['cpt_code2'][0]} - {cpt['cpt_code2'][1]}']/ancestor::div[@class='MuiBox-root css-1mqt0j0']//input[@placeholder='Total']").input_value(), "Incorrect_Total"
    page.wait_for_timeout(1000)
    expect(page.locator(f"//p[text()='Procedural Charges']/following::p[.='Total']/following::p[.='${expected_total}.00']")).to_be_visible()
    
def fill_provider_account_details(page: Page, account: dict):
    page.get_by_text("Provider Account Details").click()
    page.wait_for_timeout(500)
    page.get_by_placeholder("Enter Bank Name").click()
    page.get_by_placeholder("Enter Bank Name").fill(account["bank_name"])
    page.wait_for_timeout(300)
    page.get_by_placeholder("Enter Routing Number").click()
    page.get_by_placeholder("Enter Routing Number").fill(account['routing_number'])
    page.get_by_placeholder("Enter Branch Code").click()
    page.get_by_placeholder("Enter Branch Code").fill(account["branch_code"])
    page.get_by_placeholder("Enter Branch Address").click()
    page.get_by_placeholder("Enter Branch Address").fill(account["branch_address"])
    page.get_by_placeholder("Select Account Type").click()
    page.get_by_role("option", name=account["account_type"], exact=True).click()
    page.get_by_placeholder("Enter Account Number").click()
    page.get_by_placeholder("Enter Account Number").fill(account["account_number"])

def view_claim(page: Page, appointment: dict, account: dict, total):
    page.get_by_text("View Claim").click()
    page.get_by_role("heading", name="View Claim").click()
    page.get_by_role("heading", name=appointment['patient_name']).click()
    page.get_by_role("cell", name=appointment['icd_code'][0]).click()
    page.get_by_role("cell", name=appointment['icd_code'][1]).click()
    assert page.get_by_placeholder("Select Rendering Provider").input_value()==local_data.provider1
    expect(page.get_by_placeholder("Total")).to_have_value(total)
    expect(page.get_by_placeholder("Enter Bank Name")).to_have_value(account['bank_name'])
    expect(page.get_by_placeholder("Enter Routing Number")).to_have_value(account['routing_number'])
    expect(page.get_by_placeholder("Enter Branch Code")).to_have_value(account['branch_code'])
    expect(page.get_by_placeholder("Enter Branch Address")).to_have_value(account['branch_address'])
    expect(page.get_by_placeholder("Select Account Type")).to_have_value(account['account_type'])
    expect(page.get_by_placeholder("Enter Account Number")).to_have_value(account['account_number'])
    page.get_by_test_id("ArrowBackIcon").click()

def edit_claim(page: Page, expected_total: str):
    page.get_by_test_id("MoreVertIcon").first.click()
    page.get_by_role("menuitem", name="Edit Claim").click()
    page.get_by_placeholder("Search & select ICD Code").fill(f"{scheduling_data.appointment_data['icd_code_2'][0]}")
    page.get_by_role("option", name=f"{scheduling_data.appointment_data['icd_code_2'][0]} {scheduling_data.appointment_data['icd_code_2'][1]}").click()
    page.wait_for_timeout(400)
    page.get_by_text(f"{scheduling_data.appointment_data['icd_code_2'][1]}").click()
    page.get_by_placeholder("Search & select CPT Code").fill(f"{scheduling_data.appointment_data['cpt_code2'][0]}")
    page.get_by_role("option", name=f"{scheduling_data.appointment_data['cpt_code2'][0]} - {scheduling_data.appointment_data['cpt_code2'][1]}").click()  
    page.wait_for_timeout(1000)
    if page.locator(f"//h6[text()='{scheduling_data.appointment_data['cpt_code2'][0]} - {scheduling_data.appointment_data['cpt_code2'][1]}']").is_visible():
        edit_claim_modifiers(page, scheduling_data.appointment_data, expected_total)
        fill_provider_account_details(page, provider_account_details[1])
    page.get_by_role("button", name="Submit Claim").click()
    page.get_by_text("Claim updated successfully").click()
    page.wait_for_timeout(200)
    page.get_by_title("Close").click()
    page.get_by_role("heading", name="Please Select Claim Type For Submission").get_by_test_id("CloseIcon").click()

def delete_claim(page: Page):
    page.get_by_test_id("MoreVertIcon").first.click()
    page.get_by_role("menuitem", name='Delete Claim').click()
    page.get_by_text("Are You Sure?").click()
    page.get_by_text("you want to delete this Claim").click()
    page.get_by_role("button", name="Yes,Sure").click()
    page.get_by_text("Claim archive successfully").click()
    page.get_by_role("button", name="Close").click() 

def claim_from_encounter(page: Page, appointment: dict) -> None:
    page.get_by_role("tab", name="Billing", exact=True).click()
    page.get_by_role("menuitem", name="Billing").get_by_text("Billing").click()
    page.get_by_role("tab", name="Encounter For Billing").click()
    page.get_by_role("button", name="Filters").click()
    page.get_by_role("button", name="Patient Name").click()
    page.get_by_placeholder("Search Patient").fill(appointment["patient_name"])
    page.get_by_role("option", name=appointment["patient_name"]).click()
    page.wait_for_timeout(400)
    page.get_by_role("button", name="Apply").click()
    page.wait_for_timeout(2000)
    
    page.get_by_test_id("MoreVertIcon").click()
    page.get_by_text("Create Claim").click()
    page.get_by_role("heading", name="Create Claim").get_by_text("Create Claim").click(click_count=3)
    page.wait_for_timeout(1000)
    assert page.get_by_placeholder("Search Patient").input_value() == appointment['patient_name'], "patient name not auto-filled"
    assert page.get_by_placeholder("Select Encounter").input_value() == constants.appointment_type[0], "Encounter type not auto-filled"
    page.get_by_placeholder("Select Service Location").click()
    page.get_by_role("option", name=local_data.pg_location).click()
    page.get_by_placeholder("Select", exact=True).click()
    page.get_by_role("option", name="12 - Home").click()
    page.get_by_placeholder("Date Of Service").click()
    page.get_by_placeholder("Date Of Service").fill(data.dt_format(data.current_date, "-"))
    assert page.get_by_placeholder("Select Rendering Provider").input_value() == local_data.provider1, "Rendering Provider not auto-filled"
    page.get_by_placeholder("Select Referring Provider").fill(local_data.provider2)
    page.get_by_role("option", name=local_data.provider2).click()
    assert page.get_by_placeholder("Select Appoinment Type").input_value() == constants.appointment_type[0], "Appoinment Type not auto-filled"
    page.get_by_placeholder("Search & Select Insurance").click()
    page.get_by_text(constants.insurance[0]).click()
    assert page.get_by_placeholder("Reason for Visit").input_value() == appointment['cheif_complaint'], "Reason for Visit not auto-filled"
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Claim added successfully").click()
    page.wait_for_timeout(200)
    page.get_by_role("button", name="Close").click()
    
    page.wait_for_timeout(1000)
    page.get_by_role("heading", name=appointment["patient_name"]).click()
    
    page.get_by_placeholder("Select Rendering Provider").click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name=local_data.provider1).click()
    page.wait_for_timeout(300)
    
    page.locator(f"//p[.='{appointment['icd_code'][0]}']/following::div/div[.='{appointment['icd_code'][1]}']").click()
    # page.get_by_role("heading", name=f"{appointment['cpt_code'][0]} - {appointment['cpt_code'][1]}").click()
    
    add_claim_modifiers(page)
    
    page.locator("//input[@placeholder='Quantity']").fill("50")
    page.get_by_placeholder("Charges").fill("200")
    page.locator("(//p[text()='Discount Type']/following::input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="Percentage").click()
    
    page.get_by_placeholder("Discount").fill("10")
    page.wait_for_timeout(2000)
    
    assert "9000" in page.get_by_placeholder("Total").input_value(), "Incorrect_Total"
    page.wait_for_timeout(1000)
    
    fill_provider_account_details(page, provider_account_details[0])
    
    page.get_by_text("IS PATIENT CONDITION RELATED TO").click()
    page.get_by_placeholder("Enter Claim Code (10d)").click()
    page.get_by_text("Dates patient unable to work in current occupation (16)").click()
    page.get_by_role("button", name="Submit Claim").click()
    page.get_by_text("Claim updated successfully").click()
    page.wait_for_timeout(200)
    page.get_by_title("Close").click()
    page.get_by_role("heading", name="Please Select Claim Type For Submission").get_by_test_id("CloseIcon").click()
    
    claim_filter(page, scheduling_data.appointment_data)
    page.locator(f"//div[text()='{data.dt_format(data.current_date, '/')}']/following::p[.='{appointment['patient_name']}']/following::span[.='{constants.insurance[0]}']/following::p[text()='{local_data.provider1}']/following::div[.='$ 9000']/following::div[text()='{data.dt_format(data.current_date, '/')}']/following::span[.='Submitted']/following::div[@class='MuiBox-root css-gmuwbf']").first.click()
    view_claim(page, scheduling_data.appointment_data, provider_account_details[0], "9000")
    
    amount = "9950"
    edit_claim(page, amount)
    claim_filter(page, scheduling_data.appointment_data)
    page.locator(f"//div[text()='{data.dt_format(data.current_date, '/')}']/following::p[.='{appointment['patient_name']}']/following::span[.='{constants.insurance[0]}']/following::p[text()='{local_data.provider1}']/following::div[.='$ {amount}']/following::div[text()='{data.dt_format(data.current_date, '/')}']/following::span[.='Submitted']").first.click(click_count=3)
    delete_claim(page)
    
def claim_from_superbill(page: Page, appointment: dict, billing: dict) -> None:
    page.get_by_role("tab", name="Billing", exact=True).click()
    page.get_by_role("menuitem", name="Billing").get_by_text("Billing").click()
    page.get_by_role("tab", name="Super Bill").click()
    page.get_by_role("button", name="Filters").click()
    page.get_by_role("button", name="Clear Filter").click()
    page.get_by_role("button", name="Patient Name").click()
    page.get_by_placeholder("Search Patient").fill(appointment["patient_name"])
    page.get_by_role("option", name=appointment["patient_name"]).click()
    page.wait_for_timeout(400)
    page.get_by_role("button", name="Apply").click()
    page.wait_for_timeout(2000)
    
    page.locator(f"//p[text()='-']/following::p[text()='{appointment['patient_name']}']/ancestor::div[@class='even MuiDataGrid-row Mui-hovered']//div[@class='MuiBox-root css-gmuwbf']").click()
    page.get_by_text("Create Claim").click()
    page.get_by_role("heading", name="Create Claim").get_by_text("Create Claim").click(click_count=3)
    page.wait_for_timeout(1000)
    page.get_by_role("heading", name=appointment["patient_name"]).click()

    expect(page.get_by_placeholder("Select Rendering Provider")).to_have_value(local_data.provider1, timeout=10000)
    # assert page.get_by_placeholder("Select Rendering Provider").input_value() == local_data.provider1, "Rendering Provider not auto-filled"
    
    page.locator(f"//p[.='{appointment['icd_code'][0]}']/following::div/div[.='{appointment['icd_code'][1]}']").click()
    # page.get_by_role("heading", name=f"{appointment['cpt_code'][0]} - {appointment['cpt_code'][1]}").click()
    
    # page.locator("//input[@placeholder='Quantity']").fill("50")
    # page.get_by_placeholder("Charges").fill("200")
    # page.locator("(//p[text()='Discount Type']/following::input[@placeholder='Select'])[1]").click()
    # page.get_by_role("option", name="Percentage").click()
    
    # page.get_by_placeholder("Discount").fill("10")
    # page.wait_for_timeout(2000)
    
    assert billing["total_bill"] in page.get_by_placeholder("Total").input_value(), "Incorrect_Total"
    page.wait_for_timeout(1000)
    
    fill_provider_account_details(page, provider_account_details[0])
    
    page.get_by_text("IS PATIENT CONDITION RELATED TO").click()
    page.get_by_placeholder("Enter Claim Code (10d)").click()
    page.get_by_text("Dates patient unable to work in current occupation (16)").click()
    
    page.get_by_role("button", name="Submit Claim").click()
    page.get_by_text("Claim added successfully").click()
    page.get_by_title("Close").click()
    page.get_by_role("heading", name="Please Select Claim Type For Submission").get_by_test_id("CloseIcon").click()
    
    claim_filter(page, scheduling_data.appointment_data)
    
    page.locator(f"//div[text()='{data.dt_format(data.current_date, '/')}']/following::p[.='{appointment['patient_name']}']/following::span[.='{constants.insurance[0]}']/following::p[text()='{local_data.provider1}']/following::div[.='$ {billing['total_bill']}']/following::div[text()='{data.dt_format(data.current_date, '/')}']/following::span[.='Submitted']/following::div[@class='MuiBox-root css-gmuwbf']").first.click()
    page.wait_for_timeout(1500)
    view_claim(page, scheduling_data.appointment_data, provider_account_details[0], billing["total_bill"])
    
    amount = "4550"
    edit_claim(page, amount)
    claim_filter(page, scheduling_data.appointment_data)
    page.locator(f"//div[text()='{data.dt_format(data.current_date, '/')}']/following::p[.='{appointment['patient_name']}']/following::span[.='{constants.insurance[0]}']/following::p[text()='{local_data.provider1}']/following::div[.='$ {amount}']/following::div[text()='{data.dt_format(data.current_date, '/')}']/following::span[.='Submitted']").first.click(click_count=3)
    delete_claim(page)
    
def claims(page: Page, appointment: dict):
    # page.get_by_role("tab", name="Billing").click()
    ## page.get_by_role("menuitem", name="Billing").get_by_text("Billing").click()
    page.get_by_role("tab", name="Claims").click()
    
    for chart in ["Draft Claims",
        "Submitted Claims",
        "Denied Claims",
        "Accepted Claims",
        "Rejected Claims"
        ]:
        page.get_by_role("heading", name=f"{chart}").click(click_count=3)
    
    page.get_by_text("Create Claim").click()
    page.get_by_role("menuitem", name="Create New Claim").click()
    page.get_by_role("heading", name="Create Claim").get_by_text("Create Claim").click()
    
    page.get_by_placeholder("Search Patient").click()
    page.get_by_text(appointment['patient_name']).click()
    page.get_by_placeholder("Select Encounter").click()
    page.get_by_text("New Patient Visit", exact=True).click()
    page.get_by_placeholder("Select Service Location").click()
    page.get_by_role("option", name=local_data.pg_location1).click()
    page.get_by_placeholder("Select", exact=True).click()
    page.get_by_role("option", name="17 - Walk-in Retail Health Clinic").click()
    page.get_by_placeholder("Date Of Service").click()
    page.get_by_placeholder("Date Of Service").fill(data.dt_format(data.current_date, "-"))
    page.get_by_placeholder("Select Rendering Provider").fill(local_data.provider1)
    page.wait_for_timeout(300)
    page.get_by_role("option", name=local_data.provider1).click()
    page.get_by_placeholder("Select Referring Provider").fill(local_data.provider2)
    page.get_by_role("option", name=local_data.provider2).click()
    page.get_by_placeholder("Select Appoinment Type").click()
    page.get_by_role("option", name=constants.appointment_type[0]).click()
    page.get_by_placeholder("Search & Select Insurance").click()
    page.get_by_text(constants.insurance[0]).click()
    page.get_by_placeholder("Reason for Visit").fill("cheif_complaint")
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Claim added successfully").click()
    page.wait_for_timeout(200)
    page.get_by_role("button", name="Close").click()
    
    page.get_by_placeholder("Select Rendering Provider").click()
    page.get_by_role("option", name=local_data.provider1).click()
    page.locator(f"//p[.='{appointment['icd_code'][0]}']/following::div/div[.='{appointment['icd_code'][1]}']").click()
    
    # page.get_by_role("heading", name=f"{appointment['cpt_code'][0]} - {appointment['cpt_code'][1]}").click()
    
    add_claim_modifiers(page)
    
    page.locator("//input[@placeholder='Quantity']").fill("60")
    page.get_by_placeholder("Charges").fill("300")
    page.locator("(//p[text()='Discount Type']/following::input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="Percentage").click()
    
    page.get_by_placeholder("Discount").fill("20")
    page.wait_for_timeout(2000)
    
    assert "14400" in page.get_by_placeholder("Total").input_value(), "Incorrect_Total"
    page.wait_for_timeout(1000)
    
    fill_provider_account_details(page, provider_account_details[0])
    
    page.get_by_text("IS PATIENT CONDITION RELATED TO").click()
    page.get_by_placeholder("Enter Claim Code (10d)").click()
    page.get_by_text("Dates patient unable to work in current occupation (16)").click()
    page.get_by_label("Resubmission Code(22)").click()
    page.get_by_label("Acceptance Assignment (27)").click()
    page.get_by_role("button", name="Submit Claim").click()
    page.get_by_text("Claim updated successfully").click()
    page.wait_for_timeout(200)
    page.get_by_title("Close").click()
    
    claim_filter(page, scheduling_data.appointment_data)
    
    page.locator(f"//div[text()='{data.dt_format(data.current_date, '/')}']/following::p[.='{appointment['patient_name']}']/following::span[.='{constants.insurance[0]}']/following::p[text()='{local_data.provider1}']/following::div[.='$ 14400']/following::div[text()='{data.dt_format(data.current_date, '/')}']/following::span[.='Submitted']/following::div[@class='MuiBox-root css-gmuwbf']").first.click()
    page.wait_for_timeout(1500)
    view_claim(page, scheduling_data.appointment_data, provider_account_details[0], "14400")
    
    amount = "15350"
    edit_claim(page, amount)
    claim_filter(page, scheduling_data.appointment_data)
    page.locator(f"//div[text()='{data.dt_format(data.current_date, '/')}']/following::p[.='{appointment['patient_name']}']/following::span[.='{constants.insurance[0]}']/following::p[text()='{local_data.provider1}']/following::div[.='$ {amount}']/following::div[text()='{data.dt_format(data.current_date, '/')}']/following::span[.='Submitted']").first.click(click_count=3)
    delete_claim(page)
    
    # page.get_by_test_id("MoreVertIcon").first.click()
    # page.get_by_role("menuitem", name='View Claim').click()