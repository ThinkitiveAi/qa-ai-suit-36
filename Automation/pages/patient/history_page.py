from playwright.sync_api import Page
from Automation.utils import data

def history(page: Page, history: dict):
    # HISTORY
    page.get_by_role("tab", name="History").click()
    # Past Medical History
    page.get_by_role("tab", name="Past Medical History").click()
    # Add Past Medical History
    
    page.get_by_role("button", name="Add Past Medical History").click()
    page.get_by_placeholder("Enter Condition Name").fill(history["condition1"])
    page.get_by_placeholder("Choose date").click()
    page.get_by_placeholder("Choose date").fill("03-15-2018")
    page.get_by_placeholder("Type here").fill(history["condition1_note"])
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Medical history created successfully").click()
    
    page.get_by_role("cell", name=history["condition1"]).click(click_count=3)
    page.get_by_role("cell", name="03/15/2018").click()
    page.get_by_role("cell", name=history["condition1_note"]).click()
    page.get_by_role("cell", name=data.formatted_date).click()
    page.get_by_test_id("MoreVertIcon").first.click()
    
    # Edit
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_placeholder("Enter Condition Name").fill(history["condition2"])
    page.get_by_placeholder("Choose date").click()
    page.get_by_placeholder("Choose date").fill("09-01-2015")
    page.get_by_placeholder("Type here").fill(history["condition2_note"])
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Medical history updated successfully").click()
    
    page.get_by_role("cell", name=history["condition2"]).click(click_count=3)
    page.get_by_role("cell", name="09/01/2015").click()
    page.get_by_role("cell", name=history["condition2_note"]).click()
    page.get_by_role("cell", name=data.formatted_date).click()
    page.get_by_test_id("MoreVertIcon").first.click()
    
    # Delete
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_text("Are You Sure?").click()
    page.get_by_text("you want to delete this Past Medical History").click()
    page.get_by_role("button", name="Yes,Sure").click()
    page.get_by_text("Medical history archived successfully").click()


    # Past Surgical History
    page.get_by_role("tab", name="Past Surgical History").click()
    # Add Past Surgical History
    
    page.get_by_role("button", name="Add Past Surgical History").click()
    page.get_by_placeholder("Enter Surgery Name").fill(history["surgery1_name"])
    page.get_by_placeholder("Choose date").click()
    page.get_by_placeholder("Choose date").fill("02-20-2021")
    page.get_by_placeholder("Type here").fill(history["surgery1_note"])
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Past Surgical history created successfully").click()
    
    page.get_by_role("cell", name=history["surgery1_name"]).click(click_count=3)
    page.get_by_role("cell", name="02/20/2021").click()
    page.get_by_role("cell", name=history["surgery1_note"]).click()
    page.get_by_role("cell", name=data.formatted_date).click()
    page.get_by_test_id("MoreVertIcon").first.click()
    
    # Edit
    
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_role("heading", name="Edit Past Surgical History")
    page.get_by_placeholder("Enter Surgery Name").fill(history["surgery2_name"])
    page.get_by_placeholder("Choose date").click()
    page.get_by_placeholder("Choose date").fill("04-15-2017")
    page.get_by_placeholder("Type here").fill(history["surgery2_note"])
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Past Surgical history updated successfully").click()
    
    page.get_by_role("cell", name=history["surgery2_name"]).click(click_count=3)
    page.get_by_role("cell", name="04/15/2017").click()
    page.get_by_role("cell", name=history["surgery2_note"]).click()
    page.get_by_role("cell", name=data.formatted_date).click()
    page.get_by_test_id("MoreVertIcon").first.click()
    
    # Delete
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_text("Are You Sure?").click()
    page.get_by_text("you want to delete this Past Surgical History").click()
    page.get_by_role("button", name="Yes,Sure").click()
    page.get_by_text("Past Surgical history archived successfully").click()

    
    # Family History
    page.get_by_role("tab", name="Family History").click()
    # Add Family History
    
    page.get_by_role("button", name="Add Family History").click()
    page.get_by_role("heading", name="Add Family History").get_by_text("Add Family History").click()
    page.get_by_placeholder("Select or Search Problem").fill(history["problem1_name"][1])
    page.get_by_role("option", name=history["problem1_name"][0]).click()
    page.locator("input[name=\"relative\"]").click()
    page.get_by_role("option", name="Father", exact=True).click()
    page.get_by_placeholder("Enter Age").fill("65")
    page.get_by_placeholder("Type here").fill(history["problem1_note"])
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Family history created successfully").click()

    page.get_by_role("cell", name=history["problem1_name"][0], exact=True).click(click_count=3)
    page.get_by_role("cell", name="Father", exact=True).click()
    page.get_by_role("cell", name="65", exact=True).click()
    page.get_by_role("cell", name=data.formatted_date).click()
    page.get_by_role("cell", name=history["problem1_note"]).click()
    page.get_by_test_id("MoreVertIcon").click()
    
    # Edit
    page.get_by_role("menuitem", name="Edit").click()    
    page.get_by_role("heading", name="Edit Past Family History").get_by_text("Edit Past Family History").click()
    page.get_by_placeholder("Select or Search Problem").fill(history["problem2_name"][1])
    page.get_by_role("option", name=history["problem2_name"][0]).click()
    page.locator("input[name=\"relative\"]").click()
    page.get_by_role("option", name="Mother").click()
    page.get_by_placeholder("Enter Age").fill("60")
    page.get_by_placeholder("Type here").fill(history["problem2_note"])
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Family history updated successfully").click()
    
    page.get_by_role("cell", name=history["problem2_name"][0], exact=True).click(click_count=3)
    page.get_by_role("cell", name="Mother").click()
    page.get_by_text("60", exact=True).click()
    page.get_by_role("cell", name=data.formatted_date).click()
    page.get_by_role("cell", name=history["problem2_note"]).click()
    page.get_by_test_id("MoreVertIcon").click()
    
    # Delete
    page.get_by_role("menuitem", name="Delete").click()
    page.get_by_text("Are You Sure?").click()
    page.get_by_text("you want to delete this Family History").click()
    page.get_by_role("button", name="Yes,Sure").click()
    page.get_by_text("Family history archived successfully").click()
    print("History Module : PASS")