from playwright.sync_api import Page
from Automation.utils import constants, creds, local_data


def providerGroup(page: Page, providerGroup: dict):
    
    page.get_by_text("Provider Groups", exact=True).nth(1).click()
    # Create Provider Group
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Add Provider Group", exact=True).click()
    page.get_by_role("heading", name="Add Provider Group").get_by_text("Add Provider Group").click(click_count=3)
    
    page.get_by_placeholder("Enter Provider Group Name").click()
    page.get_by_placeholder("Enter Provider Group Name").fill(providerGroup.get("pg_name"))
        
    page.get_by_placeholder("Enter Sub Domain").click()
    page.get_by_placeholder("Enter Sub Domain").fill(providerGroup.get("pg_subdomain"))
    
    page.locator("//p[.='Speciality Type']/following::div[1]//input[@placeholder='Select']").click()
    # page.get_by_placeholder("Select").first.click()
    for i in constants.speciality:
        page.get_by_role("option", name=i, exact=True).get_by_role("checkbox").check()
    
    page.get_by_placeholder("Enter Group NPI Number").fill(providerGroup.get("pg_groupNpiNumber"))
        
    page.get_by_placeholder("Enter Contact Number").click()
    page.get_by_placeholder("Enter Contact Number").type(providerGroup.get("pg_contactNumber"), delay=20)
    
    page.get_by_placeholder("Enter Email").fill(providerGroup.get("pg_email"))
    
    page.get_by_placeholder("Enter Fax ID").fill(providerGroup.get("pg_faxId2"))
    page.wait_for_timeout(1000)
    page.get_by_placeholder("Select").first.click()
    page.get_by_placeholder("Select").first.fill(constants.insurance[0])
    page.get_by_role("option", name=constants.insurance[0], exact=True).get_by_role("checkbox").check()
    page.locator("(//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedStart MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-1y3zh1'])[2]").fill(constants.insurance[1])
    page.get_by_role("option", name=constants.insurance[1], exact=True).get_by_role("checkbox").check()
    
    page.get_by_placeholder("Select").first.click()
    page.get_by_placeholder("Select").first.press("ArrowDown")
    page.wait_for_timeout(400)
    page.get_by_placeholder("Select").first.press("Enter")
    
    page.get_by_placeholder("Select").first.click()
    page.get_by_role("option", name="Pacific Standard Time (UTC -8)").click()

    page.get_by_placeholder("Enter Website").click()
    page.get_by_placeholder("Enter Website").fill(providerGroup.get("pg_website"))
    
    page.get_by_placeholder("Enter Information").fill("Demo Information")

    page.get_by_placeholder("Address Line 1").first.click()
    page.get_by_placeholder("Address Line 1").first.fill("Happy Street")
    page.get_by_placeholder("Address Line 2").first.click()
    page.get_by_placeholder("Address Line 2").first.fill("Lane 1")

    page.locator("(//input[@placeholder='City'])[1]").click()
    page.locator("(//input[@placeholder='City'])[1]").fill("Santacruz")
        
    page.locator("(//input[@placeholder='State'])[1]").click()
    page.get_by_role("option", name="California (CA)").click()

    page.locator("(//input[@placeholder='Country'])[1]").click()
    page.get_by_role("option", name="United States").click()

    page.locator("(//input[@placeholder='Zip Code'])[1]").click()
    page.locator("(//input[@placeholder='Zip Code'])[1]").fill("234567")
    
    page.get_by_text("Same as Physical Address").check()
    
    # Upload Photo
    file_input = page.query_selector('input[type="file"]')
    file_path = "./Automation/utils/uploads/Hospital3.jpg"
    file_input.set_input_files(file_path)
    
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Save").click()
    if (page.get_by_text("Provider group is created successfully.").is_visible(timeout=50000)):
        page.get_by_placeholder("Search By Name", exact=True).click()
        page.get_by_placeholder("Search By Name", exact=True).fill(providerGroup.get("pg_name"))
        page.wait_for_timeout(1000)
        page.get_by_text(providerGroup.get("pg_name")).first.click()
        print(f"Added provider group : {providerGroup.get('pg_name')}")
    page.wait_for_timeout(1500)
    page.get_by_text(providerGroup.get("pg_name"), exact=True).click()
    page.get_by_text(providerGroup.get("pg_groupNpiNumber"), exact=True).click()
    page.get_by_text(providerGroup.get("pg_website"), exact=True).click()
    page.get_by_text(providerGroup.get("pg_contactNumber"), exact=True).click()
    page.get_by_text(providerGroup.get("pg_email"), exact=True).click()
    # page.get_by_text(providerGroup.get("pg_faxId"), exact=True).click()
    page.get_by_text("Happy Street, Lane 1, Santacruz, CA, 234567").first.click()
    page.get_by_text("Happy Street, Lane 1, Santacruz, CA, 234567").nth(1).click()
    page.get_by_text(constants.insurance[0], exact=True).click()
    page.get_by_text(constants.insurance[1], exact=True).click()
    page.get_by_text("Demo Information", exact=True).click()
    print("Added Provider Group details verified successfully")
    
    # Edit Provider Group
    page.get_by_role("button", name="Edit Profile").click()
    page.wait_for_timeout(1000)
    page.get_by_role("heading", name="Edit Provider Group Profile").click(click_count=3)
    
    page.get_by_placeholder("Enter Provider Group Name").click()
    page.get_by_placeholder("Enter Provider Group Name").fill(providerGroup.get("pg_name2"))

    page.get_by_placeholder("Enter Sub Domain").click()
    page.get_by_placeholder("Enter Sub Domain").fill(providerGroup.get("pg_subdomain2"))
    
    page.locator("(//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedStart MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-1y3zh1'])[1]").click()
    for x in constants.speciality[:2]:    
        page.get_by_role("option", name=x, exact=True).get_by_role("checkbox").uncheck()
    
    page.get_by_placeholder("Enter Group NPI Number").fill(providerGroup.get("pg_groupNpiNumber2"))
    
    page.get_by_placeholder("Enter Contact Number").click()
    page.get_by_placeholder("Enter Contact Number").press("Control+a")
    page.get_by_placeholder("Enter Contact Number").fill("")
    page.get_by_placeholder("Enter Contact Number").type(providerGroup.get("pg_contactNumber2"))
    
    page.get_by_placeholder("Enter Email").fill(providerGroup.get("pg_email2"))
    
    # page.get_by_placeholder("Enter Fax ID").fill(pg_faxId2)
    page.wait_for_timeout(1000)
    page.get_by_placeholder("Select").first.click()
    page.locator("(//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedStart MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-1y3zh1'])[2]").fill(constants.insurance[1])
    page.get_by_role("option", name=constants.insurance[1]).get_by_role("checkbox").uncheck()
    
    page.get_by_placeholder("Select").first.click()
    page.get_by_role("option", name="Indian Standard Time (UTC +5:30)").click()

    page.get_by_placeholder("Enter Website").click()
    page.get_by_placeholder("Enter Website").fill(providerGroup.get("pg_website2"))
    
    page.get_by_placeholder("Enter Information").fill("Test Information")
    
    page.get_by_placeholder("Address Line 1").first.fill("Happy Street 1")
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
    
    page.get_by_text(providerGroup.get("pg_name2")).first.click()
    print(f"updated provider group : {providerGroup.get('pg_name2')}")
    page.wait_for_timeout(1500)
    page.get_by_text(providerGroup.get("pg_name2"), exact=True).click()
    page.get_by_text(providerGroup.get("pg_groupNpiNumber2"), exact=True).click()
    page.get_by_text(providerGroup.get("pg_website2"), exact=True).click()
    page.get_by_text(providerGroup.get("pg_contactNumber2"), exact=True).click()
    page.get_by_text(providerGroup.get("pg_email2"), exact=True).click()
    # page.get_by_text(providerGroup.get("pg_faxId2"), exact=True).click()
    page.get_by_text("Happy Street 1, Lane 2, Oswego, AK, 948567", exact=True).first.click()
    page.get_by_text("Happy Street 1, Lane 2, Oswego, AK, 948567", exact=True).nth(1).click()
    page.get_by_text(constants.insurance[0], exact=True).click()
    page.get_by_text("Test Information", exact=True).click()
    print("Updated Provider Group details verified successfully")
    
    # LOCATION
    page.get_by_role("tab", name="Locations").click()
    page.get_by_role("heading", name=providerGroup.get("pg_name2"), exact=True).click()
    page.get_by_text(providerGroup.get("pg_groupNpiNumber2")).click()          # group npi
    page.get_by_text(providerGroup.get("pg_contactNumber2")).click()          # contact number
    page.get_by_text(providerGroup.get("pg_email2")).click()      
    page.get_by_text(providerGroup.get("pg_website2")).click()
    page.get_by_text("Happy Street 1, Lane 2, Oswego, AK, 948567").click()

    # ADD LOCATION
    page.get_by_role("button", name="Add Location").click()
    page.get_by_role("heading", name=f"Add Location For {providerGroup.get('pg_name2')}").click(click_count=3)
    page.get_by_placeholder("Enter Location Name").fill(providerGroup.get("loc_name"))
    page.locator("(//input[@placeholder='Select'])[1]").click()
    for specialities in constants.speciality[4:]:
        page.get_by_role("option", name=specialities).click()
    page.get_by_placeholder("Enter Location ID").fill(providerGroup.get("loc_Id"))
    page.get_by_placeholder("Enter Contact Number").type(providerGroup.get("loc_contact_num"))
    page.get_by_placeholder("Enter Email").fill(providerGroup.get("loc_email"))
    page.get_by_placeholder("Enter Fax ID").fill(providerGroup.get("loc_fax"))
    page.get_by_placeholder("Enter Information").fill("Demo Location Information")
    
    page.get_by_placeholder("Address Line 1").first.fill("Happy Street")
    page.get_by_placeholder("Address Line 2").first.fill("Lane 3")
    page.locator("(//input[@placeholder='City'])[1]").fill("Santacruz")
    page.locator("(//input[@placeholder='Select'])[2]").click()
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
    page.get_by_text(providerGroup.get("loc_name")).hover()
    page.get_by_text(providerGroup.get("loc_Id")).click()
    print(f"Added Location : {providerGroup.get('loc_name')}")
    
    page.get_by_role("tab", name="Details").click()
    page.get_by_role("paragraph").filter(has_text=providerGroup.get("loc_name")).click()
    page.get_by_role("paragraph").filter(has_text=providerGroup.get("loc_Id")).click()
    page.get_by_role("paragraph").filter(has_text=providerGroup.get("loc_contact_num")).click()
    page.get_by_text(providerGroup.get("loc_email")).click()
    page.get_by_text(providerGroup.get("loc_fax")).click()
    page.locator("(//p[text()='Happy Street'])[1]").click()
    page.locator("(//p[text()='Lane 3'])[1]").click()
    page.locator("(//p[text()='Santacruz'])[1]").click()
    page.locator("(//p[text()='CA'])[1]").click()
    page.locator("(//p[text()='United States'])[1]").click()
    page.locator("(//p[text()='234567'])[1]").click()
    print("Added Location details verified successfully")
    
    # EDIT LOCATION
    page.get_by_role("button", name="Edit Profile").click()
    page.get_by_placeholder("Enter Location Name").fill(providerGroup.get("loc_name2"))
    page.get_by_placeholder("Enter Location ID").fill(providerGroup.get("loc_Id2"))
    page.get_by_placeholder("Enter Contact Number").type(providerGroup.get("loc_contact_num2"))
    page.get_by_placeholder("Enter Email").fill(providerGroup.get("loc_email2"))
    page.get_by_placeholder("Enter Fax ID").fill(providerGroup.get("loc_fax2"))
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
    page.get_by_placeholder("Search By Name", exact=True).click()
    page.get_by_placeholder("Search By Name", exact=True).fill(providerGroup.get("loc_name2"))
    page.wait_for_timeout(1000)
    
    page.get_by_text(providerGroup.get("loc_name2")).hover()
    page.get_by_text(providerGroup.get("loc_Id2")).click()
    print(f"Updated Location : {providerGroup.get('loc_name2')}")
    
    page.get_by_role("tab", name="Details").click()
    page.get_by_role("paragraph").filter(has_text=providerGroup.get("loc_name2")).click()

    page.get_by_role("paragraph").filter(has_text=providerGroup.get("loc_Id2")).click()
    page.get_by_role("paragraph").filter(has_text=providerGroup.get("loc_contact_num2")).click()
    page.get_by_text(providerGroup.get("loc_email2")).click()
    page.get_by_text(providerGroup.get("loc_fax2")).click()
    page.locator("(//p[text()='Happy Street A'])[1]").click()
    page.locator("(//p[text()='Lane 4'])[1]").click()
    page.locator("(//p[text()='United States'])[1]").click()
    page.locator("(//p[text()='CA'])[1]").click()
    page.locator("(//p[text()='Santacruz'])[1]").click()
    page.locator("(//p[text()='234889'])[1]").click()
    print("Updated Location details verified successfully")

    # Adding Another Location
    page.get_by_role("button", name="Location").click()
    page.get_by_role("button", name="Add Location").click()
    page.get_by_role("heading", name=f"Add Location For {providerGroup.get('pg_name2')}").click(click_count=3)
    
    page.get_by_placeholder("Enter Location Name").fill(providerGroup.get("loc_name3"))
    page.get_by_placeholder("Select").first.click()
    for specialities in constants.speciality[3:]:
        page.get_by_role("option", name=specialities).click()
    page.get_by_placeholder("Enter Location ID").fill(providerGroup.get("loc_Id3"))
    page.get_by_placeholder("Enter Contact Number").type(providerGroup.get("loc_contact_num3"))
    page.get_by_placeholder("Enter Email").fill(providerGroup.get("loc_email3"))
    page.get_by_placeholder("Enter Fax ID").fill(providerGroup.get("loc_fax3"))
    page.get_by_placeholder("Enter Information").fill("Demo Location Information")
    
    page.get_by_placeholder("Address Line 1").first.fill("Happy Street")
    page.get_by_placeholder("Address Line 2").first.fill("Lane 3")
    page.locator("(//input[@placeholder='City'])[1]").fill("Santacruz")
    page.locator("(//input[@placeholder='Select'])[2]").click()
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
    
    page.get_by_placeholder("Search By Name", exact=True).click()
    page.get_by_placeholder("Search By Name", exact=True).fill(providerGroup.get("loc_name3"))
    page.wait_for_timeout(1000)
    
    # verification
    page.get_by_text(providerGroup.get("loc_name3")).hover()
    page.get_by_text(providerGroup.get("loc_Id3")).click()
    print(f"Added Another Location : {providerGroup.get('loc_name3')}")
    
    page.get_by_role("tab", name="Details").click()
    page.get_by_role("paragraph").filter(has_text=providerGroup.get("loc_name3")).click()
    page.get_by_role("paragraph").filter(has_text=providerGroup.get("loc_Id3")).click()
    page.get_by_role("paragraph").filter(has_text=providerGroup.get("loc_contact_num3")).click()
    page.get_by_text(providerGroup.get("loc_email3")).click()
    page.get_by_text(providerGroup.get("loc_fax3")).click()
    page.get_by_role("button", name="Location").click()
    print("Another Added Location details verified successfully")
    
    # STAFF
    page.get_by_role("tab", name="Staffs").click()
    # Add Staff
    page.get_by_role("button", name="Add Staff User").click()
    page.get_by_placeholder("Enter First Name").fill(providerGroup.get("staff_fname"))
    page.get_by_placeholder("Enter Last Name").fill(providerGroup.get("staff_lname"))
    page.get_by_placeholder("MM-DD-YYYY").fill("05-15-1993")
    page.get_by_placeholder("Select").first.click()
    page.get_by_role("option", name="Female", exact=True).click()
    page.get_by_placeholder("Enter Email").fill(providerGroup.get("staff_email")) 
    page.get_by_placeholder("Enter Contact Number").fill(providerGroup.get("staff_number"))
    page.get_by_placeholder("Select Role").click()
    page.get_by_role("option", name="Biller").click()
    page.get_by_placeholder("Select").nth(2).click()
    page.get_by_role("option", name=providerGroup.get("loc_name2")).click()
    
    # Upload Photo
    file_input = page.query_selector('input[type="file"]')
    file_path = "./ecarehealth_ui_automation/eCareHealth_tests/uploads/staff1.jpg"
    file_input.set_input_files(file_path)
    
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Save").click()
    page.get_by_text("User created successfully.").click()
    page.wait_for_timeout(1000)
    
    page.get_by_text("Biller").click()
    page.get_by_text(providerGroup.get("staff_number")).click()
    page.get_by_text(providerGroup.get("staff_email")).click()
    page.get_by_text(f"{providerGroup.get('staff_fname')} {providerGroup.get('staff_lname')}").click()
    print(f"Added Staff User : {providerGroup.get('staff_fname')} {providerGroup.get('staff_lname')}")
        
    page.locator(f"//p[text()='Name']/following::p[text()='{providerGroup.get('staff_fname')} {providerGroup.get('staff_lname')}']").click()
    page.locator("//p[text()='DOB']/following::p[text()='05-15-1993']").click()
    page.get_by_title("User Profile").get_by_text(providerGroup.get("staff_number")).click()
    page.get_by_text("BILLER", exact=True).click()
    page.get_by_title("User Profile").get_by_text(providerGroup.get("staff_email")).click()
    page.get_by_text("Female", exact=True).click()
    page.get_by_text("STAFF", exact=True).click()
    print("Added Staff details verified successfully")
    page.get_by_test_id("CloseIcon").click()
    page.get_by_test_id("MoreVertIcon").first.click()

    # Edit Staff User 
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_placeholder("Enter First Name").fill(providerGroup.get("staff_fname2"))
    page.get_by_placeholder("Enter Last Name").fill(providerGroup.get("staff_lname2"))
    page.get_by_placeholder("MM-DD-YYYY").fill("06-18-1991")
    # page.get_by_placeholder("Select", exact=True).click()
    # page.get_by_role("option", name="Male", exact=True).click()
    page.get_by_placeholder("Enter Email").fill(providerGroup.get("staff_email2"))
    page.get_by_placeholder("Enter Contact Number").type(providerGroup.get("staff_number2"))
    page.get_by_placeholder("Select Role").click()
    page.get_by_role("option", name="Nurse").click()

    # Upload Photo
    file_input = page.query_selector('input[type="file"]')
    file_path = "./ecarehealth_ui_automation/eCareHealth_tests/uploads/staff2.jpg"
    file_input.set_input_files(file_path)
    
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Save").click()
    page.get_by_text("User profile updated successfully.").click()
    page.wait_for_timeout(1000)
    
    page.get_by_placeholder("Search By Name", exact=True).fill(f"{providerGroup.get('staff_fname2')} {providerGroup.get('staff_lname2')}")
    page.wait_for_timeout(1500)    
    page.get_by_text("Nurse").click()
    page.get_by_text(providerGroup.get("staff_number2")).click()
    page.get_by_text(providerGroup.get("staff_email2")).click()
    page.locator(f"//p[text()='{providerGroup.get('staff_fname2')} {providerGroup.get('staff_lname2')}']").click()
    print(f"Updated Staff User : {providerGroup.get('staff_fname2')} {providerGroup.get('staff_lname2')}")
    
    page.get_by_text("User Profile").click(click_count=3)
    page.get_by_title("User Profile").get_by_text(f"{providerGroup.get('staff_fname2')} {providerGroup.get('staff_lname2')}").click()
    page.get_by_title("User Profile").get_by_text(providerGroup.get("staff_email2")).click()
    page.locator("//p[text()='DOB']/following::p[text()='06-18-1991']").click()
    page.get_by_text("Male", exact=True).click()
    page.get_by_title("User Profile").get_by_text(providerGroup.get("staff_number2")).click()
    page.get_by_text("STAFF", exact=True).click()
    page.get_by_text("NURSE", exact=True).click()
    print("Updated Staff details verified successfully")
    page.get_by_test_id("CloseIcon").click()
    
    # Adding Another Staff
    page.get_by_role("button", name="Add Staff User").click()
    page.get_by_placeholder("Enter First Name").fill(providerGroup.get("staff_fname3"))
    page.get_by_placeholder("Enter Last Name").fill(providerGroup.get("staff_lname3"))
    page.get_by_placeholder("MM-DD-YYYY").fill("08-20-1990")
    page.get_by_placeholder("Select").first.click()
    page.get_by_role("option", name="Male", exact=True).click()
    page.get_by_placeholder("Enter Email").fill(providerGroup.get("staff_email3"))
    page.get_by_placeholder("Enter Contact Number").fill(providerGroup.get("staff_number3"))
    page.get_by_placeholder("Select Role").click()
    page.get_by_role("option", name="Nurse").click()
    page.get_by_placeholder("Select").nth(2).click()
    page.get_by_role("option", name=providerGroup.get("loc_name3")).click()
    
    # Upload Photo
    file_input = page.query_selector('input[type="file"]')
    file_path = "./ecarehealth_ui_automation/eCareHealth_tests/uploads/staff2.jpg"
    file_input.set_input_files(file_path)
    
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Save").click()
    page.get_by_text("User created successfully.").click()
    page.wait_for_timeout(1000)
    
    page.get_by_placeholder("Search By Name", exact=True).click()
    page.get_by_placeholder("Search By Name", exact=True).fill(f"{providerGroup.get('staff_fname3')} {providerGroup.get('staff_lname3')}")
    
    page.get_by_text("Nurse").click()
    page.get_by_text(providerGroup.get("staff_number3")).click()
    page.get_by_text(providerGroup.get("staff_email3")).click()
    page.locator(f"//p[text()='{providerGroup.get('staff_fname3')} {providerGroup.get('staff_lname3')}']").click()
    print(f"Added Another Staff User : {providerGroup.get('staff_fname3')} {providerGroup.get('staff_lname3')}")
    
    page.get_by_title("User Profile").get_by_text(f"{providerGroup.get('staff_fname3')} {providerGroup.get('staff_lname3')}").click()
    page.locator("//p[text()='DOB']/following::p[text()='08-20-1990']").click()
    page.get_by_title("User Profile").get_by_text(providerGroup.get("staff_number3")).click()
    page.get_by_text("NURSE", exact=True).click()
    page.get_by_title("User Profile").get_by_text(providerGroup.get("staff_email3")).click()
    page.get_by_text("Male", exact=True).click()
    page.get_by_text("STAFF", exact=True).click()
    print("Another Added Staff details verified successfully")
    page.get_by_test_id("CloseIcon").click()
    
    # DEPARTMENTS
    page.get_by_role("tab", name="Departments").click()
    # Add Department
    page.get_by_role("button", name="Add Department").click()
    page.get_by_placeholder("Enter Department ID").fill(providerGroup.get("dept_Id"))
    page.get_by_placeholder("Enter Department Name").fill(providerGroup.get("dept_name"))
    page.get_by_placeholder("Select Department Admin").click()
    page.get_by_role("option", name=f"{providerGroup.get('staff_fname2')} {providerGroup.get('staff_lname2')}", exact=True).click()
    page.get_by_placeholder("Enter Contact Number").type(providerGroup.get("dept_contact_num"))
    page.get_by_placeholder("Select", exact=True).click()
    page.get_by_role("option", name=providerGroup.get("loc_name2"), exact=True).click()      #location
    page.wait_for_timeout(1000)    
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Department created successfully.").click()

    # verification
    page.get_by_text(providerGroup.get("dept_Id")).click()
    page.get_by_text(providerGroup.get("dept_name")).click()
    print(f"Added Department : {providerGroup.get('dept_name')}")
    page.get_by_text(f"{providerGroup.get('staff_fname2')} {providerGroup.get('staff_lname2')}").click()
    page.get_by_text(providerGroup.get("dept_contact_num")).click()
    print("Added Department details verified successfully")
    page.get_by_test_id("MoreVertIcon").click()
    
    # Edit Department
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_placeholder("Enter Department ID").fill(providerGroup.get("dept_Id2"))
    page.get_by_placeholder("Enter Department Name").fill(providerGroup.get("dept_name2"))
    page.get_by_placeholder("Select Department Admin").click()
    page.get_by_role("option", name=f"{providerGroup.get('staff_fname3')} {providerGroup.get('staff_lname3')}").click()
    page.get_by_placeholder("Enter Contact Number").type(providerGroup.get("dept_contact_num2"))
    page.locator("//input[@class='MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall MuiInputBase-inputAdornedStart MuiInputBase-inputAdornedEnd MuiAutocomplete-input MuiAutocomplete-inputFocused css-1y3zh1']").click()
    page.get_by_role("option", name=providerGroup.get("loc_name3"), exact=True).get_by_role("checkbox").check()
    page.wait_for_timeout(1000)    
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Department updated successfully.").click()
    page.wait_for_timeout(1000)    
    
    # verification
    page.get_by_text(providerGroup.get("dept_Id2")).click()
    page.get_by_text(providerGroup.get("dept_name2")).click()
    print(f"Updated Department : {providerGroup.get('dept_name2')}")
    page.get_by_text(f"{providerGroup.get('staff_fname3')} {providerGroup.get('staff_lname3')}").click()
    page.get_by_text(providerGroup.get("dept_contact_num2")).click()
    print("Updated Department details verified successfully")
    
    # PROVIDER
    page.get_by_role("tab", name="Providers").click()
    # Add
    page.get_by_role("button", name="Add Provider User").click()
    page.get_by_placeholder("First Name").fill(providerGroup.get("fname"))
    page.get_by_placeholder("Last Name").fill(providerGroup.get("lname"))
    print("Provider User Name :", providerGroup.get("fname"), providerGroup.get("lname"))
    page.locator("(//input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="PA").click()
    page.locator("(//input[@placeholder='Select'])[2]").click()
    for i in constants.speciality[3:]:
        page.get_by_role("option", name=i).click()
    page.wait_for_timeout(1000)
    page.locator("(//input[@placeholder='Select'])[2]").click()
    page.get_by_role("option", name=providerGroup.get("role")).click()
    page.get_by_placeholder("MM-DD-YYYY").first.fill(providerGroup.get("dob"))
    page.locator("(//input[@placeholder='Select'])[3]").click()
    page.get_by_role("option", name=providerGroup.get("gender"), exact=True).click()
    page.locator("input[name=\"npi\"]").fill(providerGroup.get("npi_number"))
    page.get_by_placeholder("Enter Contact Number").type(providerGroup.get("contact_num"))
    page.locator("input[name=\"officeFaxNumber\"]").fill(providerGroup.get("fax_num"))
    # page.locator("(//input[@placeholder='Select'])[4]").click()
    # for x in constants.insurance:
    #     page.locator("(//input[@placeholder='Select'])[4]").fill(x)
    #     page.get_by_role("option", name=x).click()
    page.get_by_placeholder("Enter Year Of Experience").fill(providerGroup.get("yearOfExperience"))
    page.locator("input[name=\"taxonomyNumber\"]").fill(providerGroup.get("taxonomy_num"))
    page.locator("(//input[@placeholder='Select'])[5]").click()
    page.get_by_role("option", name=local_data.pg_location1).click()
    page.get_by_placeholder("Enter Email").fill(providerGroup.get("email"))
    page.locator("(//input[@placeholder='Select'])[5]").click()
    page.get_by_role("option", name="Indian Standard Time (UTC +5:30)").click()
    
    page.locator("(//input[@placeholder='Select'])[6]").click()
    page.get_by_role("option", name=providerGroup.get("state"))
    page.locator("input[name=\"licenseNumber\"]").fill(providerGroup.get("license_num"))
    page.get_by_placeholder("Enter Bio").fill(providerGroup.get("bio"))
    page.get_by_placeholder("Enter Expertise ").fill(providerGroup.get("expertise"))
    page.get_by_placeholder("Enter Education, Work Experience").fill(providerGroup.get("workExperience"))
    
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Provider created successfully.").click()
    page.wait_for_timeout(1000)
    
    # verification
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill(f"{providerGroup.get('fname')} {providerGroup.get('lname')}")
    page.locator(f"//p[text()='{providerGroup.get('email')}']").click()
    page.locator(f"//div[text()='{providerGroup.get('contact_num')}']").click()
    page.locator(f"//div[text()='{providerGroup.get('role')}']").click()
    page.get_by_text(f"{providerGroup.get('fname')} {providerGroup.get('lname')}").click()
    print(f"Added Provider : {providerGroup.get('fname')} {providerGroup.get('lname')}")
    # View Provider User
    page.get_by_text("PA", exact=True).click()      # Provider Type
    page.get_by_text(providerGroup.get("gender"), exact=True).click()
    page.get_by_text(providerGroup.get("dob")).click()
    page.get_by_title("View Provider User").get_by_text(providerGroup.get("contact_num")).click()
    page.get_by_title("View Provider User").get_by_text(providerGroup.get("email")).click()
    page.get_by_text(providerGroup.get("npi_number")).click()
    page.get_by_text(providerGroup.get("bio")).click()
    page.get_by_text(providerGroup.get("fax_num")).click()
    page.get_by_text(providerGroup.get("taxonomy_num")).click()
    # page.get_by_text("1.undefined (6894697732) ( undefined)").click()       # Licensed Details
    page.get_by_text("IST (Indian Standard Time (UTC +5:30))").click()
    page.get_by_text(local_data.pg_location1).click()
    # page.get_by_text(1. American LIFECARE").click()
    # page.get_by_text(2. American Medical Security Inc.").click()
    page.get_by_title("View Provider User").get_by_text(providerGroup.get("yearOfExperience")).click()
    page.get_by_text(providerGroup.get("workExperience")).click()
    print("Added Provider details verified successfully")
    
    # Edit Provider User
    page.get_by_test_id("ModeOutlinedIcon").click()
    page.get_by_placeholder("First Name").fill(providerGroup.get("edit_fname"))
    page.get_by_placeholder("Last Name").fill(providerGroup.get("edit_lname"))
    print("Provider User Name :", providerGroup.get("edit_fname"), providerGroup.get("edit_lname"))
    page.locator("(//input[@placeholder='Select'])[1]").click()
    page.get_by_role("option", name="MD").click()
    # page.locator("(//input[@placeholder='Select'])[2]").click()
    # for i in constants.speciality[3:]:
    #     page.get_by_role("option", name=i).click()
    page.wait_for_timeout(1000)
    # page.locator("(//input[@placeholder='Select'])[2]").click()
    # page.get_by_role("option", name=providerGroup.get("edit_role")).click()
    page.get_by_placeholder("MM-DD-YYYY").first.fill(providerGroup.get("edit_dob"))
    page.locator("(//input[@placeholder='Select'])[3]").click()
    page.get_by_role("option", name=providerGroup.get("edit_gender"), exact=True).click()
    page.locator("input[name=\"npi\"]").fill(providerGroup.get("edit_npi_number"))
    page.get_by_placeholder("Enter Contact Number").type(providerGroup.get("edit_contact_num"))
    page.locator("input[name=\"officeFaxNumber\"]").fill(providerGroup.get("edit_fax_num"))
    # page.locator("(//input[@placeholder='Select'])[4]").click()
    # for x in constants.insurance:
    #     page.get_by_role("option", name=x).click()
    page.get_by_placeholder("Enter Year Of Experience").fill(providerGroup.get("edit_yearOfExperience"))
    page.locator("input[name=\"taxonomyNumber\"]").fill(providerGroup.get("edit_taxonomy_num"))
    
    page.get_by_role("button", name=local_data.pg_location1).hover()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Clear").click()
    page.wait_for_timeout(500)
    page.locator("(//input[@placeholder='Select'])[5]").click()
    page.get_by_role("option", name=local_data.pg_location).click()
    
    page.get_by_placeholder("Enter Email").fill(providerGroup.get("edit_email"))
    page.locator("(//input[@placeholder='Select'])[5]").click()
    page.get_by_role("option", name="Indian Standard Time (UTC +5:30)").click()
    
    page.locator("(//input[@placeholder='Select'])[6]").click()
    page.get_by_role("option", name=providerGroup.get("edit_state"))
    page.locator("input[name=\"licenseNumber\"]").fill(providerGroup.get("edit_license_num"))
    page.get_by_placeholder("Enter Bio").fill(providerGroup.get("edit_bio"))
    page.get_by_placeholder("Enter Expertise ").fill(providerGroup.get("edit_expertise"))
    page.get_by_placeholder("Enter Education, Work Experience").fill(providerGroup.get("edit_workExperience"))
    
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Provider updated successfully.").click()
    page.wait_for_timeout(1000)
    page.get_by_title("View Provider User").get_by_test_id("CloseIcon").click()
    
    # verification
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill(f"{providerGroup.get('edit_fname')} {providerGroup.get('edit_lname')}")    
    page.locator(f"//p[text()='{providerGroup.get('edit_email')}']").click()
    page.locator(f"//div[text()='{providerGroup.get('edit_contact_num')}']").click()
    # page.locator(f"//div[text()='{providerGroup.get('edit_role')}']").click()
    page.get_by_text(f"{providerGroup.get('edit_fname')} {providerGroup.get('edit_lname')}").click()
    print(f"Updated Provider : {providerGroup.get('edit_fname')} {providerGroup.get('edit_lname')}")

    # View Provider User
    page.get_by_text("MD", exact=True).click()      # Provider Type
    page.get_by_text(providerGroup.get("edit_gender"), exact=True).click()
    page.get_by_text(providerGroup.get("edit_dob")).click()
    page.get_by_title("View Provider User").get_by_text(providerGroup.get("edit_contact_num")).click()
    page.get_by_title("View Provider User").get_by_text(providerGroup.get("edit_email")).click()
    page.get_by_text(providerGroup.get("edit_npi_number")).click()
    page.get_by_text(providerGroup.get("edit_bio")).click()
    page.get_by_text(providerGroup.get("edit_fax_num")).click()
    page.get_by_text(providerGroup.get("edit_taxonomy_num")).click()
    # page.get_by_text("1.undefined (6894697732) ( undefined)").click()       # Licensed Details
    page.get_by_text("IST (Indian Standard Time (UTC +5:30))").click()
    page.get_by_text(local_data.pg_location).click()
    # page.get_by_text(1. American LIFECARE").click() 
    # page.get_by_text(2. American Medical Security Inc.").click()
    page.get_by_title("View Provider User").get_by_text(providerGroup.get("edit_yearOfExperience"), exact=True).click()
    page.get_by_text(providerGroup.get("edit_workExperience")).click()
    page.get_by_test_id("CloseIcon").click()
    print("Updated Provider details verified successfully")