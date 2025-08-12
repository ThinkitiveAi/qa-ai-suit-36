from playwright.sync_api import Page
from Automation.utils import constants
from Automation.utils import creds, local_data

def provider_user(page: Page, provider: dict):
    page.get_by_role("tab", name="Settings").click()
    # User Settings
    page.get_by_text("User Settings").click()
    # Providers
    page.get_by_role("tab", name="Providers").click()
    # Add
    page.get_by_role("button", name="Add Provider User").click()
    page.get_by_placeholder("First Name").fill(provider.get("fname"))
    page.get_by_placeholder("Last Name").fill(provider.get("lname"))
    print("Provider User Name :", provider.get("fname"), provider.get("lname"))
    page.locator("(//input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="PA").click()
    page.locator("(//input[@placeholder='Select'])[2]").click()
    for i in constants.speciality[3:]:
        page.get_by_role("option", name=i).click()
    page.wait_for_timeout(1000)
    page.locator("(//input[@placeholder='Select'])[2]").click()
    page.get_by_role("option", name=provider.get("role")).click()
    page.get_by_placeholder("Choose Date").fill(provider.get("dob"))
    page.locator("(//input[@placeholder='Select'])[3]").click()
    page.get_by_role("option", name=provider.get("gender"), exact=True).click()
    page.locator("input[name=\"npi\"]").fill(provider.get("npi_number"))
    page.get_by_placeholder("Enter Contact Number").type(provider.get("contact_num"))
    page.locator("input[name=\"officeFaxNumber\"]").fill(provider.get("fax_num"))
    page.locator("(//input[@placeholder='Select'])[4]").click()
    for x in constants.insurance:
        page.get_by_role("option", name=x).click()
    page.get_by_placeholder("Enter Year Of Experience").fill(provider.get("yearOfExperience"))
    page.locator("input[name=\"taxonomyNumber\"]").fill(provider.get("taxonomy_num"))
    page.locator("(//input[@placeholder='Select'])[4]").click()
    page.get_by_role("option", name=local_data.pg_location1).click()
    page.get_by_placeholder("Enter Email").fill(provider.get("email"))
    page.locator("(//input[@placeholder='Select'])[4]").click()
    page.get_by_role("option", name="Indian Standard Time (UTC +5:30)").click()
    
    page.locator("(//input[@placeholder='Select'])[5]").click()
    page.get_by_role("option", name=provider.get("state"))
    page.locator("input[name=\"licenseNumber\"]").fill(provider.get("license_num"))
    page.get_by_placeholder("Enter Bio").fill(provider.get("bio"))
    page.get_by_placeholder("Enter Expertise ").fill(provider.get("expertise"))
    page.get_by_placeholder("Enter Education, Work Experience").fill(provider.get("workExperience"))
    
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Provider created successfully.").click()
    page.wait_for_timeout(1000)
    
    # verification
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill(f"{provider.get('fname')} {provider.get('lname')}")
    page.get_by_role("heading", name=f"{provider.get('fname')} {provider.get('lname')}").click()
    page.get_by_text(provider.get("contact_num")).click()
    # page.locator(f"//p[@aria-label={provider.get('email')}]").click()
    # View Profile
    page.get_by_role("button", name="View Profile").click()
    page.get_by_title("View Provider User").get_by_text(f"{provider.get('fname')} {provider.get('lname')}").click()
    page.get_by_text("PA", exact=True).click()      # Provider Type
    page.get_by_text(provider.get("gender")).click()
    page.get_by_text(provider.get("dob")).click()
    page.get_by_title("View Provider User").get_by_text(provider.get("contact_num")).click()
    page.get_by_text(provider.get("email")).click()
    page.get_by_text(provider.get("npi_number")).click()
    page.get_by_text(provider.get("bio")).click()
    page.get_by_text(provider.get("fax_num")).click()
    page.get_by_text(provider.get("taxonomy_num")).click()
    # page.get_by_text("1.undefined (6894697732) ( undefined)").click()       # Licensed Details
    page.get_by_text("IST (Indian Standard Time (UTC +5:30))").click()
    page.get_by_text(local_data.pg_location1).click()
    # page.get_by_text(f"1. American LIFECARE").click()
    # page.get_by_text(f"2. American Medical Security Inc.").click()
    page.get_by_text(provider.get("yearOfExperience")).click()
    page.get_by_text(provider.get("workExperience")).click()
    page.get_by_test_id("CloseIcon").click()
    
    # Edit Profile
    page.get_by_role("button", name="Edit Profile").click()
    
    page.get_by_placeholder("First Name").fill(provider.get("edit_fname"))
    page.get_by_placeholder("Last Name").fill(provider.get("edit_lname"))
    print("Provider User Name :", provider.get("edit_fname"), provider.get("edit_lname"))
    page.locator("(//input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="MD").click()
    # page.locator("(//input[@placeholder='Select'])[2]").click()
    # for i in constants.speciality[3:]:
    #     page.get_by_role("option", name=i).click()
    page.wait_for_timeout(1000)
    page.locator("(//input[@placeholder='Select'])[2]").click()
    page.get_by_role("option", name=provider.get("edit_role")).click()
    page.get_by_placeholder("Choose Date").fill(provider.get("edit_dob"))
    page.locator("(//input[@placeholder='Select'])[3]").click()
    page.get_by_role("option", name=provider.get("edit_gender"), exact=True).click()
    page.locator("input[name=\"npi\"]").fill(provider.get("edit_npi_number"))
    page.get_by_placeholder("Enter Contact Number").type(provider.get("edit_contact_num"))
    page.locator("input[name=\"officeFaxNumber\"]").fill(provider.get("edit_fax_num"))
    # page.locator("(//input[@placeholder='Select'])[4]").click()
    # for x in constants.insurance:
    #     page.get_by_role("option", name=x).click()
    page.get_by_placeholder("Enter Year Of Experience").fill(provider.get("edit_yearOfExperience"))
    page.locator("input[name=\"taxonomyNumber\"]").fill(provider.get("edit_taxonomy_num"))
    
    page.get_by_role("button", name=local_data.pg_location1).hover()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Clear").click()
    page.wait_for_timeout(500)
    page.locator("(//input[@placeholder='Select'])[4]").click()
    page.get_by_role("option", name=local_data.pg_location).click()
    
    page.get_by_placeholder("Enter Email").fill(provider.get("edit_email"))
    page.locator("(//input[@placeholder='Select'])[4]").click()
    page.get_by_role("option", name="Indian Standard Time (UTC +5:30)").click()
    
    page.locator("(//input[@placeholder='Select'])[5]").click()
    page.get_by_role("option", name=provider.get("edit_state"))
    page.locator("input[name=\"licenseNumber\"]").fill(provider.get("edit_license_num"))
    page.get_by_placeholder("Enter Bio").fill(provider.get("edit_bio"))
    page.get_by_placeholder("Enter Expertise ").fill(provider.get("edit_expertise"))
    page.get_by_placeholder("Enter Education, Work Experience").fill(provider.get("edit_workExperience"))
    
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Provider updated successfully.").click()
    page.wait_for_timeout(1000)
    
    # verification
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill(f"{provider.get('edit_fname')} {provider.get('edit_lname')}")
    page.get_by_role("heading", name=f"{provider.get('edit_fname')} {provider.get('edit_lname')}").click()
    page.get_by_text(provider.get("edit_contact_num")).click()
    # page.locator(f"//p[@aria-label={provider.get('edit_email')}]").click()
    # View Profile
    page.get_by_role("button", name="View Profile").click()
    page.get_by_title("View Provider User").get_by_text(f"{provider.get('edit_fname')} {provider.get('edit_lname')}").click()
    page.get_by_text("MD", exact=True).click()      # Provider Type
    page.get_by_text(provider.get("edit_gender")).click()
    page.get_by_text(provider.get("edit_dob")).click()
    page.get_by_title("View Provider User").get_by_text(provider.get("edit_contact_num")).click()
    page.get_by_text(provider.get("edit_email")).click()
    page.get_by_text(provider.get("edit_npi_number")).click()
    page.get_by_text(provider.get("edit_bio")).click()
    page.get_by_text(provider.get("edit_fax_num")).click()
    page.get_by_text(provider.get("edit_taxonomy_num")).click()
    # page.get_by_text("1.undefined (6894697732) ( undefined)").click()       # Licensed Details
    page.get_by_text("IST (Indian Standard Time (UTC +5:30))").click()
    page.get_by_text(local_data.pg_location).click()
    # page.get_by_text(f"1. American LIFECARE").click() 
    # page.get_by_text(f"2. American Medical Security Inc.").click()
    page.get_by_text(provider.get("edit_yearOfExperience")).click()
    page.get_by_text(provider.get("edit_workExperience")).click()
    page.get_by_test_id("CloseIcon").click()