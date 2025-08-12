from playwright.sync_api import Page
from Automation.utils import data

def allergy(page: Page, allergy: dict):
    # ALLERGIES
    page.get_by_role("tab", name="Allergies").click()
    
    page.get_by_role("button", name="Add Allergy").click()
    page.get_by_placeholder("Enter Allergy Name").fill(allergy.get("allergy_name"))
    page.get_by_placeholder("Select Severity").click()
    page.get_by_role("option", name=allergy.get("allergy_severity")).click()
    page.get_by_placeholder("Enter Reaction").fill(allergy.get("allergy_reaction"))
    page.get_by_placeholder("Choose Date").click()
    page.get_by_placeholder("Choose Date").fill("03-22-2020")
    page.get_by_placeholder("Select", exact=True).click()
    page.get_by_role("option", name="Inactive").click()
    page.get_by_placeholder("Type here").fill(allergy.get("allergy_note"))
    page.get_by_role("button", name="Save").click()    
    page.get_by_text("Allergy created successfully").click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("cell", name=allergy.get("allergy_name")).click(click_count=3)
    page.get_by_role("cell", name=allergy.get("allergy_reaction")).click()
    page.get_by_role("cell", name=allergy.get("allergy_severity")).click()
    page.get_by_role("cell", name="03/22/2020").click()
    page.get_by_role("cell", name=data.formatted_date).click()
    page.get_by_role("cell", name="Inactive").click()
    page.get_by_role("cell", name=allergy.get("allergy_note")).click()
    page.get_by_test_id("MoreVertIcon").click()
    
    # Edit
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_placeholder("Enter Allergy Name").click()
    page.get_by_placeholder("Enter Allergy Name").fill(allergy.get("edit_allergy_name"))
    page.get_by_placeholder("Select Severity").click()
    page.get_by_role("option", name=allergy.get("edit_allergy_severity")).click()
    page.get_by_placeholder("Enter Reaction").fill(allergy.get("edit_allergy_reaction"))
    page.get_by_placeholder("Choose Date").click()
    page.get_by_placeholder("Choose Date").fill("05-27-2021")
    page.get_by_placeholder("Select", exact=True).click()
    page.get_by_role("option", name="Active", exact=True).click()
    page.get_by_placeholder("Type here").fill(allergy.get("edit_allergy_note"))
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Allergy updated successfully").click()
    
    page.get_by_role("cell", name=allergy.get("edit_allergy_name"), exact=True).click(click_count=3)
    page.get_by_role("cell", name=allergy.get("edit_allergy_reaction")).click()
    page.get_by_role("cell", name=allergy.get("edit_allergy_severity")).click()
    page.get_by_role("cell", name="05/27/2021").click()
    page.get_by_role("cell", name=data.formatted_date).click()
    page.get_by_role("cell", name="Active").click()
    page.get_by_role("cell", name=allergy.get("edit_allergy_note")).click()
    page.get_by_test_id("MoreVertIcon").click()
    
    # Delete
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_text("Are You Sure?").click()
    page.get_by_text("you want to delete this Allergy").click()
    page.get_by_role("button", name="Yes,Sure").click()
    page.get_by_text("Allergy archived successfully").click()
    print("Allergy Module : PASS")