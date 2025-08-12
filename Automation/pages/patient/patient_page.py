from playwright.sync_api import Page, expect
from Automation.utils import constants, creds, local_data
from Automation.utils import data
from Automation.test_data import patient_data
common_class = "//div[contains(@class,'MuiGrid-container css-1d3bbye')]"

def create_patient(page: Page, patient: dict):
    page.get_by_role("tab", name="Patients").click()
    page.get_by_text("Patient List").click()
    page.get_by_text("Create").click()
    page.get_by_text("New Patient").click()
    page.get_by_text("Enter Patient Details").click()
    page.get_by_role("button", name="Next").click()
    
    # PROVIDER INFORMATION
    page.get_by_placeholder("Select Provider Group Location").click()
    page.get_by_role("option", name=local_data.pg_location1).click()
    page.get_by_placeholder("Select Primary Provider").click()
    page.get_by_role("option", name=local_data.provider1).click()
    page.locator("[id=\"Provider\\ Information\"]").get_by_placeholder("Choose Date").fill(data.today_date)
    page.locator("(//input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="SMS").click()
    
    # PATIENT DETAILS
    page.locator("(//p[text()='Profile Picture']/following::input[@type='file'])[1]").set_input_files("./Automation/utils/uploads/patient.jpeg")
    print(f"Random Name: {patient.get('patient_fname')} {patient.get('patient_lname')}")
    page.locator("input[name=\"firstName\"]").fill(patient.get("patient_fname"))
    page.locator("input[name=\"middleName\"]").fill("Shaun")
    page.locator("input[name=\"lastName\"]").fill(patient.get("patient_lname"))
    page.locator("[id=\"Patient\\ Details\"]").get_by_placeholder("Choose Date").fill(patient.get("patient_dob")[0])
    
    page.locator("[id=\"Patient\\ Details\"]").get_by_placeholder("Select", exact=True).first.click()
    page.get_by_role("option", name=patient.get("patient_gender"), exact=True).click()
    
    page.locator("[id=\"Patient\\ Details\"]").get_by_placeholder("Select", exact=True).nth(1).click()
    page.get_by_role("option", name=patient.get("patient_marital_status")).click()
    
    page.locator("input[name=\"timezone\"]").click()
    page.get_by_role("option", name=patient.get("patient_timezone")).click()
    
    page.locator("[id=\"Patient\\ Details\"]").get_by_placeholder("Select", exact=True).nth(3).click()
    page.get_by_role("option", name=patient.get("patient_language"), exact=True).click()
    
    page.get_by_placeholder("Enter SSN").fill(patient.get("patient_ssn"))
    page.get_by_placeholder("Enter MRN").fill(patient.get("patient_mrn"))
    page.get_by_placeholder("Select Race").click()
    page.get_by_role("option", name=patient.get("patient_race"), exact=True).click()
    page.get_by_placeholder("Select Ethnicity").click()
    page.get_by_role("option", name=patient.get("patient_ethnicity")).click()
    
    # CONTACT INFORMATION
    page.get_by_placeholder("Enter Number").first.fill(patient.get("patient_mob_num"))
    page.get_by_placeholder("Enter Number").nth(1).fill(patient.get("patient_home_num"))
    page.locator("input[name=\"email\"]").fill(patient.get("patient_email"))
    page.locator("input[name=\"faxNumber\"]").fill(patient.get("patient_fax_num"))
    page.locator("input[name=\"address\\.line1\"]").fill("Happy Street 1")
    page.locator("input[name=\"address\\.line2\"]").fill("Lane 2")
    page.locator("input[name=\"address\\.city\"]").fill("Santacruz")
    page.locator("[id=\"Contact\\ Information\"]").get_by_placeholder("Select State").click()
    page.get_by_role("option", name="California (CA)").click()
    page.locator("[id=\"Contact\\ Information\"]").get_by_placeholder("Select Country").click()
    page.get_by_role("option", name="United States").click()
    page.locator("input[name=\"address\\.zipcode\"]").fill("843842")
    
    # EMERGENCY CONTACT
    page.locator("//div[@id='Emergency Contact']").get_by_placeholder("Select").click()
    page.get_by_role("option", name=patient.get("relationship_with_patient"), exact=True).click()
    
    page.get_by_placeholder("Enter First Name").fill(patient.get("child_fname"))
    page.get_by_placeholder("Enter Last Name").fill(patient.get("child_lname"))
    page.locator("//div[@id='Emergency Contact']").get_by_placeholder("Enter Number").type(patient.get("emergency_contact"))
    page.locator("//input[@name='emergencyContacts[0].email']").fill(patient.get("emergency_email"))
    
    # INSURANCE"
    page.get_by_label("Payer Name").fill(constants.insurance[0])
    page.get_by_role("option", name=constants.insurance[0]).click()
    page.wait_for_timeout(1000)
    
    page.get_by_label("Plan Name").click()
    page.wait_for_timeout(1000)
    if(page.get_by_role("option", name=patient.get("insurance_plan_name")).first.is_visible(timeout=2000)):
        page.wait_for_timeout(500)
        page.get_by_role("option", name=patient.get("insurance_plan_name")).first.click()
        page.wait_for_timeout(500)
    else:
        page.get_by_role("button", name="Edit payer and plan details").click()
        page.get_by_placeholder("Plan Name").fill(patient.get("insurance_plan_name"))
        page.get_by_placeholder("Enter Plan Type").click()
        page.get_by_role("option", name=patient.get("insurance_plan_type")).click()
        page.get_by_placeholder("Type Note here").fill("Patient enrolled under BlueCare Advantage PPO through Affinity Health Plan. Coverage verified for medical services. No referral required for specialist visits.")
        page.get_by_role("button", name="Save").click()
        
    page.get_by_placeholder("Order of Benefits").click()
    page.get_by_role("option", name=patient.get("insurance_order_of_benefits")).click()
    
    page.get_by_placeholder("Enter Insurance ID").fill(patient.get("insurance_id"))
    page.get_by_placeholder("Enter Group ID").fill(patient.get("insurance_group_id"))
    page.locator("(//p[.='Effective Start Date']/following::input[@placeholder='MM-DD-YYYY'])[1]").fill(data.insurance_dt("-", "month"))
    page.locator("(//p[.='Effective End Date']/following::input[@placeholder='MM-DD-YYYY'])[1]").fill(data.insurance_dt("-", "year"))
    
    page.get_by_placeholder("Select Provider", exact=True).fill(local_data.provider1)
    page.get_by_role("option", name=local_data.provider1).click()
    
    page.locator("//p[.='Co-pay Amount']/following::div[1]//input[@placeholder='Enter Co-pay Amount']").fill(patient.get("insurance_copay_amount"))
    page.get_by_placeholder("Co-insurance Percentage").fill("20")
    page.get_by_placeholder("Deductable Amount").fill("1500")
    page.get_by_placeholder("Enter coverage Level").fill("Family")

    # page.locator("//p[.='Relationship to Insured']/following::div[1]//input[@placeholder='Select']").click()
    # page.get_by_role("option", name="Self").click()
    
    page.locator("//p[.='Upload Insurance Card']").click()
    page.locator("(//p[text()='Upload Insurance Card']/following::input[@type='file'])[1]").set_input_files("./Automation/utils/uploads/insurance1.jpg")
    page.locator("(//p[text()='Upload Insurance Card']/following::input[@type='file'])[2]").set_input_files("./Automation/utils/uploads/insurance2.jpg")
    
    # page.locator("input[name=\"patientInsurances\\[0\\]\\.insuredFirstName\"]").click()
    # page.locator("input[name=\"patientInsurances\\[0\\]\\.insuredLastName\"]").click()
    # page.locator("#Insurance").get_by_placeholder("Select", exact=True).nth(3).click()
    # page.get_by_role("option", name="Male", exact=True).click()
    # page.locator("//input[@name='patientInsurances[0].address.line1' and @placeholder='Enter Address Line 1']").fill("Streets of Europe")
    # page.locator("//input[@name='patientInsurances[0].address.line2' and @placeholder='Enter Address Line 2']").fill("Lane 4")
    # page.locator("//input[@name='patientInsurances[0].address.city' and @placeholder='Enter City']").fill("Miami")
    # page.locator("#Insurance").get_by_placeholder("Select State").click()
    # page.get_by_role("option", name="Florida (FL)").click()
    # page.locator("#Insurance").get_by_placeholder("Select Country").click()
    # page.get_by_role("option", name="United States").click()
    # page.locator("input[name=\"patientInsurances\\[0\\]\\.address\\.zipcode\"]").fill("236765")

    
    # # PREFERENCES
    # page.locator("(//p[text()='Add New Preferences'])[1]").click()
    # page.get_by_role("heading", name="Add New Pharmacy").click(click_count=3)
    # page.get_by_placeholder("Enter Pharmacy Name").fill("Wellness Pharmacy")
    # # page.locator("//input[@placeholder='Address Line 1']").fill("Kenny Wren Rd")
    # # page.locator("//input[@placeholder='Address Line 2']").fill("546")
    # # page.locator("//input[@placeholder='City']").fill("Dillingham")
    # # page.get_by_role("combobox", name="Select", exact=True).click()
    # # page.get_by_role("option", name="Alaska (AK)").click()
    
    # # page.get_by_role("combobox", name="Select Country", exact=True).click()
    # # page.get_by_role("option", name="United States").click()
    # # page.get_by_placeholder("Zip Code", exact=True).fill("99576")
    # page.get_by_role("textbox", name="Enter Fax Number").fill("(312) 895-1902")
    # page.get_by_placeholder("Enter Contact Number").fill("(647) 747-7435")
    # page.get_by_role("button", name="Save Pharmacy").click()
    
    page.locator("//p[text()='Preferences']/following::div[1]//input[@placeholder='Select']").click()
    for x in local_data.preferences:
        page.get_by_role("option", name=x).click()
    page.get_by_role("cell", name=x).click()
    
    # Consent
    page.get_by_label("Consent to Email").check()
    page.get_by_label("Consent to Call").check()
    page.get_by_label("Consent to Message").check()
    
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Patient Details Added Successfully.").click()
    page.wait_for_timeout(1000)
    print("Patient Added Successfully")
    page.get_by_placeholder("Search Patient").click()
    page.get_by_placeholder("Search Patient").fill(f"{patient.get('patient_fname')} {patient.get('patient_lname')}")
    page.wait_for_timeout(2000)
    page.wait_for_load_state
    # verification in patient list
    page.get_by_role("cell", name="05/22/1985").click()
    page.get_by_text(patient.get("patient_mob_num")).click()
    page.get_by_text(local_data.provider1).click(click_count=3)
    page.get_by_text("Active").click(click_count=3)
    page.get_by_text(f"{patient.get('patient_fname')} {patient.get('patient_lname')}").click(click_count=3)
    print(f"Created Patient : {patient.get('patient_fname')} {patient.get('patient_lname')}")
    
    page.get_by_role("heading", name=f"{patient.get('patient_fname')} {patient.get('patient_lname')}").click()
    page.get_by_text(patient.get("patient_mob_num")).first.click()
    page.get_by_label(patient.get("patient_email")).hover()
    page.get_by_role("tooltip", name=patient.get("patient_email")).get_by_text(patient.get("patient_email")).click()

    page.get_by_role("tab", name="Demographics").click()
    page.wait_for_timeout(1000)
    # Demographics > BASIC INFORMATION
    for label, value, message in patient_data.basic_information:
        assert page.locator(f"{common_class}[div/p[text()='{label}'] and div/p[text()='{value}']]").is_visible(), message
    
    # Demographics > REGISTERING INFORMATION
    for attr_value, label, value, message in patient_data.registering_information:
        assert page.locator(f"{attr_value}[div/p[text()='{label}'] and div/p[text()='{value}']]").is_visible(), message 
    
    # Demographics > EMERGENCY CONTACT
    page.locator(f"//div[text()='{patient_data.patient_data['relationship_with_patient']}']/following::div[text()='{patient_data.patient_data['child_fname']} {patient_data.patient_data['child_lname']}']/following::div[text()='{patient_data.patient_data['emergency_contact']}']/following::div[text()='{patient_data.patient_data['emergency_email']}']").click(click_count=3)

    # Consent
    page.locator("//p[text()='Privacy Consent']/following::p[contains(text(),'Email')]/following::div[1]//p[text()='Yes']").click()
    page.locator("//p[text()='Privacy Consent']/following::p[contains(text(),'Call')]/following::div[1]//p[text()='Yes']").click()
    page.locator("//p[text()='Privacy Consent']/following::p[contains(text(),'Message')]/following::div[1]//p[text()='Yes']").click()
    
    # PREFERENCES
    for x in local_data.preferences:
        page.get_by_role("cell", name=x).click()
           
    # Insurance
    page.get_by_role("tab", name="Insurance").click()
    page.wait_for_timeout(1000)
    page.get_by_role("heading", name=f"{patient['insurance_plan_name']} INSURANCE")
    for label, value, message in patient_data.insurance_info:
        assert page.locator(f"{common_class}[div/p[text()='{label}'] and div/p[text()='{value}']]").is_visible(), message
    
    page.get_by_role("tab", name="Eligibility").click()
    page.get_by_role("tab", name="Authorization").click()
    return page