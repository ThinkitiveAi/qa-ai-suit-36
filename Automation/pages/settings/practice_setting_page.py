from playwright.sync_api import Page

from Automation.utils import constants, creds

def practiceSetting(page: Page, practice: dict):
    page.get_by_role("tab", name="Settings").click()
    # Practice Settings
    page.get_by_text("Practice Settings").click()
    # Edit Provider Group
    page.get_by_role("button", name="Edit Profile").click()
    page.wait_for_timeout(1000)
    page.get_by_role("heading", name="Edit Provider Group Profile").click(click_count=3)
    
    page.get_by_placeholder("Enter Provider Group Name").click()
    page.get_by_placeholder("Enter Provider Group Name").fill(practice.get("pg_name2"))
    
    page.get_by_text("Speciality Type").click()
    page.get_by_placeholder("Select").first.click()
    for i in constants.speciality[3:]:
        page.get_by_role("option", name=i).get_by_role("checkbox").check()
    
    page.get_by_placeholder("Enter Group NPI Number").fill(practice.get("pg_groupNpiNumber2"))
    
    page.get_by_placeholder("Enter Contact Number").click()
    page.get_by_placeholder("Enter Contact Number").press("Control+a")
    page.get_by_placeholder("Enter Contact Number").fill("")
    page.get_by_placeholder("Enter Contact Number").type(practice.get("pg_contactNumber2"))
    
    page.get_by_placeholder("Enter Email").fill(practice.get("pg_email2"))
    
    # page.get_by_placeholder("Enter Fax ID").fill(pg_faxId2)
    page.wait_for_timeout(1000)
    page.get_by_placeholder("Select").first.click()
    page.get_by_placeholder("Select").first.fill(constants.insurance[0])
    page.get_by_role("option", name=constants.insurance[0]).get_by_role("checkbox").check()
    # page.locator("(//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedStart MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-1y3zh1'])[2]").fill(constants.insurance[1])
    # page.get_by_role("option", name=constants.insurance[1]).get_by_role("checkbox").check()
    
    page.get_by_placeholder("Select").first.click()
    page.get_by_role("option", name="Indian Standard Time (UTC +5:30)").click()

    page.get_by_placeholder("Enter Website").click()
    page.get_by_placeholder("Enter Website").fill(practice.get("pg_website2"))
    
    page.get_by_placeholder("Enter Information").fill("Test Information")
    
    page.get_by_placeholder("Address Line 1").first.click()
    page.get_by_placeholder("Address Line 1").first.fill("Happy Street 1")
    page.get_by_placeholder("Address Line 2").first.click()
    page.get_by_placeholder("Address Line 2").first.fill("Lane 2")

    page.locator("(//input[@placeholder='City'])[1]").click()
    page.locator("(//input[@placeholder='City'])[1]").fill("Oswego")
        
    page.locator("(//input[@placeholder='State'])[1]").click()
    page.get_by_role("option", name="Alaska (AK)").click()

    page.locator("(//input[@placeholder='Country'])[1]").click()
    page.get_by_role("option", name="United States").click()

    page.locator("(//input[@placeholder='Zip Code'])[1]").click()
    page.locator("(//input[@placeholder='Zip Code'])[1]").fill("948567")
    
    page.get_by_text("Same as Physical Address").check()
    
    # Upload Photo
    file_input = page.query_selector('input[type="file"]')
    file_path = "./Automation/utils/uploads/MGhospital.jpg"
    file_input.set_input_files(file_path)
    
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Provider group updated successfully.").click()
    page.wait_for_timeout(2000)
    
    page.get_by_text(practice.get("pg_name2")).first.click()
    print(f"updated provider group : {practice.get('pg_name2')}")
    page.wait_for_timeout(1500)
    page.get_by_text(practice.get("pg_name2"), exact=True).click()
    page.get_by_text(practice.get("pg_groupNpiNumber2"), exact=True).click()
    page.get_by_text(practice.get("pg_website2"), exact=True).click()
    page.get_by_text(practice.get("pg_contactNumber2"), exact=True).click()
    page.get_by_text(practice.get("pg_email2"), exact=True).click()
    # page.get_by_text(practice.get("pg_faxId2"), exact=True).click()
    page.get_by_text("Happy Street 1, Lane 2, Oswego, AK, 948567", exact=True).first.click()
    page.get_by_text("Happy Street 1, Lane 2, Oswego, AK, 948567", exact=True).nth(1).click()
    # page.get_by_text(constants.insurance[0], exact=True).click()
    # page.get_by_text(constants.insurance[1], exact=True).click()
    page.get_by_text("Test Information", exact=True).click()
    
    # LOCATION
    page.get_by_role("tab", name="Locations").click()
    page.get_by_role("heading", name=practice.get("pg_name2"), exact=True).click()
    page.get_by_text(practice.get("pg_groupNpiNumber2")).click()
    page.get_by_text(practice.get("pg_contactNumber2")).click()
    page.get_by_text(practice.get("pg_email2")).click()      
    page.get_by_text(practice.get("pg_website2")).click()
    page.get_by_text("Happy Street 1, Lane 2, Oswego, AK, 948567").click()

    # ADD LOCATION
    page.get_by_role("button", name="Add Location").click()
    page.get_by_role("heading", name=f"Add Location For {practice.get('pg_name2')}").click(click_count=3)
    page.get_by_placeholder("Enter Location Name").fill(practice.get("loc_name"))
    page.locator("(//input[@placeholder='Select'])[1]").click()
    for specialities in constants.speciality[3:]:
        page.get_by_role("option", name=specialities).click()
    page.get_by_placeholder("Enter Location ID").fill(practice.get("loc_Id"))
    page.get_by_placeholder("Enter Contact Number").type(practice.get("loc_contact_num"))
    page.get_by_placeholder("Enter Email").fill(practice.get("loc_email"))
    page.get_by_placeholder("Enter Fax ID").fill(practice.get("loc_fax"))
    page.get_by_placeholder("Enter Information").fill("Demo Location Information")
    
    page.get_by_placeholder("Address Line 1").first.fill("Happy Street")
    page.get_by_placeholder("Address Line 2").first.fill("Lane 3")
    page.locator("(//input[@placeholder='City'])[1]").fill("Santacruz")
    page.locator("(//input[@placeholder='Select'])[3]").click()
    page.get_by_role("option", name="California (CA)").click()
    page.locator("(//input[@placeholder='Country'])[1]").click()
    page.get_by_role("option", name="United States").click()
    page.locator("(//input[@placeholder='Zip Code'])[1]").fill("234567")
    
    page.get_by_text("Same as Physical Address").check()
    
    # Upload Photo
    file_input = page.query_selector('input[type="file"]')
    file_path = "./ecarehealth_ui_automation/eCareHealth_tests/uploads/Hospital2.jpg"
    file_input.set_input_files(file_path)
    
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Location added successfully.").click()
    page.wait_for_timeout(2000)
    
    # verification
    page.get_by_placeholder("Search By Name", exact=True).fill(practice.get("loc_name"))
    page.wait_for_timeout(1000)
    page.get_by_text(practice.get("loc_name")).click(click_count=3)
    page.get_by_text(practice.get("loc_Id")).click()
    
    page.get_by_role("tab", name="Details").click()
    page.get_by_role("paragraph").filter(has_text=practice.get("loc_name")).click()
    page.get_by_role("paragraph").filter(has_text=practice.get("loc_Id")).click()
    page.get_by_role("paragraph").filter(has_text=practice.get("loc_contact_num")).click()
    page.get_by_text(practice.get("loc_email")).click()
    page.get_by_text(practice.get("loc_fax")).click()
    page.locator("(//p[text()='Happy Street'])[1]").click()
    page.locator("(//p[text()='Lane 3'])[1]").click()
    page.locator("(//p[text()='Santacruz'])[1]").click()
    page.locator("(//p[text()='CA'])[1]").click()
    page.locator("(//p[text()='United States'])[1]").click()
    page.locator("(//p[text()='234567'])[1]").click()
    
    # EDIT LOCATION
    page.get_by_role("button", name="Edit Profile").click()
    page.get_by_placeholder("Enter Location Name").fill(practice.get("loc_name2"))
    page.get_by_placeholder("Enter Location ID").fill(practice.get("loc_Id2"))
    page.get_by_placeholder("Enter Contact Number").type(practice.get("loc_contact_num2"))
    page.get_by_placeholder("Enter Email").fill(practice.get("loc_email2"))
    page.get_by_placeholder("Enter Fax ID").fill(practice.get("loc_fax2"))
    page.locator("//input[@name='timezone']").click()
    page.get_by_role("option", name="Indian Standard Time (UTC +5:30)").click()
    page.get_by_placeholder("Enter Information").fill("Test Location Information")
    
    page.get_by_placeholder("Address Line 1").first.fill("Happy Street A")
    page.get_by_placeholder("Address Line 2").first.fill("Lane 4")
    page.locator("(//input[@placeholder='City'])[1]").fill("Santacruz")
    page.locator("(//input[@placeholder='Zip Code'])[1]").fill("234889")
    
    # Upload Photo
    file_input = page.query_selector('input[type="file"]')
    file_path = "./ecarehealth_ui_automation/eCareHealth_tests/uploads/Hospital1.jpeg"
    file_input.set_input_files(file_path)
    
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Location updated successfully.").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Location").click()
    
    # verification
    page.get_by_placeholder("Search By Name", exact=True).fill(practice.get("loc_name2"))
    page.wait_for_timeout(1000)
    
    page.get_by_text(practice.get("loc_name2")).click(click_count=3)
    page.get_by_text(practice.get("loc_Id2")).click()
    
    page.get_by_role("tab", name="Details").click()
    page.get_by_role("paragraph").filter(has_text=practice.get("loc_name2")).click()

    page.get_by_role("paragraph").filter(has_text=practice.get("loc_Id2")).click()
    page.get_by_role("paragraph").filter(has_text=practice.get("loc_contact_num2")).click()
    page.get_by_text(practice.get("loc_email2")).click()
    page.get_by_text(practice.get("loc_fax2")).click()
    page.locator("(//p[text()='Happy Street A'])[1]").click()
    page.locator("(//p[text()='Lane 4'])[1]").click()
    page.locator("(//p[text()='United States'])[1]").click()
    page.locator("(//p[text()='CA'])[1]").click()
    page.locator("(//p[text()='Santacruz'])[1]").click()
    page.locator("(//p[text()='234889'])[1]").click()
    page.get_by_role("button", name="Location").click()
    
    # DEPARTMENTS
    page.get_by_role("tab", name="Departments").click()
    # Add Department
    page.get_by_role("button", name="Add Department").click()
    page.get_by_placeholder("Enter Department ID").fill(practice.get("dept_Id"))
    page.get_by_placeholder("Enter Department Name").fill(practice.get("dept_name"))
    page.get_by_placeholder("Select Department Admin").click()
    page.get_by_role("option", name=practice.get("staff_user"), exact=True).click()
    page.get_by_placeholder("Enter Contact Number").type(practice.get("dept_contact_num"))
    page.get_by_placeholder("Select", exact=True).click()
    page.get_by_role("option", name=practice.get("loc_name2"), exact=True).click()      #location
    page.wait_for_timeout(1000)    
    page.get_by_role("button", name="Save").click()
    # page.get_by_text("Department created successfully.").click()

    # verification
    page.get_by_text(practice.get("dept_Id")).click()
    page.get_by_text(practice.get("dept_name")).click()
    page.get_by_text(practice.get("staff_user")).click()
    page.get_by_text(practice.get("dept_contact_num")).click()
    page.get_by_test_id("MoreVertIcon").click()
    
    # Edit Department
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_placeholder("Enter Department ID").fill(practice.get("dept_Id2"))
    page.get_by_placeholder("Enter Department Name").fill(practice.get("dept_name2"))
    page.get_by_placeholder("Select Department Admin").click()
    page.get_by_role("option", name=practice.get("staff_user1")).click()
    page.get_by_placeholder("Enter Contact Number").type(practice.get("dept_contact_num2"))
    page.get_by_placeholder("Select", exact=True).click()
    page.get_by_role("option", name=practice.get("loc_name3"), exact=True).click()  
    page.wait_for_timeout(1000)    
    page.get_by_role("button", name="Save").click()
    # page.get_by_text("Department updated successfully.").click()
    page.wait_for_timeout(1000)    
    
    # verification
    page.get_by_text(practice.get("dept_Id2")).click()
    page.get_by_text(practice.get("dept_name2")).click()
    page.get_by_text(practice.get("staff_user1")).click()
    page.get_by_text(practice.get("dept_contact_num2")).click()