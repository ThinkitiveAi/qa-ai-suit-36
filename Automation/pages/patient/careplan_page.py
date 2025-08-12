from playwright.sync_api import Page

from Automation.utils import creds, local_data

def careplan(page: Page, careplan: dict):
    # CAREPLAN
    page.get_by_role("tab", name="Care Plan").click()
    # Add New Care Plan
    page.get_by_role("button", name="Add New Care Plan").click()
    page.get_by_placeholder("Individualized Care Plan").fill(careplan["cp_title1"])
    page.get_by_placeholder("Enter Condition").fill(careplan["cp_condition1"])
    page.get_by_placeholder("Start Date").fill("01-01-2024")
    page.get_by_placeholder("End Date").fill("12-31-2024")
    page.get_by_placeholder("Select").click()
    page.get_by_role("option", name="Inactive", exact=True).click()
    page.get_by_placeholder("Enter Description").fill(careplan["cp_description1"])
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Care plan created successfully").click()

    page.get_by_role("tab", name="Historical Care Plan").click()
    page.get_by_role("cell", name=careplan["cp_title1"], exact=True).click()
    page.get_by_role("heading", name="View Care Plan").get_by_test_id("CloseIcon").click()
    page.get_by_role("cell", name=careplan["cp_condition1"], exact=True).click()
    page.get_by_role("cell", name="01/01/2024").click()
    page.get_by_role("cell", name="12/31/2024").click()
    page.get_by_role("cell", name=local_data.provider1).click()
    page.get_by_role("cell", name=careplan["cp_description1"]).click()
    page.get_by_role("cell", name="Completed").click()
    page.get_by_test_id("MoreVertIcon").click()
    
    # Edit
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_placeholder("Individualized Care Plan").fill(careplan["cp_title2"])
    page.get_by_placeholder("Enter Condition").fill(careplan["cp_condition2"])
    page.get_by_placeholder("Start Date").fill("02-01-2025")
    page.get_by_placeholder("End Date").fill("12-31-2025")
    page.get_by_placeholder("Select").click()
    page.get_by_role("option", name="Active", exact=True).click()
    page.get_by_placeholder("Enter Description").fill(careplan["cp_description2"])
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Care plan updated successfully").click()
    
    page.get_by_role("tab", name="Active Care Plan").click()
    page.get_by_role("cell", name=careplan["cp_title2"], exact=True).click()
    page.get_by_role("heading", name="View Care Plan").get_by_test_id("CloseIcon").click()
    page.get_by_role("cell", name=careplan["cp_condition2"], exact=True).click()
    page.get_by_role("cell", name="02/01/2025").click()
    page.get_by_role("cell", name="12/31/2025").click()
    page.get_by_role("cell", name=local_data.provider1).click()
    page.get_by_role("cell", name=careplan["cp_description2"]).click()
    page.get_by_role("cell", name="Active").click()
    page.get_by_test_id("MoreVertIcon").click()
    
    # Delete
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_text("Are You Sure?").click()
    page.get_by_text("you want to delete this Careplan").click()
    page.get_by_role("button", name="Yes,Sure").click()
    page.get_by_text("Care plan archived successfully").click()
    print("Careplan Module : PASS")
